from CVpage import db

class PaperImage(db.Model): #이미지 이름을 저장할 모델
    id=db.Column(db.Integer,primary_key=True)
    subject=db.Column(db.String(200),nullable=False)
    paper_id=db.Column(db.Integer,db.ForeignKey('paper.id',ondelete='CASCADE'))
    paper=db.relationship('Paper',backref=db.backref('image_set'))


class Paper(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String(200),nullable=False)
    content=db.Column(db.Text(), nullable=False)#paper 요약을 보여줄 db
    file_name=db.Column(db.String(200),nullable=False)#paper pdf 파일 이름 'id+_+file_name'으로 실제 파일 저장
    create_date=db.Column(db.DateTime(), nullable=False)#생성 시간
