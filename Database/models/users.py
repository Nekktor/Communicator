from Database.init import Base
from sqlalchemy import Column, String, Integer, Date, Text, DateTime, func, text
from sqlalchemy.orm import relationship


# Таблица users
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    lastname = Column(String(60))
    birthday = Column(Date)
    avatar_url = Column(Text)
    date_created = Column(Date, server_default=func.current_date())
    last_time_online = Column(DateTime, server_default=text("date_trunc('minute', CURRENT_TIMESTAMP)"))  #  Если postgresql
    # last_time_online = Column(DateTime, server_default=text("datetime(strftime('%Y-%m-%d %H:%M:00', 'now'))"))  # Если не postgresql
    phone = Column(String(20), unique=True)
    email = Column(String(254), unique=True)

    participants = relationship("Participants", back_populates="user", cascade="all, delete-orphan")
    chats = relationship("Chats", secondary="participants", back_populates="users", overlaps="participants")
    messages = relationship("Messages", back_populates="sender")

    # def __repr__(self):
    #     return f'{self.id, self.name, self.username, self.lastname, self.birthday, self.avatar_url, self.date_created, self.last_time_online, self.phone, self.email}'