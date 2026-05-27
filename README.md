# 👨‍💻 Streamlit 자기소개 페이지

Streamlit으로 만든 개인 포트폴리오 / 자기소개 페이지입니다.

## 🚀 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 앱 실행
streamlit run app.py
```

브라우저에서 http://localhost:8501 접속

## 📁 프로젝트 구조

```
streamlit-test/
├── app.py                  # 메인 앱
├── requirements.txt        # 의존성
├── .streamlit/
│   └── config.toml         # Streamlit 테마 설정
└── README.md
```

## 🗂 페이지 구성

| 메뉴 | 내용 |
|------|------|
| 🏠 홈 | 프로필 카드, 요약 지표, 자기소개 |
| 💼 경력 | 경력 타임라인, 학력, 자격증 |
| 🛠 기술스택 | 기술 숙련도 바, 뱃지 |
| 🎯 프로젝트 | 주요 프로젝트 카드 |
| 📬 연락처 | 문의 폼, 연락 정보 |
