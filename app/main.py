from fastapi import FastAPI
from database import create_table
from computer import router as computer_router
from nurse import router as nurse_router

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Welcome to Juwon's Pokemon Center"}


# 컴퓨터 기능 연결
app.include_router(computer_router)

# 간호사 기능 연결
app.include_router(nurse_router)
