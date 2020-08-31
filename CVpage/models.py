from CVpage import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectName = db.Column(db.String(200), nullable=False)
    projectType = db.Column(db.String(200), nullable=False)
    pictureName = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    gitAddress = db.Column(db.String(200), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)