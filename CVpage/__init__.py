from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    from .views import workdetail_view,main_view,about_view
    #db 설정 등록
    app.config.from_object(config)
    #ORM(db 코드 추상화) 등록
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    #블루 프린트 등록
    app.register_blueprint(workdetail_view.bp)
    app.register_blueprint(main_view.bp)
    app.register_blueprint(about_view.bp)
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    return app