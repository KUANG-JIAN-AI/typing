from datetime import datetime
from .. import db

class Users(db.Model):
    __tablename__ = "typ_users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Integer, default=lambda: int(datetime.now().timestamp()), nullable=False)
    updated_at = db.Column(db.Integer, default=lambda: int(datetime.now().timestamp()), onupdate=lambda: int(datetime.now().timestamp()), nullable=False)
    deleted_at = db.Column(db.Integer, nullable=True)
    

    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "created_at": datetime.fromtimestamp(self.created_at).strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None,
            "updated_at": datetime.fromtimestamp(self.updated_at).strftime("%Y-%m-%d") if self.updated_at else None
        }

    def __repr__(self):
        return f'<Users {self.id}>'
