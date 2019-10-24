from database_singleton import Singleton
from project import create_app
from Flask import current_app

db = Singleton().database_connection()

class Report(db.Model):
    __tablename__ = 'REPORT'
