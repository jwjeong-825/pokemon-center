# 주원이의 포켓몬센터

FastAPI와 SQLite를 이용해 만든 포켓몬센터 웹 프로젝트입니다.

포켓몬을 PC에 맡기고 조회하거나 다시 데리고 갈 수 있으며,
간호사 기능을 통해 포켓몬을 치료할 수 있습니다.

---

## 사용 기술

- Python
- FastAPI
- SQLite
- HTML / CSS / JavaScript
- Git / GitHub

---

## 주요 기능

### 포켓몬 PC 기능

- 포켓몬 맡기기
- 포켓몬 목록 조회
- 포켓몬 데리고 가기

### 간호사 기능

- 포켓몬 치료 기능

---

## 프로젝트 실행 방법

### 1. 가상환경 활성화

```bash
source venv/bin/activate
```

### 2. 서버 실행

```bash
python3 -m uvicorn app.main:app --reload
```

### 3. 접속

```text
http://127.0.0.1:8000
```

---

## 프로젝트 구조

```text
pokemon-center
│
├── app
│   ├── main.py
│   ├── computer.py
│   ├── nurse.py
│   ├── database.py
│   │
│   ├── templates
│   │   └── index.html
│   │
│   └── static
│       ├── style.css
│       └── pokemon-center-ui.png
│
├── pokemon.db
├── requirements.txt
└── README.md
```

---

## 배운 점

- FastAPI 라우터 구조 이해
- SQLite 데이터 저장 및 삭제
- JavaScript fetch API 사용
- HTML/CSS 기반 UI 구성
- GitHub 프로젝트 관리 경험
- 게임 UI 스타일 웹페이지 구현 경험
