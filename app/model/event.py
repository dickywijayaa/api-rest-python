from app import db
from datetime import datetime
from app.model.user import Users

class Events(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    event = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))

    def __repr__(self):
        return '<Event {}>'.format(self.todo)
