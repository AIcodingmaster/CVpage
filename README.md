# CVpage with flask
이 페이지는 제 CV Page 제작을 위한 git입니다.
페이지 제작에 있어 기억이 나지 않았던 상황들으 적었습니다.

1. flask run시 패키지의 상위 dir에 위치해서 flask run 명령어를 수행해야 패키지를 찾음.
2. flask Migrate 설치 후 flask SQL Alqemy, Migrate 객체 생성 후 init하면 flask db init를 수행 가능, 수행 후 migrations 폴더가 생성됨.
3. import시 최상위 패키지 밖에서 접근하는 것(최상위 패키지를 ..으로 나가서 접근)은 불가능함.
4. db.Column의 속성은 전부 대문자(db.Integer, db.String)
5. config파일과 migrations 폴더는 CVpage패키지와 동일한 level의 dir에 존재함.
6. from datetime import datetime 후 datetime.now()시 db.DateTime에 대입 가능
7. 템플릿 상속시 {%extends 'base.html'%}을 쓰고 base.html에 block명을 정한 후 그 이름을 사용해야 함.
8. 라우트에서 url을 통해 데이터를 받을 시 파라미터로 그 변수 명을 써주어야 함. def Question(question_id)이런 식
9. static을 추가 하기 위해 base.html에 <link rel="stlysheet" href="{{url_for('static',filename='style.css')}}">이런식으로 추가한다.
10. 특정 파일로 들어가는 링크는 <a href="{{url_for('static',filename='static내경로/파일이름)}}">으로 쓰면 된다.(단 맨처음 / 은 쓰지않음)
11. Flask Form을 만들기 위해서는
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
```
를 추가해야 함. 그리고 사용을 위해서는 config.py에 SECRET_KEY = "string"을 입력해야 한다.
또한 validation체크를 하고 싶은 경우  {{ form.csrf_token }}을 html에 삽입 후
if request.method is 'POST' and form.validate_on_submit(): 조건을 라우트 함수 내부에 걸면 된다.
12. Form의 속성 생성시
content = TextAreaField('라벨이름', validators=[DataRequired()])과 같은 형태를 띈다.
필수값이면서 이메일이어야 하면 validators=[DataRequired(), Email()] 과 같이 사용

13. config파일의 경우 패키지 상위 디렉토리에 있어도 바로 import로 접근이 가능

14. 라우트에서 POST, GET방식의 경우 methods=튜플 로 들어간다.