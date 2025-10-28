# AWS AI Image Gallery 구현 가이드

## 1. 요구사항

### 기능 요구사항
- 텍스트 프롬프트를 통한 AI 이미지 생성 (Amazon Nova Canvas 사용)
- 생성된 이미지를 Amazon S3 버킷에 자동 저장
- 저장된 이미지를 갤러리 형태로 웹에서 조회
- 이미지 생성과 갤러리를 동일 화면에서 동시 표시

### 기술 요구사항
- Python Streamlit 프레임워크 기반 웹 애플리케이션
- Amazon Bedrock의 Nova Canvas 모델 (us-east-1 리전)
- Amazon S3를 이미지 저장소로 활용
- 환경변수를 통한 S3 버킷 설정

## 2. 기술 스택

### 백엔드
- **Python 3.9+**: 메인 개발 언어
- **Streamlit**: 웹 프레임워크
- **boto3**: AWS SDK for Python
- **Pillow**: 이미지 처리 라이브러리

### AWS 서비스
- **Amazon Bedrock**: Nova Canvas 모델 호출 (us-east-1)
- **Amazon S3**: 이미지 저장 및 관리

### 패키지 관리
- **uv**: Python 패키지 관리자

## 3. 구현 단계

### 1단계: 프로젝트 초기 설정
- 프로젝트 디렉토리 구조 생성 (`src/`, `docs/`)
- `pyproject.toml` 파일 생성 및 의존성 정의
- `main.py` 파일 생성 (서버 실행 진입점)
- 환경변수 설정 파일 준비

**필요한 의존성:**
```toml
dependencies = [
    "streamlit>=1.28.0",
    "boto3>=1.34.0",
    "pillow>=10.0.0",
    "python-dotenv>=1.0.0"
]
```

### 2단계: AWS 서비스 연동 모듈 개발
- Bedrock 클라이언트 설정 (us-east-1 리전)
- Nova Canvas 모델 호출 함수 구현
- S3 클라이언트 설정 및 이미지 업로드 함수 구현
- 환경변수 처리 로직 구현

**환경변수:**
- `S3_BUCKET_NAME`: S3 버킷 이름
- `S3_REGION`: S3 버킷 리전

### 3단계: 이미지 생성 기능 구현
- Streamlit UI 컴포넌트 구성 (텍스트 입력, 생성 버튼)
- Nova Canvas API 요청 구조 구현
- Base64 이미지 디코딩 및 처리
- 생성된 이미지 S3 업로드 로직

**Nova Canvas 요청 구조:**
```json
{
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": "사용자 프롬프트"
    },
    "imageGenerationConfig": {
        "width": 1024,
        "height": 1024,
        "quality": "standard",
        "numberOfImages": 1
    }
}
```

### 4단계: 갤러리 기능 구현
- S3 버킷에서 이미지 목록 조회 함수
- Streamlit 컬럼 레이아웃을 활용한 갤러리 UI
- 이미지 썸네일 표시 및 클릭 시 확대 기능
- 페이지네이션 또는 무한 스크롤 구현

### 5단계: 메인 애플리케이션 통합
- `src/app.py` 메인 애플리케이션 파일 구현
- 이미지 생성과 갤러리를 동일 화면에 배치
- 실시간 갤러리 업데이트 로직
- 에러 처리 및 사용자 피드백 구현

## 실행 방법

### 환경 설정
1. 프로젝트 루트에 `.env` 파일 생성:
```
S3_BUCKET_NAME=your-bucket-name
S3_REGION=your-bucket-region
```

2. AWS 자격 증명 설정 (AWS CLI 또는 IAM 역할)

### 서버 실행
```bash
# 프로젝트 루트에서 실행
uv run main.py
```

### 필요한 AWS 권한
- `bedrock:InvokeModel` (Nova Canvas 모델 호출)
- `s3:PutObject`, `s3:GetObject`, `s3:ListObjects` (S3 버킷 접근)

## 파일 구조
```
develop/
├── src/
│   ├── app.py              # 메인 Streamlit 애플리케이션
│   ├── aws_services.py     # AWS 서비스 연동 모듈
│   └── utils.py           # 유틸리티 함수
├── docs/
│   └── implement_guide.md  # 구현 가이드 (본 문서)
├── main.py                # 서버 실행 진입점
├── pyproject.toml         # 프로젝트 설정 및 의존성
└── .env                   # 환경변수 설정
```