# Juwon's Pokemon Center

FastAPI와 SQLite를 사용한 포켓몬센터 백엔드 프로젝트입니다.

## Features

- 포켓몬 맡기기
- 포켓몬 조회
- 포켓몬 데려가기
- 간호사 치료 기능

## Tech Stack

- Python
- FastAPI
- SQLite
- GitHub

## Run

```bash
uvicorn main:app --reload
```

## API

### Pokemon Computer

- POST /pokemon
- GET /pokemon
- GET /pokemon/{pokemon_id}
- DELETE /pokemon/name/{name}

### Nurse

- POST /nurse/heal
