# 배포 가이드 (바이브코더용)

> 이 문서는 개발 환경에 익숙하지 않은 분을 위한 **단계별 가이드**입니다.

---

## 📋 목차
1. [로컬에서 테스트하기](#1-로컬에서-테스트하기)
2. [Docker로 실행하기](#2-docker로-실행하기)
3. [서버에 배포하기](#3-서버에-배포하기)
4. [자동 배포 설정 (GitHub Actions)](#4-자동-배포-설정)

---

## 1. 로컬에서 테스트하기

### 방법 A: 스크립트 사용 (가장 쉬움)

```bash
# 1. auth_backend 폴더로 이동
cd auth_backend

# 2. 스크립트 실행 권한 부여
chmod +x scripts/dev.sh

# 3. 개발 서버 실행
./scripts/dev.sh
```

### 방법 B: 수동 실행

```bash
# 1. auth_backend 폴더로 이동
cd auth_backend

# 2. 가상환경 생성 (최초 1회)
python3 -m venv venv

# 3. 가상환경 활성화
source venv/bin/activate

# 4. 패키지 설치 (최초 1회)
pip install -r requirements.txt
pip install email-validator

# 5. 환경변수 설정 (최초 1회)
cp .env.example .env

# 6. 서버 실행
python main.py
```

### 테스트 방법

서버가 실행되면:
- 브라우저에서 http://localhost:8000/docs 열기
- Swagger UI에서 API 테스트 가능

---

## 2. Docker로 실행하기

> Docker가 설치되어 있어야 합니다.  
> 설치: https://docs.docker.com/get-docker/

### 방법 A: docker-compose 사용 (추천)

```bash
# 1. auth_backend 폴더로 이동
cd auth_backend

# 2. 개발 모드로 실행
docker-compose -f docker-compose.dev.yml up --build

# 또는 백그라운드로 실행
docker-compose -f docker-compose.dev.yml up -d --build
```

### 방법 B: Docker 직접 실행

```bash
# 1. 이미지 빌드
docker build -t md-retooling-auth .

# 2. 컨테이너 실행
docker run -d \
  --name md-retooling-auth \
  -p 8000:8000 \
  -e JWT_SECRET_KEY="your-secret-key-here" \
  md-retooling-auth
```

### Docker 명령어 모음

```bash
# 로그 보기
docker logs md-retooling-auth

# 실시간 로그
docker logs -f md-retooling-auth

# 컨테이너 중지
docker stop md-retooling-auth

# 컨테이너 재시작
docker restart md-retooling-auth

# 컨테이너 삭제
docker rm md-retooling-auth
```

---

## 3. 서버에 배포하기

### 사전 준비

1. **서버 준비** (AWS EC2, GCP, 등)
   - Ubuntu 22.04 추천
   - 최소 사양: 1 CPU, 1GB RAM

2. **서버에 Docker 설치**
```bash
# Ubuntu에서 Docker 설치
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# 로그아웃 후 다시 로그인
```

### 배포 방법

```bash
# 1. 서버에 접속
ssh user@your-server-ip

# 2. 프로젝트 클론 (또는 파일 업로드)
git clone your-repo-url
cd your-repo/auth_backend

# 3. 환경변수 설정 (중요!)
export JWT_SECRET_KEY="your-super-secret-key-here"

# 4. 배포 스크립트 실행
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

### 🔐 보안 주의사항

**JWT_SECRET_KEY 생성 방법:**
```bash
# 랜덤 키 생성 (터미널에서 실행)
openssl rand -hex 32
```
결과를 복사해서 JWT_SECRET_KEY로 사용하세요.

---

## 4. 자동 배포 설정

> GitHub에 push하면 자동으로 서버에 배포됩니다.

### GitHub Secrets 설정

GitHub repo → Settings → Secrets and variables → Actions → New repository secret

| Secret 이름 | 값 | 설명 |
|------------|-----|------|
| `DOCKER_USERNAME` | your-dockerhub-id | Docker Hub 계정 |
| `DOCKER_PASSWORD` | your-password | Docker Hub 비밀번호 |
| `SERVER_HOST` | 123.456.789.0 | 서버 IP |
| `SERVER_USER` | ubuntu | SSH 사용자명 |
| `SERVER_SSH_KEY` | -----BEGIN... | SSH 개인키 전체 |
| `JWT_SECRET_KEY` | abc123... | JWT 시크릿 |

### SSH 키 생성 (서버 접속용)

```bash
# 로컬에서 실행
ssh-keygen -t ed25519 -C "deploy-key"

# 공개키를 서버에 등록
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server-ip

# 개인키 내용을 GitHub Secret에 등록
cat ~/.ssh/id_ed25519
```

### 배포 확인

1. GitHub에서 코드 push
2. Actions 탭에서 워크플로우 실행 확인
3. 서버에서 `curl http://localhost:8000/health`

---

## 🆘 문제 해결

### "permission denied" 에러
```bash
chmod +x scripts/*.sh
```

### Docker 권한 에러
```bash
sudo usermod -aG docker $USER
# 로그아웃 후 다시 로그인
```

### 포트 8000 사용 중
```bash
# 사용 중인 프로세스 확인
lsof -i :8000

# 프로세스 종료
kill -9 [PID]
```

### 서버 로그 확인
```bash
docker logs md-retooling-auth
```

---

## 📞 다음 단계

인프라 셋업이 완료되면:
1. 도메인 연결 (선택)
2. HTTPS 설정 (Let's Encrypt)
3. Nginx 리버스 프록시 설정

필요하면 말씀해주세요!
