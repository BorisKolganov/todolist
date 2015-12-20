from app import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    importance = db.Column(db.Enum('so-so', 'important', 'very important', name='importance_type'))
    done = db.Column(db.Boolean)
    expired = db.Column(db.TIMESTAMP)
    def __init__(self, body, importance, done, expired):
        self.body = body
        self.importance = importance
        self.done = done
        self.expired = expired

    def trig(self):
        self.done = not self.done
        return self

    def serialize(self):
        return {
            "id": self.id,
            "body": self.body,
            "importance": self.importance,
            "done": self.done,
            "expired": self.expired
        }
