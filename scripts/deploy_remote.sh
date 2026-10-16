#!/usr/bin/env bash
# ==============================================================================
# deploy_remote.sh - Automated Deployment for Tianya Limestone (tianyalimestone.com)
# Synchronizes compiler, assets, and AI feeds to production and reloads Nginx.
# ==============================================================================

set -euo pipefail

REMOTE_HOST="43.130.32.54"
REMOTE_PORT="2222"
REMOTE_USER="ubuntu"
REMOTE_PASS="WHJCwhjc2026"
REMOTE_DIR="/var/www/tianyalimestone.com"
ARCHIVE_NAME="tianya_site_update_$(date +%Y%m%d_%H%M%S).tar.gz"

echo "=== [1/5] Compiling Production Website & AI Endpoints ==="
python3 build_tianya_site.py
python3 scripts/build_cis_yandex_optimization.py
python3 scripts/validate_site.py

echo "=== [2/5] Packaging Local Web Files (Clean tar, no xattrs) ==="
export COPYFILE_DISABLE=1
tar --no-xattrs -czf "/tmp/${ARCHIVE_NAME}" \
    --exclude=".*" \
    --exclude="*.tar.gz" \
    --exclude="node_modules" \
    --exclude="__pycache__" \
    build_tianya_site.py \
    limestone_category_data.json \
    DESIGN.md \
    README.md \
    acceptance.md \
    rfq_server.py \
    preview_server.py \
    index.html \
    about-us/ \
    contact-us/ \
    compliance/ \
    resources/ \
    blog/ \
    stone-flooring/ \
    ru/ \
    references/ \
    ai/ \
    assets/ \
    data/ \
    scripts/ \
    sitemap.xml \
    robots.txt \
    llms.txt \
    llms-full.txt \
    e8a4c9f21b0d4637a9e52c3f8b7d6e21.txt \
    main.js \
    search_index.js \
    eco-outdoor.css

echo "=== [3/5] Uploading ${ARCHIVE_NAME} to ${REMOTE_HOST}:${REMOTE_PORT} ==="
/opt/homebrew/bin/sshpass -p "${REMOTE_PASS}" scp -o StrictHostKeyChecking=no -P "${REMOTE_PORT}" "/tmp/${ARCHIVE_NAME}" "${REMOTE_USER}@${REMOTE_HOST}:/tmp/"

echo "=== [4/5] Extracting to Production Directory and Setting Permissions ==="
/opt/homebrew/bin/sshpass -p "${REMOTE_PASS}" ssh -o StrictHostKeyChecking=no -p "${REMOTE_PORT}" "${REMOTE_USER}@${REMOTE_HOST}" "
    echo '${REMOTE_PASS}' | sudo -S tar -xzf /tmp/${ARCHIVE_NAME} -C ${REMOTE_DIR}/ && \
    echo '${REMOTE_PASS}' | sudo -S find ${REMOTE_DIR} -name '._*' -delete && \
    echo '${REMOTE_PASS}' | sudo -S chown -R ${REMOTE_USER}:www-data ${REMOTE_DIR} && \
    echo '${REMOTE_PASS}' | sudo -S chmod -R 755 ${REMOTE_DIR} && \
    rm -f /tmp/${ARCHIVE_NAME}
"

echo "=== [5/5] Testing Nginx Configuration & Reloading Service ==="
/opt/homebrew/bin/sshpass -p "${REMOTE_PASS}" ssh -o StrictHostKeyChecking=no -p "${REMOTE_PORT}" "${REMOTE_USER}@${REMOTE_HOST}" "
    echo '${REMOTE_PASS}' | sudo -S nginx -t && \
    echo '${REMOTE_PASS}' | sudo -S systemctl reload nginx
"

echo "=== [6/6] Submitting Realtime IndexNow Notification to Yandex & Bing ==="
python3 scripts/yandex_indexnow_notify.py || true

rm -f "/tmp/${ARCHIVE_NAME}"
echo ">>> DEPLOYMENT COMPLETE! All files and AI feeds are live on https://tianyalimestone.com"
