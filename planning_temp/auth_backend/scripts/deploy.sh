#!/bin/bash
# 수동 배포 스크립트
# 
# 사용법:
#   chmod +x scripts/deploy.sh
#   ./scripts/deploy.sh

set -e  # 에러 시 중단

echo "🚀 배포 시작..."

# 환경변수 확인
if [ -z "$JWT_SECRET_KEY" ]; then
    echo "⚠️  JWT_SECRET_KEY 환경변수가 설정되지 않았습니다."
    echo "   export JWT_SECRET_KEY='your-secret-key' 실행 후 다시 시도하세요."
    exit 1
fi

# Docker 이미지 빌드
echo "📦 Docker 이미지 빌드 중..."
docker build -t md-retooling-auth:latest .

# 기존 컨테이너 중지
echo "🛑 기존 컨테이너 중지..."
docker stop md-retooling-auth 2>/dev/null || true
docker rm md-retooling-auth 2>/dev/null || true

# 새 컨테이너 실행
echo "▶️  새 컨테이너 실행..."
docker run -d \
    --name md-retooling-auth \
    --restart unless-stopped \
    -p 8000:8000 \
    -e JWT_SECRET_KEY="$JWT_SECRET_KEY" \
    -e DATABASE_URL=sqlite+aiosqlite:///./data/auth.db \
    -e DEBUG=false \
    -v auth-data:/app/data \
    md-retooling-auth:latest

# 헬스체크
echo "🏥 헬스체크 중..."
sleep 3
if curl -sf http://localhost:8000/health > /dev/null; then
    echo "✅ 배포 성공! http://localhost:8000"
else
    echo "❌ 헬스체크 실패"
    docker logs md-retooling-auth
    exit 1
fi
