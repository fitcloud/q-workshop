# Amazon Q Developer Agent

Amazon Q Developer의 Agent는 IDE 안에서 자연어 대화를 기반으로 "계획-수행-검토"를 자동화해 주는 기능입니다. 단순 설명을 넘어서, 변경 계획을 제안하고, 코드 변경을 적용하며, 경우에 따라 저위험 셸 명령을 실행할 수 있습니다. 작업은 항상 개발자 검토를 거쳐 diff 형태로 확인·취소할 수 있습니다.

이 작업에서는 에이전트의 핵심 개념과 바로 실습 가능한 단계들을 소개합니다.

## Act 1: Amazon Q 채팅 에이전트 활성화
  1. 채팅에 ```/clear``` 명령어를 사용하거나, 상단 탭에서 "+" 버튼을 눌러, 새로운 채팅을 활성화합니다.

    !!! note
        Amazon Q는 활성화된 채팅의 내용을 참고하여 응답을 생성합니다. 컨텍스트 용량 초과 또는 다른 주제에 대한 더 나은 응답을 원하신다면 새 채팅을 활성화 하는 것을 권장드립니다.
    
    ![clear](./images/clear.png)
    <br>
  
  2. 에이전트 기능을 활성화합니다.
    
    ![agent_on](./images/agent_on.png)


## Act 2: 코드 분석 및 수정 요청
  1. Context로 ```sample/sample_python_code.py```를 추가하고, 아래 내용으로 Amazon Q에 요청하여 python 코드를 수정합니다.
    ```
    이 Python 코드를 분석하고, 발견된 취약점을 설명한 뒤, 권장 코드 스타일과 모범 사례에 따라 리팩터링된 코드를 제시하고 변경해주세요.
    ```

    ![agent_request](./images/agent_request.png)
    <br>
  
  2. Amazon Q가 해당 요청에 대해 어떻게 분석하고 응답하는지 확인합니다.

    !!! note
        코드(Context)를 분석하고 수정하는 데 다소 시간이 소요될 수 있습니다.

    ![agent_request1](./images/agent_request1.png)
  
  3. 채팅에서 수정된 코드(파일)을 눌러서 변경 사항을 확인합니다.

    ![agent_request2](./images/agent_request2.png)
    ![agent_request3](./images/agent_request3.png)
  
  4. (선택) 변경 사항을 원치 않으실 경우, 채팅에서 수정된 파일 우측에 "Undo" 버튼을 눌러서 이전 사항으로 되돌릴 수 있습니다.
    ![agent_request4](./images/agent_request4.png)


## Act 3: 문서 생성 요청
  1. Context로 ```sample/sample_python_code.py```를 추가하고, 아래 내용으로 Amazon Q에 요청하여 Readme.md 파일을 생성합니다.

    ```
    이 Python 코드에 대한 Readme.md 파일을 sample 디렉토리에 생성해주세요.
    ```

    ![agent_request5](./images/agent_request5.png)
  
  2. 생성된 응답과 문서 ```Readme.md```를 확인합니다.

    !!! info
        생성되는 모든 응답과 파일, 코드는 모두 다를 수 있습니다.

    ![agent_request6](./images/agent_request6.png)
    ![agent_request7](./images/agent_request7.png)

## 리소스 정리
  왼쪽 사이드바에서 탐색기(Explorer)를 열고 sample 디렉토리를 우클릭하여 삭제합니다.

!!! note
    이 정리 작업은 애플리케이션 구성 과정에서 불필요한 컨텍스트가 포함되지 않도록 하기 위함입니다.

  ![delete](./images/delete.png)

## 요약

이 워크숍 활동에서 다음 항목을 실습했습니다.

  - ✅ Amazon Q 에이전트 코드 변경 및 리팩터링 요청
  - ✅ 변경 사항 비교
  - ✅ 문서 생성 요청

다음 활동에서는 Amazon Q의 Rule 기능을 실습해볼 것입니다.