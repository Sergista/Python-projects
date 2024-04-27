from app import db



class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)  # datetime -> datetime, date, time

    def __repr__(self):
        return f"<Member: {self.username}>"

