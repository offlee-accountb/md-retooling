# Auth Backend

MD Retooling 인증 백엔드 서비스

## 설치 및 실행

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env
# .env 파일에서 JWT_SECRET_KEY 수정 필수!

# 서버 실행
python main.py
# 또는
uvicorn main:app --reload
```

## API 문서

서버 실행 후:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 엔드포인트

### 인증 API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | 회원가입 |
| POST | `/auth/login` | 로그인 (토큰 발급) |
| POST | `/auth/refresh` | 토큰 갱신 |
| GET | `/auth/me` | 현재 사용자 정보 |
| POST | `/auth/logout` | 로그아웃 |

### 요청/응답 예시

#### 회원가입
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123",
    "name": "홍길동"
  }'
```

Response:
```json
{
  "user_id": 1,
  "message": "User registered successfully"
}
```

#### 로그인
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

Response:
```json
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### 사용자 정보 조회
```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer {access_token}"
```

Response:
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "홍길동",
  "is_active": true,
  "is_verified": false,
  "created_at": "2025-11-30T12:00:00"
}
```

#### 토큰 갱신
```bash
curl -X POST http://localhost:8000/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "eyJ..."
  }'
```

## 프론트엔드 연동 가이드

### 토큰 저장
```javascript
// 로그인 후
const response = await fetch('/auth/login', { ... });
const { access_token, refresh_token } = await response.json();

localStorage.setItem('access_token', access_token);
localStorage.setItem('refresh_token', refresh_token);
```

### API 요청 시
```javascript
const response = await fetch('/api/some-endpoint', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
  }
});
```

### 토큰 갱신 (401 에러 시)
```javascript
if (response.status === 401) {
  const refreshResponse = await fetch('/auth/refresh', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      refresh_token: localStorage.getItem('refresh_token')
    })
  });
  
  if (refreshResponse.ok) {
    const { access_token, refresh_token } = await refreshResponse.json();
    localStorage.setItem('access_token', access_token);
    localStorage.setItem('refresh_token', refresh_token);
    // 원래 요청 재시도
  } else {
    // 로그인 페이지로 리다이렉트
  }
}
```

## 환경변수

| 변수 | 설명 | 기본값 |
|------|------|--------|
| JWT_SECRET_KEY | JWT 서명 키 (필수 변경!) | dev-secret-key |
| JWT_ALGORITHM | JWT 알고리즘 | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | 액세스 토큰 만료(분) | 30 |
| REFRESH_TOKEN_EXPIRE_DAYS | 리프레시 토큰 만료(일) | 7 |
| DATABASE_URL | 데이터베이스 URL | sqlite+aiosqlite:///./auth.db |
| DEBUG | 디버그 모드 | true |

## 프로덕션 배포 시 주의사항

1. **JWT_SECRET_KEY 변경 필수** - 충분히 긴 랜덤 문자열 사용
2. **CORS 설정** - `allow_origins`를 실제 도메인으로 제한
3. **HTTPS 사용** - 토큰이 평문으로 전송되지 않도록
4. **데이터베이스** - SQLite 대신 PostgreSQL 등 사용 권장
