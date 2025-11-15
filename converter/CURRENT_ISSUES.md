# Current Issues - 진행중인 이슈

> Phase 1 개발 중 **현재 해결 중인** 문제들
> 
> **목적:** AI 간 인수인계, 컨텍스트 유지, 중복 시도 방지

---

## ⚠️ 중요

이 파일은 **진행중인 이슈만** 기록합니다.

**해결되면:**
1. 내용을 `TROUBLESHOOTING.md`로 이동
2. 이 파일에서 삭제 또는 [해결됨] 표시

---

## 작성 규칙

### 형식
```markdown
## [진행중] 이슈 제목

**우선순위:** High / Medium / Low  
**담당 AI:** 마지막으로 작업한 AI 이름

### 상황
- 현재 어떤 상태인가
- 어디까지 진행됐는가

### 시도한 방법들
1. [AI명 - 날짜] 방법1 → 결과
2. [AI명 - 날짜] 방법2 → 결과

### 다음 AI에게
- 시도해볼 접근
- 참고할 스펙 위치
- 주의사항

### 관련 파일
- 영향받는 파일들
```

---

## 진행중인 이슈

<!-- 
이슈가 없으면 아래 메시지 유지
이슈 발생 시 이 주석 삭제하고 작성
-->

## [진행중] Generated HWPX files fail to open in Hangul

**우선순위:** High
**담당 AI:** Claude (2025-11-15)

### 상황

`md_to_hwpx.py`로 생성한 HWPX 파일이 한글 프로그램에서 열리지 않음:
- 증상: "문서 변환코드를 선택하라"는 오류 메시지
- 파일 내용이 깨져서 출력됨 (바이너리 데이터처럼 보임)

### 원인 분석 완료

정상 동작하는 `test_inputmodel.hwpx`와 생성된 파일을 비교 분석한 결과:

#### 1. 필수 파일 누락
- ❌ `META-INF/manifest.xml` - 완전히 누락
- ❌ `META-INF/container.rdf` - 완전히 누락

#### 2. 파일 구조 불완전
- ⚠️ `content.hpf`:
  - manifest에 header.xml 항목 없음
  - spine 섹션 완전히 없음
  - 메타데이터 최소화됨
- ⚠️ `container.xml`:
  - rootfile 항목이 content.hpf만 참조
  - container.rdf, PrvText.txt 참조 누락
- ⚠️ `version.xml`:
  - micro, buildNumber, os, xmlVersion, application, appVersion 속성 누락

#### 3. ID 참조 체계
- header.xml과 section0.xml의 ID 참조는 현재 일관성 있음
- 하지만 전체 패키지 구조가 불완전해서 파일 자체가 열리지 않음

### 시도한 방법들

1. [Claude - 11/15] HWPX 구조 비교 분석 → **원인 파악 완료**
2. [Claude - 11/15] 필수 파일 목록 확인 → **누락 파일 식별**

### 다음 AI에게

#### 접근 방법
외부 LLM에 "최소한으로 동작하는 HWPX 패키지" 샘플 요청 후 적용:

1. **요청 문서 작성 완료**: `converter/EXTERNAL_LLM_REQUEST.md`
   - 필수 파일 9개 명시
   - 현재 문제점 상세 설명
   - 성공 기준 명확화

2. **외부 LLM 활용**:
   - 요청 문서를 외부 LLM에 전달
   - 각 파일의 완전한 XML 샘플 받기
   - 스펙 준수 여부 확인 요청

3. **적용 순서**:
   ```
   a. 받은 샘플을 converter/minimal_reference.hwpx로 저장
   b. unzip으로 XML 파일들 추출
   c. md_to_hwpx.py의 빌더 함수들 업데이트:
      - build_manifest_xml() 추가
      - build_container_rdf() 추가
      - build_container_xml() 수정
      - build_content_hpf() 수정 (spine 추가)
      - build_version_xml() 수정 (속성 추가)
   d. write_hwpx() 함수에 누락 파일 추가
   e. 테스트 실행 및 검증
   ```

4. **검증 방법**:
   ```bash
   # 생성
   python3 converter/md_to_hwpx.py converter/sample_input.md output/test_fixed

   # 구조 확인
   unzip -l output/test_fixed.hwpx

   # 실제 한글에서 열기 테스트
   ```

#### 참고할 스펙 위치
- HWPX 표준: `docs/hwpx_spec.md`
- 검색 도구: `tools/spec_search.py`
- 검색 예시:
  ```bash
  python3 tools/spec_search.py "manifest container"
  python3 tools/spec_search.py "package structure"
  ```

#### 주의사항
- **ID 참조 일관성 유지**: header.xml ↔ section0.xml
- **namespace 정확성**: 모든 요소에 올바른 namespace prefix 사용
- **파일 순서**: ZIP 내부 파일 추가 순서가 중요할 수 있음 (mimetype은 첫 번째)
- **encoding**: 모든 XML은 UTF-8, standalone="yes" 권장

### 관련 파일
- `converter/md_to_hwpx.py` (L166-598: XML 빌더 함수들)
- `converter/EXTERNAL_LLM_REQUEST.md` (외부 LLM 요청 문서)
- `converter/test_inputmodel.hwpx` (정상 동작 참조 파일)
- `/tmp/hwpx_analysis/reference/` (추출된 참조 파일들)

### 예상 해결 시간
- 외부 LLM 응답 대기: 변수
- 코드 적용: 1-2시간
- 테스트 및 디버깅: 1-2시간

---

<!-- 예시 형식 (실제 이슈 발생 시 참고)

## [진행중] 제목 스타일이 적용 안됨

**우선순위:** High  
**담당 AI:** GitHub Copilot (2024-11-15)

### 상황
- h1 제목을 18pt 굵게로 설정했으나 실제 HWPX에서 12pt로 나옴
- h2는 정상 작동

### 시도한 방법들
1. [Copilot - 11/15] styles.py에서 크기 직접 지정 → 실패
2. [Copilot - 11/15] HWPX XML에서 직접 수정 → 부분 성공 (굵기만)

### 다음 AI에게
- 표준 스펙 3.1.2 "제목 스타일" 섹션 참고 필요
- CharShape과 ParaShape 두 곳 모두 설정해야 할 가능성
- 검색: `python tools/spec_search.py "제목 heading style"`

### 관련 파일
- `converter/hwpx_generator.py` (L45-67)
- `converter/styles.py` (L12-24)

-->
