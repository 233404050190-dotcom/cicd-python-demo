#!/bin/bash
set -e

URL="http://localhost:8000/health"
MAX_RETRIES=5
WAIT_TIME=3

echo "==> Bắt đầu Health Check ứng dụng tại: $URL"

for ((i=1; i<=MAX_RETRIES; i++)); do
    HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL" || true)
    echo "Lần $i/$MAX_RETRIES: Status code = $HTTP_STATUS"

    if [ "$HTTP_STATUS" -eq 200 ]; then
        echo "==> HEALTH CHECK PASSED: Ứng dụng đã sẵn sàng!"
        exit 0
    fi

    sleep $WAIT_TIME
done

echo "==> HEALTH CHECK FAILED: Ứng dụng không phản hồi (Status: $HTTP_STATUS)!"
echo "==> Đang kích hoạt tiến trình ROLLBACK..."

# Kịch bản khôi phục: Tắt container lỗi và chạy lại bản trước đó
docker compose -f docker-compose.prod.yml down || true

if [ -n "$PREVIOUS_IMAGE" ]; then
    echo "==> Rollback về Image: $PREVIOUS_IMAGE"
    DOCKER_IMAGE=$PREVIOUS_IMAGE docker compose -f docker-compose.prod.yml up -d
fi

echo "==> Quá trình Rollback hoàn tất. Vui lòng kiểm tra log hệ thống."
exit 1
