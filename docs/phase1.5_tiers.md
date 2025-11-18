# Phase 1.5 Tier Testing Log

> Option B note: 모든 Tier 검증 실험은 이 파일 하나에만 기록하여 필요 시 통째로 보관하거나 폐기할 수 있도록 한다.

## 목적 & 범위
- Phase 1.5 Validator가 다양한 난이도의 샘플을 얼마나 커버하는지 추적한다.
- 실행 명령, 결과 요약, 회고 코멘트를 모두 한 곳에 모아 추후 정리/삭제를 단순화한다.
- Tier별 샘플은 `validator/tier_test/tier0~tier3/`에만 적재한다 (외부 공유 금지).

## Tier 정의
| Tier | 초점 | 요구 기능 | 샘플 유형 |
|------|------|-----------|------------|
| Tier 0 | Phase 1 최소 형태 | 단일 섹션, 기본 스타일, 표 없음 | `templates/phase1_5_sample.yaml` 대응 HWPX |
| Tier 1 | 레이아웃 다양성 | 제목/소제목 혼합, spacer, 기본 표 | Option B에서 확보한 File 2 경량 버전 |
| Tier 2 | 메타데이터/표 집중 | 복수 표, 머리말/꼬리말, 강조 블록 | 기관 배포본에서 추출한 정식 샘플 |
| Tier 3 | 풀 스펙 | 조건부 블록, 복합 스타일, 주석 | 실제 제출본에 가장 근접한 상위 난이도 |

> Tier 정의는 필요 시 갱신하되, 변경 내역은 아래 Run Log에 자유 형식으로 기록한다.

## Validator 실행 흐름
1. 샘플 파일을 지정된 Tier 폴더에 배치 (예: `validator/tier_test/tier1/sample_a.hwpx`).
2. 템플릿 또는 추가 설정이 필요하면 동일 폴더에 YAML/메모를 둔다.
3. 다음 명령으로 검증 진행:
   ```bash
   python -m validator.cli validate-phase1-5 \
     templates/phase1_5_sample.yaml \
     validator/tier_test/<tier>/sample.hwpx \
     --format text
   ```
4. 결과를 아래 Run Log에 자유롭게 요약하고, 필요 시 후속 작업을 `CURRENT_ISSUES.md`에 링크한다.

## Run Log & Compatibility Status (Free-Form)
- **2025-11-16 상태:** Tier 0 샘플(`output/test_final.hwpx`)은 `templates/phase1_5_sample.yaml`과 비교 시 통과. Tier 1~3 샘플은 아직 미수신 상태라 검증 대기 중.
- 추후 실행 기록은 날짜/샘플/명령/결과/메모 순으로 자유롭게 작성한다. 로그가 과도해지면 이 문서를 보관용으로 아카이브하거나 삭제한다.
- **2025-11-16 실행:** `/bin/python3 converter/md_to_hwpx.py converter/sample_input.md output/test_final.hwpx` → `/bin/python3 validator/cli.py templates/phase1_5_sample.yaml output/test_final.hwpx --format text` (PASS 29/29). 메모: content.hpf에 2016 확장 namespace 및 메타데이터 세트를 추가했고, `Preview/PrvText.txt` + 1x1 PNG 썸네일을 자동 생성하도록 복원. Validator 초기 실패 이력 해소됨.
- **2025-11-16 실행:** `/bin/python3 converter/md_to_hwpx.py converter/sample_input.md output/test_final.hwpx` → `/bin/python3 validator/cli.py templates/phase1_5_sample.yaml output/test_final.hwpx --format text` (PASS 29/29). 메모: 724×1024 단색 `Preview/PrvImage.png` 플레이스홀더를 새로 포함하고 텍스트 프리뷰와 동시생성하도록 유지. Tier0 기준으로는 Option A 메타데이터 구조 + 프리뷰 자산이 모두 안정 동작 확인.
- **Option A 메모 (2025-11-16):** Paragraph layout/indent 재작업은 고위험 요소로 분류되어 당분간 보류한다. 관련 변경은 `converter/md_to_hwpx.py`에서 명시적으로 플래그를 켠 뒤 충분한 검증 루프(`converter/sample_input.md` → validator) 하에서만 진행한다.
- **Preview 자산 계획:** Hangul Tier1 산출물과의 구조적 차이를 줄이기 위해 `Preview/PrvText.txt`와 PNG 썸네일을 다시 생성 대상으로 편입한다. 실제 구현은 메타데이터/namespace 동기화 이후 단계에서 수행하며, 최종 검증 루프에 포함한다.
