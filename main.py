from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class member:
    # __init__ 객체생성 자동 호출 함수
    def __init__(self, name:str, age: int, adrs: str, job: str):
        self.name = name
        self.age = age
        self.adrs = adrs
        self.job = job

    def intr(self):
        return (
            f"안녕하세요. 제 이름은 {self.name}입니다. \n"
            f"현재 나이는 {self.age}세 이고 거주지는 {self.adrs} 이며 \n"
            f"직업은 {self.job} 입니다. 잘 부탁드립니다. \n"
        )

me = member(
    name='홍기현',
    age=33,
    adrs='충청북도 청주시',
    job='웹 퍼블리셔'
)

class Chat:
    def __init__(self, id:str, content:str):
        self.id = id
        self.content = content

chatLog = []

@app.post('/chat/{id}')
def add_chat(id:str, content:str):
    chat = Chat(id, content)
    chatLog.append(chat)
    return '체팅 추가'

@app.get('/chat')
def get_chat():
    return chatLog

@app.get('/me')
def read_intro():
    return {'소개': me.intr()}

members = []

class Memo(BaseModel):
    id:int
    content:str

memos = []

@app.put('/memos/{memo_id}')
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '성공'
    return '동일 아이디 메모 없음'

@app.get('/memos')
def read_memo():
    return memos

@app.post('/memos')
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모 추가'

app.mount('/', StaticFiles(directory='static', html=True), name='static')