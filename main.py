# 웹 백엔드 프레임 워크인 fastapi 모듈 불러오기
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated
import uvicorn
from sqlalchemy import create_engine 


                            #sql종류://아이디:비번@아이피:포트/스키마 이름
db_connection = create_engine("mysql://root:1234@127.0.0.1:3306/test")



'''
        # 커넥터를 통해 실행하겠다 (쿼리를)
query = db_connection.execute("select * from player")

            # 퀴리 날려서 그 결과를 result 변수에 받아옴
result = query.fetchall()

for data in result:
    print("======================================================")
    print(data)
'''



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

# 화면 입락창부터 들어가야 됨
@app.get("/test_get")
def test_get(request:Request):
    return templates.TemplateResponse("post_test.html",context={"request":request})

#받는놈
@app.post("/test_post")
def test_post(name:Annotated[str,Form()], pwd: Annotated[int, Form()]):
    print(name,pwd)

@app.get("/mysqltest")
def db_get(request:Request):  #request 인자로 받는 이유 : 
    query = db_connection.execute("select * from player")
    result_db = query.fetchall()

    # 받아온 정보를 정제해서 리스트에 담을 것
    result = []
    for data in result_db:
        temp = {'player_id':data[0],'player_name':data[1]}
        result.append(temp)
    ## result [{선수id, 선수이름},{선수id, 선수이름},{선수id, 선수이름}...]

                                                     # 페이지를 jinja2로 랜더링할 때 서버 정보가 필요하다.
                                                     # 그래서 request에는 서버에 대한 상태 정보들이 저장되어 있어서 프론트로 던진다.
    return templates.TemplateResponse("sqltest.html",context={'request':request, 'result_table':result})


if __name__ == '__main__':
                #    ip 설정,         port 설정하는 곳       
    uvicorn.run(app, host='localhost',port=5000)