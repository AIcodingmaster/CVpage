from flask import Blueprint,render_template,url_for,session,g,redirect,request
from werkzeug.utils import secure_filename
from CVpage.models import Project,db
from CVpage.form import ProjectForm
from datetime import datetime
import os
bp = Blueprint('about', __name__, url_prefix='/about/')

@bp.route('/')
def about():
    work_list=Project.query.order_by(Project.create_date.desc())
    return render_template('about/about.html',w_list=work_list)
@bp.route('/add/',methods=('GET','POST'))
def add():
    form=ProjectForm()
    if request.method =="POST" and form.validate_on_submit():
        p=Project(projectName=form.projectName.data,
        projectType=form.projectType.data,
        pictureName=form.pictureName.data,
        content=form.content.data,
        gitAddress=form.content.data,
        create_date=datetime.now())
        pic1=request.files['pic1']
        pic2=request.files['pic2']
        video=request.files['video']
        pictureName=form.pictureName.data
        pic1.save('/home/ubuntu/projects/CVpage/CVpage/static/img/'+secure_filename(pictureName+'1.jpg'))
        pic2.save('/home/ubuntu/projects/CVpage/CVpage/static/img/'+secure_filename(pictureName+'2.jpg'))
        video.save('/home/ubuntu/projects/CVpage/CVpage/static/video/'+secure_filename(pictureName+'.mp4'))
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('about.about'))
    else:
        return render_template('project_form.html', form=form)

@bp.route('/delete/<int:project_id>')
def delete(project_id):
    p=Project.query.get(project_id)
    if g.user is "admin":
        db.session.delete(p)
        db.session.commit()
    return redirect(url_for('about.about'))

@bp.route('/modify/<int:project_id>', methods=('GET','POST'))
def modify(project_id):
    p=Project.query.get(project_id)
    if request.method =="POST":#작성을 하고 form태그의 post요청으로 들어간 것
        form = ProjectForm()
        bpicN=p.pictureName
        if  g.user is "admin" and form.validate_on_submit():
            pic1=request.files['pic1']
            pic2=request.files['pic2']
            video=request.files['video']
            form.populate_obj(p)
            if pic1 is None or pic2 is None or video is None:
                return render_template('project_form.html', form=form)
            os.remove('/home/ubuntu/projects/CVpage/CVpage/static/img/'+secure_filename(bpicN+'1.jpg'))
            os.remove('/home/ubuntu/projects/CVpage/CVpage/static/img/'+secure_filename(bpicN+'2.jpg'))
            os.remove('/home/ubuntu/projects/CVpage/CVpage/static/video/'+secure_filename(bpicN+'.mp4'))
            pic1.save('/home/ubuntu/projects/CVpage/CVpage/static/img/'+secure_filename(pictureName+'1.jpg'))
            pic2.save('/home/ubuntu/projects/CVpage/CVpage/static/img/'+secure_filename(pictureName+'2.jpg'))
            video.save('/home/ubuntu/projects/CVpage/CVpage/static/video/'+secure_filename(pictureName+'.mp4'))
            db.session.commit()
            return redirect(url_for('about.about'))
    else:#다른 html에서 접근한 것(GET요청일 경우)
        form = ProjectForm(obj=p)#기존 데이터를 대입시켜서 리턴
    return render_template('project_form.html', form=form)

@bp.route('/admin/<int:pw>')
def admin(pw):
    if pw==123:
        session.clear()
        session['pw']=123
        return redirect(url_for('about.about'))
    else:
        return redirect(url_for('about.about'))