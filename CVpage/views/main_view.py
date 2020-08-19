from flask import Blueprint,render_template,redirect,url_for
bp=Blueprint('main',__name__,url_prefix='/')#(블루프린트 이름, 패키지 이름, 라우트 접미사)

@bp.route('/')
def index():
    return redirect(url_for('paper._list'))