#!/bin/bash
# 로컬 개발 서버 실행 스크립트
#
# 사용법:
#   chmod +x scripts/dev.sh
#   ./scripts/dev.sh

set -e

echo "🔧 개발 서버 시작..."

# 가상환경 확인
if [ ! -d "venv" ]; then
    echo "📦 가상환경 생성 중..."
    python3 -m venv venv
fi

# 가상환경 활성화
source venv/bin/activate

# 의존성 설치
echo "📥 의존성 설치 중..."
pip install -q -r requirements.txt
pip install -q email-validator

# 환경변수 설정
if [ ! -f ".env" ]; then
    echo "⚙️  .env 파일 생성 중..."
    cp .env.example .env
fi

# 서버 실행
echo "🚀 서버 시작: http://localhost:8000"
echo "📚 API 문서: http://localhost:8000/docs"
echo ""
echo "종료하려면 Ctrl+C"
echo ""

python main.py
