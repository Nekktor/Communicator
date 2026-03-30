from Database.methods.init import *
from Database.init import Session
from sqlalchemy.orm import Session


# Sql-запросы у таблице messages
class MessagesRequests:
    def __init__(self, session: Session):
        self.session = session
