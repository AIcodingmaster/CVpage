from flask import Blueprint,render_template,request
from CVpage.models import Project
bp = Blueprint('detail', __name__, url_prefix='/detail/')

@bp.route('/<int:project_id>')
def detail(project_id):
    p=Project.query.get(project_id)
    bp=Project.query.get(project_id+1)
    np=Project.query.get(project_id-1)
    last_picture=request.args.get('last_picture',None)#key값 p를 찾아보고 없으면 None반환
    if last_picture==None: 
        return render_template('work/work_detail.html',p=p,bp=bp,np=np)
    else:
        return render_template('work/work_detail.html',p=p,bp=bp,np=np,last_picture=last_picture)

@bp.route('/video/<int:project_id>')
def video(project_id):
    p=Project.query.get(project_id)
    return render_template('/video.html',p=p)