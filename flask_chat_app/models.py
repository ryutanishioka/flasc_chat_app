from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # SQLAlchemyのインスタンスを作成

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):  # __repr__ メソッドは2つのアンダースコアを持つ必要があります
        return f'<Message {self.id}: {self.content}>'
