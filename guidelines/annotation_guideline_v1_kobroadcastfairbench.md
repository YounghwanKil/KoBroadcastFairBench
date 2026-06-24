# KoBroadcastFairBench Annotation Guideline v1

## 0. 목표
한국어 방송 대본에서 특정 집단에 대한 차별, 고정관념, 혐오·비하, 불공정한 framing을 문맥 기반으로 판정한다. 단순 욕설/키워드 검출이 아니라, 방송심의 관점에서 차별 조장 가능성과 보도 맥락의 정당성을 함께 평가한다.

## 1. Annotator output fields
각 sample에 대해 다음을 작성한다.

- `bias_categories`: 하나 이상. 해당 없으면 `no_bias`.
- `context_types`: 하나 이상. 해당 없으면 `non_discriminatory_context` 또는 `unclear`.
- `protected_attributes_mentioned`: 언급된 보호속성/집단.
- `risk_spans`: 문제 또는 판단 근거가 되는 span.
- `severity`: 0~3.
- `direct_harm_or_reported_context`: `direct_harm`, `reported_context`, `no_issue`, `unclear`.
- `human_rationale`: 한국어 근거 1~3문장.
- `human_revision`: 필요 시 사실 보존형 수정문.

## 2. Severity
- 0: 차별/편견 문제 없음. 맥락상 정당한 언급.
- 1: 약한 고정관념 또는 불명확한 표현. 주의/검토 필요.
- 2: 명확한 차별·비하·집단 일반화. 수정 권고.
- 3: 혐오·비인간화·배제 선동·심각한 조롱. 반드시 수정/인간 검토.

## 3. Bias categories
`taxonomy_v1_kobroadcastfairbench.md`의 10개 bias category를 사용한다.

## 4. Context 판정 규칙

### 4.1 Explicit Discrimination
특정 집단을 직접적으로 열등, 위험, 배제 대상, 비정상으로 표현한다.

### 4.2 Implicit Stereotype
직접 비하어는 없지만 집단의 역할·능력·성격을 고정한다. 예: “여성은 감정적이라…”, “노인은 기술을 못 다룬다”.

### 4.3 Overgeneralization
일부 사건/사례를 집단 전체로 일반화한다. “모두”, “대부분”, “원래”, “항상” 등의 단서에 주의한다.

### 4.4 Derogatory Expression
멸칭, 조롱, 혐오 단어, 비인간화 표현을 포함한다.

### 4.5 Humor/Sarcasm with Bias
예능·농담·풍자 형식이어도 특정 집단에 대한 비하나 고정관념을 강화하면 label한다.

### 4.6 Non-discriminatory Context
정책, 통계, 피해구제, 보도 맥락에서 보호속성 언급이 필요하고 표현이 중립적이면 문제 없음.

### 4.7 Quoted/Critical Mention
차별 표현이 등장하더라도, 그것이 명확히 인용·비판·보도 목적이고 방송사가 문제 표현을 강화하지 않으면 직접 위해 표현으로 보지 않는다. 단, 과도한 반복·자극적 재현·맥락 부족이면 severity를 올릴 수 있다.

## 5. 방송 대본 특수 규칙
- 앵커 멘트, 리포트 본문, 인터뷰 인용, 자막/그래픽 설명을 구분한다.
- 인터뷰이 발언이라도 편집·전달 방식이 차별을 강화하면 방송 책임 관점에서 별도 기록한다.
- 영상/그래픽 정보가 필요한 경우 `unclear`로 표시하고 human review를 남긴다.
- 예능/풍자 표현은 의도보다 수용자에게 미치는 차별 조장 가능성을 함께 본다.

## 6. Counterfactual annotation
가능하면 보호속성 swap pair를 만든다.
- 성별: 남성↔여성 등
- 연령: 청년↔노인 등
- 지역: 특정 지역↔다른 지역
- 국적/민족: 특정 국적↔다른 국적
단, 역사적/정책적 맥락이 깨지는 swap은 만들지 않는다.

## 7. Reject/hold cases
- 원문만으로 맥락 판단 불가: `unclear`.
- 영상/표정/자막/그래픽이 핵심: `unclear` + note.
- 명예훼손·개인정보 등 법적 위험: raw 공개 금지, 내부 검토.
