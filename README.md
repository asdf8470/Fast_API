# Fast_API
 메인 코드는 main.py<br>
 html 코드는 templates 폴더 test.html에 있뜸

## 기본구조


## SQLAlchemy, SQLClient
* SQLAlchemy -> 파이썬 main.py 에서 mySQL 언어로 변환시켜주는 프포그램 <br>
* SQLclient -> 변환된 언어 mySQL에 연결시켜주는 connector

## GPT 명령어 주는법
```<html>
    <head>
        <!-- 홈페이지의 상태, 외부파일 import, 탭 이름 등 페이지에 대한 속성을 정의하는 곳-->
        <tittle1 style = 'color : rgb(0, 0, 0)'> 1조 팀원 2명 </tittle1>
    </head>
    
    <body>
        <h1 style = 'color : rgb(0, 0, 255)'> 팀원 1 :{{name1}} </h1>
        <h1 style = 'color : rgb(255, 0, 0)'> 팀원 1 :{{name2}} </h3>    
    </body>
</html>
이게 지금 내 웹 화면 코드야, 이건 이름 2개를 화면에 띄우는 코드야, 
화면 위쪽에 공지사항, 게시판, QnA 헤더를 배치해 주고 그 아래에 백그라운드 컬러가 하얀색이고 테두리가 빨간색인 박스 안에 이름 두 개를 배치하는 html 코드 짜줘
```

## 명령어 잘못 나올 때
```<!DOCTYPE html>
<html>

<head>
    <!-- 홈페이지의 상태, 외부 파일 import, 탭 이름 등 페이지에 대한 속성을 정의하는 곳-->
    <title>팀 정보</title>
    <style>
        body {
            background-color: #ffffff; /* 하얀색 배경 */
            margin: 0; /* 페이지 여백 없애기 */
        }

        .header {
            background-color: #ff0000; /* 빨간색 헤더 배경 */
            padding: 10px; /* 헤더 안 여백 */
            text-align: center;
            color: #ffffff; /* 헤더 텍스트 색상 */
        }

        .container {
            border: 2px solid #ff0000; /* 빨간색 테두리 */
            padding: 20px; /* 박스 안 여백 */
            margin: 20px; /* 박스 간 여백 */
            text-align: center;
        }

        h1 {
            margin: 10px 0; /* 팀원 이름 간 여백 */
        }
    </style>
</head>

<body>
    <div class="header">
        <h1>공지사항</h1>
        <!-- 다른 헤더 항목들도 추가할 수 있음 -->
    </div>

    <div class="container">
        <h1 style='color: rgb(0, 0, 255);'>팀원 1: {{name1}}</h1>
        <h1 style='color: rgb(255, 0, 0);'>팀원 2: {{name2}}</h1>
    </div>
</body>

</html>
헤더 부분 빨간색 말로 회색으로 바꿔주고 공지사항, 게시판, QnA 는 검은색 글씨로 설정해줘
```
