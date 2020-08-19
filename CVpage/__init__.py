from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from datetime import datetime
db=SQLAlchemy()#db 생성
migrate=Migrate()#Migrate 생성

def create_app():
    app=Flask(__name__)#name은 이 패키지 이름을 의미함(CVpage)

    #-- config(db 환경변수)를 app로 끌어들임 --#
    app.config.from_object(config)
    
    #-- ORM(SQLAlchemy, Migrate시작)--#
    db.init_app(app)
    migrate.init_app(app, db)

    #-- 모델 추가 --#
    from . import models #migrate 객체가 우리 모델을 참조 할 수 있도록

    #--블루프린트 추가--#
    from .views import main_view,paper_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(paper_view.bp)
    #--app 가동--#
    return app

