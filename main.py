# 웹 백엔드 프레임 워크인 fastapi 모듈 불러오기
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory = "templates")

#fastAPI 객체 생성
app=FastAPI()


@app.get("/") #fastAPI 객체에 url w주소 매핑 정의 (예 : https://231.28.13.23:8000/test)
def hello(): 
    return {"message" : "안녕하세요 fastapi 입니다."}


@app.get("/test")
def test(request:Request):
    print(Request)
    return templates.TemplateResponse("test.html",context={"request" : request, ' a':2})


@app.get("/getinfo/{name}/{gener}")
def getinfofn(request:Request, name=str, gender=str):
    print(name,gender)
    return templates.TemplateResponse("test.html",context={"request": request, "name":name , "gender":gender})

@app.get("/teamname/{name1}/{name2}")
def teamname(request: Request, name1=str, name2=str):
    return templates.TemplateResponse("teamname.html",context={"request":request, "name1":name1,"name2":name2})


if __name__ == '__main__':
                #    ip 설정,         port 설정하는 곳       
    uvicorn.run(app, host='localhost',port=5000)