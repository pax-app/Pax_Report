from database import db
from project import create_app
from Flask import current_app


class Report(db.Model):
    __tablename__ = 'REPORT'
