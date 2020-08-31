from flask import Blueprint,redirect,url_for,session,g
bp = Blueprint('main', __name__, url_prefix='/')

@bp.before_app_request
def load_logged_in_user():
    pw= session.get('pw')
    if pw is 123:
        g.user = "admin"

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('about.about'))

@bp.route('/admin/<int:pw>')
def admin(pw):
    if pw==123:
        session.clear()
        session['pw']=123
        return redirect(url_for('about.about'))
    else:
        return redirect(url_for('about.about'))

@bp.route('/')
def index():
    return redirect(url_for('about.about'))