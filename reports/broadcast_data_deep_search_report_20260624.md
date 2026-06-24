# 방송 데이터/방송윤리 데이터 심층 탐색 보고서

작성일: 2026-06-24

## 0. 현재 상태
- AI Hub API shell 목록 조회는 로컬 인증 환경에서 확인했다. 공개 저장소에는 API key나 `.secret/` 파일을 포함하지 않는다.
- API shell 목록 조회는 정상 동작한다.
- 단, 실제 다운로드는 데이터셋별 웹 승인 전에는 `인증실패, 권한이 거부되었습니다`로 막힌다.

## 1. 결론: 데이터 우선순위 변경
기존에는 AI Hub 591을 1순위로 보았지만, 전체 AI Hub 목록을 다시 훑은 결과 **71557 뉴스 대본 및 앵커 음성 데이터**가 더 직접적이다. 따라서 우선순위는 다음과 같이 바꾼다.

1. **AI Hub 71557 뉴스 대본 및 앵커 음성 데이터**: 뉴스 대본 benchmark의 1순위.
2. **AI Hub 591 방송 콘텐츠 대본 요약 데이터**: 일반 방송 장르 benchmark의 2순위.
3. **AI Hub 71314 방송콘텐츠 대화체 음성인식 데이터**: 시사/토론/토크쇼 transcript와 speaker subgroup 확장.
4. **AI Hub 463 방송 콘텐츠 대화체 음성인식 데이터**: 추가 ASR transcript 후보. 원천 음성은 매우 커서 라벨 zip만 우선.
5. **AI Hub 558 텍스트 윤리검증 데이터**: 방송 데이터는 아니지만 toxic/non-toxic, hate/discrimination 보조 학습과 Codex prompt calibration용.
6. **방송법/방송심의규정/국가인권위원회 혐오표현 안내서**: annotation guideline의 근거.

## 2. AI Hub 목록 조회 결과

### 2.1 AI Hub 71557 — 뉴스 대본 및 앵커 음성 데이터
파일 트리 확인 결과:
- Training 라벨링데이터: `TL.zip` 244 MB, filekey `558639`
- Validation 라벨링데이터: `VL.zip` 28 MB, filekey `558641`
- Training 원천데이터: `TS.z01` 100 GB, `TS.z02` 100 GB, `TS.zip` 2 GB
- Validation 원천데이터: `VS.zip` 25 GB

판단:
- 뉴스 대본이라는 점에서 우리 benchmark에 가장 직접적이다.
- 우선 음성 원천은 받지 말고 `TL.zip`, `VL.zip`만 받는다.

### 2.2 AI Hub 591 — 방송 콘텐츠 대본 요약 데이터
파일 트리 확인 결과:
- Training 라벨: `TL1.zip` 114 MB, filekey `32781`
- Training 원천: `TS1.zip` 100 MB, filekey `62043`
- Validation 라벨: `VL1.zip` 14 MB, filekey `32783`
- Validation 원천: `VS1.zip` 12 MB, filekey `32784`

판단:
- KBS 방송대본 기반, 장르 다양성 확보에 좋다.
- 크기가 작아서 승인만 되면 전체 다운로드 가능하다.

### 2.3 AI Hub 71314 — 방송콘텐츠 대화체 음성인식 데이터
파일 트리 확인 결과:
- 장르별 라벨 zip: 교양/문화/시사/예능/예술/지식교육/토론/토크쇼, 각 17~42 MB 수준.
- 시사 TL: `465448`, 토론 TL: `465452`, 시사 VL: `465464`, 토론 VL: `465468`.

판단:
- 시사/토론/토크쇼 대화체 transcript가 있으면 context-aware fairness에 좋다.
- speaker/intent metadata가 있으면 subgroup 분석 보조 가능.

### 2.4 AI Hub 463 — 방송 콘텐츠 대화체 음성인식 데이터
파일 트리 확인 결과:
- 원천 음성은 50~90GB 단위로 매우 큼.
- 라벨 zip은 28~47MB 단위.
- Validation label `31637`, Training label `477500` 등.

판단:
- 원천 음성은 받지 말고 label zip만 샘플 확인.

### 2.5 AI Hub 558 — 텍스트 윤리검증 데이터
공개 페이지 기준:
- 한국어 텍스트, JSON.
- 453,340 문장 / 대화세트 132,807건.
- 비윤리 유형: CENSURE, HATE, DISCRIMINATION, SEXUAL, ABUSE, VIOLENCE, CRIME.
- HATE, DISCRIMINATION 분류 성능 지표가 공개되어 있어 toxic/non-toxic 보조 benchmark로 적합.

파일 트리:
- TL1_aihub.zip 33 MB `61875`
- TS1.zip 8 MB `61876`
- VL1_aihub.zip 4 MB `61877`
- VS1.zip 1017 KB `61878`

판단:
- 방송 데이터는 아니므로 최종 test에는 넣지 않는다.
- Codex labeling prompt 보정, toxic classifier pretraining, label mapping sanity check에 사용한다.

## 3. 방송윤리/심의 기준 데이터

### 3.1 방송법 제6조
- 방송 보도는 공정하고 객관적이어야 한다.
- 성별, 연령, 직업, 종교, 신념, 계층, 지역, 인종 등을 이유로 차별을 두어서는 안 된다는 근거가 있다.
- 우리 taxonomy의 protected attributes와 직접 연결된다.

### 3.2 방송심의에 관한 규정
- 방송심의의 구체 기준으로 annotation guideline의 법/정책 근거가 된다.
- 인권보호, 양성평등, 객관성, 공정성 등 label rationale에 연결한다.

### 3.3 국가인권위원회 혐오표현 대항 안내서
- 2024년 발간.
- 여성혐오, 장애 혐오, 재난피해자 혐오, 이슬람혐오, 성소수자 혐오 등 category 보강에 유용하다.

### 3.4 공공데이터포털 방송미디어통신위원회 심결정보
- CSV 856행 다운로드 완료.
- 위치: `13_data_sources/public_downloads/broadcast_regulation/broadcast_media_commission_decision_info_20250531.csv`
- 직접적인 방송대본 데이터는 아니지만, 규제/심결 문서 index로 활용 가능하다.

## 4. 보조 혐오표현 데이터
- Smilegate Korean UnSmile: 혐오/악플/clean, 여성/남성/성소수자/인종/연령/지역/종교 등 multi-label.
- K-MHaS: Korean multi-label hate speech.
- KOCO/BEEP Korean HateSpeech: toxic/bias comment dataset.
- 국립국어원 AI말평 혐오 발언 탐지: binary hate/non-hate task 설계 참고.

판단:
- 방송대본 test에는 넣지 않는다.
- Codex pre-label 검증, toxic/nontoxic classifier pretraining, label taxonomy mapping에만 사용한다.

## 5. 당장 해야 할 일

### 사용자가 웹에서 해야 하는 승인
AI Hub 로그인 후 다음 dataset 페이지에서 다운로드/활용 승인 신청:
1. 71557 뉴스 대본 및 앵커 음성 데이터
2. 591 방송 콘텐츠 대본 요약 데이터
3. 558 텍스트 윤리검증 데이터
4. 선택: 71314 방송콘텐츠 대화체 음성인식 데이터
5. 선택: 463 방송 콘텐츠 대화체 음성인식 데이터

### 승인 후 내가 바로 실행할 명령
```bash
cd /mnt/c/Users/yhgil/broadcast_fairness_2026
./scripts/download_priority_aihub_data.sh download-core
./scripts/download_priority_aihub_data.sh download-asr-labels
```

## 6. Benchmark 구축 전략 업데이트
- 71557 뉴스 대본을 news benchmark core로 사용.
- 591을 장르 다양성 확장으로 사용.
- 558을 toxic/non-toxic pre-label calibration으로 사용.
- Codex가 실제 방송 segment에 toxic/nontoxic, category, context, span offset을 pre-label.
- Human adjudication으로 locked test label 확정.
- 최종 실험은 RoBERTa base/large의 non-SWA vs SWA 비교.
