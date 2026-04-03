from Database.init import Base
from sqlalchemy import Column, String, Integer, Text, text
from sqlalchemy.orm import relationship
import sqlalchemy as sql


# Таблица users
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    lastname = Column(String(60))
    birthday = Column(String(10))
    avatar_url = Column(Text)
    date_created = Column(String(10), nullable=False, server_default=text("to_char(current_date, 'DD-MM-YYYY')"))
    last_time_online = Column(String(16), nullable=False, server_default=sql.text("to_char(current_timestamp, 'DD-MM-YYYY HH24:MI')"))
    phone = Column(String(20), unique=True)
    email = Column(String(254), unique=True)

    participants = relationship("Participants", back_populates="user", cascade="all, delete-orphan")
    chats = relationship("Chats", secondary="participants", back_populates="users", overlaps="participants")
    messages = relationship("Messages", back_populates="sender")

    # def __repr__(self):
    #     return f'{self.id, self.name, self.username, self.lastname, self.birthday, self.avatar_url, self.date_created, self.last_time_online, self.phone, self.email}'