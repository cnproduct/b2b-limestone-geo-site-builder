# VPS 运维详细手册

## 连接
- 别名 `tianya-deploy`（`~/.ssh/config`）：`43.130.32.54:2222`，用户 `ubuntu`，经 `198.19.0.1:3128` HTTP CONNECT 代理。
- 本环境 ssh 不自动读取用户 config，**每次**显式 `-F ~/.ssh/config`。
- 密码认证：用户在聊天中提供，允许临时使用；**绝不**写入任何文件、记忆或聊天记录。

## 密码助手的正确写法
expect 脚本只从环境变量 `TY_SSH_PASSWORD` 读密码（exec 工具的 `env` 字段传入）：

```expect
#!/usr/bin/expect -f
set timeout 60
set pw $env(TY_SSH_PASSWORD)
# ssh 模式：argv[2..] 拼成一个远程命令，单引号包裹后传给 ssh
# scp 模式：参数原样拼接
```

**引号陷阱**：构造远程命令时，`&&`/`;`/`|` 必须作为**一个**远程字符串整体加引号传给 ssh，否则会被本地 shell 解析执行——曾因此出现过 `cp` 在本地执行的真实故障。

## 标准部署流程
1. `cp build_tianya_site.py /tmp/build_tianya_site.py.bak.YYYYMMDD_<任务>`（服务器上备份；`main.js` 单独备份，它不由构建器生成）
2. 本地改完做语法检查（`python3 -c "import ast..."` / `node --check`）
3. `scp` 上传到 `/var/www/tianyalimestone.com/`
4. 服务器 `python3 build_tianya_site.py`，核对 `Total HTML pages compiled` 页数（基线 41，加 blog 后 46）
5. `curl -A "Mozilla/5.0" "https://www.tianyalimestone.com/<path>?v=<日期>"` 验证（裸 curl 会被 Cloudflare 403；`?v=` 破边缘缓存）
6. 收尾提醒用户换密码、撤销 token
