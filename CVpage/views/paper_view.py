from flask import Blueprint,render_template,redirect,url_for,render_template,request,send_from_directory
from ..models import Paper
from ..forms import PaperForm
from datetime import datetime
from CVpage import db
from werkzeug.utils import secure_filename
import os
bp=Blueprint('paper',__name__,url_prefix='/paper')

@bp.route('/create/', methods=('POST','GET'))
def create():
    form=PaperForm()
    if request.method == 'POST' and form.validate_on_submit():
        f=request.files['files']
        paper=Paper(subject=form.subject.data, content=form.content.data,create_date=datetime.now())
        if f.filename:
            os.chdir('./CVpage/static/paper/')
            t=str(datetime.now())
            f.save(secure_filename(t+'/'+f.filename))#filename시 확장자명도 같이 들어감
            os.chdir('../../../')
            paper.file_name=t.replace(' ','_').replace(':','')+'_'+f.filename
        db.session.add(paper)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('paper/paper_create.html', form=form)

@bp.route('/detail/<int:paper_id>/')
def detail(paper_id):
    paper=Paper.query.get_or_404(paper_id)
    return render_template('paper/paper_detail.html',paper=paper)

@bp.route('/list/')
def _list():
    paper_list=Paper.query.order_by(Paper.create_date.desc())
    return render_template('/paper/paper_list.html',paper_list=paper_list)

    