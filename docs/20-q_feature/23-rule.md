# Amazon Q Developer Rule

Rule은 Amazon Q Developer가 따라야 할 팀 규칙과 작업 가이드를 자연어로 정의해 일관된 행동을 보장하는 지속 지침입니다. 일회성 프롬프트가 아니라 코드 생성·수정·설명·명령 제안 전반에 걸쳐 우선순위, 금지사항, 산출물 형식 등을 명확히 합니다.

이 작업에서는 Amazon Q Developer의 Rules 사용법과 실제 애플리케이션 구성에 적용할 Rule을 작성합니다.

## Act 1: Rule 이해하기
  1. Rule을 적용하면 얻는 이점

    - 일관성: 팀의 코드 스타일·디렉토리 규칙·품질 기준을 자동으로 준수합니다.
    - 비용 절감: 매 대화마다 같은 제약을 반복 설명할 필요가 줄어듭니다.
    - 안전성: 민감 작업/명령 제한, 보안·컴플라이언스 가이드라인을 내재화합니다.
    - 생산성: 비기능 요구사항을 고정해 재작업과 핑퐁을 최소화합니다.
    - 온보딩: 신입/게스트가 규칙을 통해 빠르게 팀 표준을 학습합니다.

    !!! note
        Rule은 Context와 마찬가지로 Input Token에 영향을 주며, 너무 많은 Rule은 비효율적일 수 있습니다.
    <br>
  
  2. 좋은 Rule 작성 가이드

    - 200줄 이하로 유지합니다
    - 범위와 금지사항을 명시합니다(생성 위치, 수정 금지 영역, 파일 길이 제한 등).
    - 품질 기준을 정의합니다(스타일 가이드, 테스트/로그/예외 처리 원칙).
    - 산출물 형식을 고정합니다(코드·설명 분리, 언어, 표기 규칙 등).
    - 의사결정 기준을 밝힙니다(단순성 우선, 중복 회피, 기존 구현 재사용).
    - 불확실성 처리 원칙을 추가합니다(모호하면 질문하고 확정 후 진행).

## Act 2: AI Image Gallery 프로젝트에 대한 Rule 추가
  1. 채팅 입력 칸 우측에 "Rules" 버튼을 누르고, "Create a new rule"을 누릅니다.
    ![create_rule1](./images/create_rule1.png)
    <br>

  2. Rule name 을 ```project_rule```로 설정하고 "Create" 버튼을 누릅니다.
    ![create_rule2](./images/create_rule2.png)
    <br>

  3. IDE에서 ```.amazonq/rules/project_rule.md``` 파일이 열린 것을 확인하고, 해당 파일에 아래 규칙을 추가(작성)합니다.
    ```markdown
    당신은 **AWS와 Python 전문가**입니다.
    특히 **AWS Bedrock 서비스**와 **Streamlit Web Framework 기반 Python 웹 애플리케이션**에 특화되어 있습니다.
    모든 작업은 **최신 AWS 및 Python 모범 사례**를 준수하며 진행하세요.

    ---

    ### 기본 규칙

    * **코드 위치:** 모든 코드는 `src/` 디렉토리에, 문서는 `docs/` 디렉토리에 생성합니다.
    * **패키지 관리:** `pip` 대신 **uv**를 사용하여 패키지를 관리합니다.
    * **코드 품질:**

      * 간단하고 직관적인 솔루션을 우선합니다.
      * 코드 중복을 피하고, 기존 코드와의 일관성을 확인합니다.
      * 파일은 200~300줄 이내로 유지하며, 초과 시 리팩터링합니다.
      * **PEP8 스타일 가이드**를 준수하고, 주요 로직에는 간단한 주석을 추가합니다.
    * **작업 범위:** 요청된 변경 사항만 반영하며, 불확실하거나 모호한 부분은 반드시 질문 후 진행합니다.
    * **출력 형식:** 코드 / 문서 / 설명은 구분해 작성하고, 필요 시 간단한 테스트 코드나 실행 예시를 포함합니다.
    * **유지보수성:** 모듈화, 함수 분리, 의미 있는 네이밍으로 확장성을 고려하고 코드베이스를 깔끔하게 유지합니다.
    ```

    ![create_rule3](./images/create_rule3.png)
    <br>

  4. Rule이 정상적으로 적용됬는지 확인하기 위해 채팅에 아래 내용을 질문합니다.
    ```
    당신이 할당받은 역할과 프로젝트 규칙을 설명하세요.
    ```

    !!! warning
        "Active file" Context를 제거하고 진행해주세요.
    
    ![create_rule4](./images/create_rule4.png)
    <br>
    
  5. Amazon Q가 자동으로 Context가 추가하는지 확인하고, 해당 질문에 대해 어떻게 응답하는지 확인합니다

    ![create_rule5](./images/create_rule5.png)


## Tips
  1. 아래 AWS 문서를 참고하여 다른 프로젝트에도 적용 가능한 Rule을 만들 수 있습니다.
  [Mastering Amazon Q Developer with Rules](https://aws.amazon.com/blogs/devops/mastering-amazon-q-developer-with-rules/)
  <br>

  2. 또는 다른 커뮤니티 혹은 사용자가 만든 Rule을 가져오거나 참고하여 사용할 수 있습니다.
  [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules?tab=readme-ov-file)
  [cursor.directory](https://cursor.directory/rules)

## 요약

  이 워크숍 활동에서 다음 항목을 실습했습니다.

  - ✅ Amazon Q Rule 이해
  - ✅ Amazon Q Rule 적용

  다음 활동에서는 Amazon Q의 MCP 기능을 실습해볼 것입니다.
