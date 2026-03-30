from Database.methods.init import *
from Database.init import Session
from sqlalchemy.orm import Session


# Sql-запросы у таблице chats
class ParticipantsRequests:
    def __init__(self, session: Session):
        self.session = session
