# Production Nginx, Security Headers & Edge Deployment Reference

## 1. Nginx 生产环境配置（高防与 GEO 优化）

`tianyalimestone.com` 在生产服务器部署于 Ubuntu 22.04 LTS，配合 Let's Encrypt 自动化 SSL、静态缓存与精准反爬规则。

```nginx
server {
    server_name www.tianyalimestone.com tianyalimestone.com;
    root /var/www/tianyalimestone.com;
    index index.html;

    # 1. 拦截恶意扫描与非正常批量爬虫（放行 GPTBot, PerplexityBot, ClaudeBot 等正规 AI 引擎）
    if ($http_user_agent ~* (HTTrack|Teleport|Scrapy|WebCopier|Offline\ Explorer|SiteSnagger|WebStripper|SuperBot|BlackWidow|ChinaClaw|Zeus|libwww-perl|SemrushBot|AhrefsBot|DotBot|MJ12bot|BLEXBot|DataForSeoBot|PetalBot)) {
        return 403;
    }

    # 2. 封锁私有与系统脚本文件
    location ~* /\.(git|svn|hg|env|htaccess) {
        return 404;
    }
    location ~* \.(xlsx|csv|bak|sql|py|sh|log|tar\.gz)$ {
        return 404;
    }

    # 3. Gzip 压缩支持
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/rss+xml image/svg+xml;

    # 4. URL 尾斜杠与规范化跳转
    if ($request_uri ~ ^/index\.html(\?.*)?$) {
        return 301 /$1;
    }
    if ($request_uri ~ ^/(.*)/index\.html(\?.*)?$) {
        return 301 /$1/$2;
    }

    # 5. AI 与搜索引擎专用端点放行与 CORS
    location = /robots.txt {
        default_type text/plain;
        charset utf-8;
        add_header Access-Control-Allow-Origin "*" always;
    }
    location = /llms.txt {
        default_type text/plain;
        charset utf-8;
        add_header Access-Control-Allow-Origin "*" always;
    }
    location = /llms-full.txt {
        default_type text/plain;
        charset utf-8;
        add_header Access-Control-Allow-Origin "*" always;
    }
    location /ai/ {
        default_type application/json;
        charset utf-8;
        add_header Access-Control-Allow-Origin "*" always;
    }

    # 6. B2B RFQ 询盘网关反向代理 (Port 8011)
    location /api/ {
        proxy_pass http://127.0.0.1:8011;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 7. 主静态路由与安全头
    location / {
        try_files $uri $uri/ $uri.html =404;
    }

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Content-Security-Policy "frame-ancestors 'self';" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
}
```

---

## 2. 自动化一键部署脚本：`scripts/deploy_remote.sh`

在本地执行：
```bash
./scripts/deploy_remote.sh
```
自动完成：
1. 忽略 macOS `.DS_Store` 与扩展属性打包网站源码与 AI 知识文件；
2. SCP 上传归档至生产服务器 `/tmp/`；
3. 解压并赋予 `ubuntu:www-data` 标准属主权限；
4. 运行 `build_tianya_site.py` 重新生成全量 HTML 页面；
5. 执行 `nginx -t` 并重载 Nginx 服务。
