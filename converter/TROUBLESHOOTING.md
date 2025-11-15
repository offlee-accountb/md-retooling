# Troubleshooting - 해결된 문제 기록

> Phase 1 개발 중 발생한 문제와 해결 방법 아카이브
> 
> **목적:** 유사 문제 재발 시 빠른 해결, 다음 양식 개발 시 참고

---

## 작성 규칙

### 형식
```markdown
## [YYYY-MM-DD] 문제: 간단한 제목

### 증상
- 어떤 문제가 발생했는가
- 에러 메시지, 현상

### 원인
- 왜 발생했는가

### 해결 방법
- 어떻게 해결했는가
- 코드/설정

### 참고
- 표준 스펙 위치
- 관련 이슈
```

### 작성 시점
- ✅ 문제 **해결 완료** 후
- ❌ 해결 중에는 `CURRENT_ISSUES.md` 사용

---

## 해결된 문제들

<!-- 
아래부터 해결된 문제 기록
최신이 위로
-->

## [2025-11-15] 문제: 생성한 HWPX가 한글에서 열리지 않음

### 증상
- `md_to_hwpx.py`로 만든 문서를 한글에서 열면 “문서 변환코드를 선택하라”는 오류가 뜨고, 내용이 깨진 바이너리처럼 보임.

### 원인
- OCF/HWPX 패키지 구성요소가 빠져 있었음.
  - `META-INF/manifest.xml`, `META-INF/container.rdf`, `contents/content.hpf`의 spine 등이 누락.
  - `version.xml` 속성도 최소값만 들어 있어서 Hancom 뷰어가 패키지를 인정하지 못함.

### 해결 방법
1. `test_inputmodel.hwpx`, `test_minimal_manual.hwpx`를 비교 분석해 필수 파일/속성을 정리.
2. `md_to_hwpx.py`에 다음 빌더를 추가/수정:
   - `build_manifest_xml()`, `build_container_rdf()`, `build_container_xml()` (rootfile 2개 등록).
   - `build_content_hpf()`에서 manifest/spine/metadata를 표준대로 생성.
   - `build_version_xml()` 속성 보완.
3. `write_hwpx()`에서 누락된 XML을 ZIP에 포함하고, `mimetype`를 `application/hwp+zip`으로 수정.
4. 새로 생성한 `output/test_styled?.hwpx`를 한글에서 열어 정상 동작 확인.

### 참고
- 관련 이슈: `converter/CURRENT_ISSUES.md` (2025-11-15 이전 기록)
- 스펙 링크: `docs/hwpx_spec.md`
- 비교용 샘플: `converter/test_inputmodel.hwpx`

---

<!-- 예시 (실제 문제 발생 시 이 예시 삭제)

## [2024-11-15] 문제: 줄간격이 140%로 나옴

### 증상
- 설정은 160%인데 생성된 HWPX에서 140%로 표시
- 한글 프로그램에서 확인 시 줄간격 틀림

### 원인
- HWPX 표준에서 줄간격은 비율이 아닌 절대값 사용
- 160% = 1.6이 아니라 특정 단위 값 필요

### 해결 방법
```python
# Before (잘못된 방법)
line_spacing = 1.6

# After (올바른 방법)
line_spacing = 160  # 단위: %를 의미하는 정수값
```

### 참고
- 표준 스펙: `docs/hwpx_spec.md` 섹션 3.2.4
- 검색: `python tools/spec_search.py "줄간격 line-spacing"`

-->
