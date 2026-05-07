from fastapi import FastAPI
from app.database import create_table
from app.computer import router as computer_router
from app.nurse import router as nurse_router

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Welcome to Juwon's Pokemon Center"}


# 컴퓨터 기능 연결
app.include_router(computer_router)

# 간호사 기능 연결
app.include_router(nurse_router)
