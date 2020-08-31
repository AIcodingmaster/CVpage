from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    projectName = StringField('프로젝트이름', validators=[DataRequired()])
    projectType = StringField('타입', validators=[DataRequired()])
    pictureName = StringField('video, pic이름', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    gitAddress = StringField('git주소', validators=[DataRequired()])
