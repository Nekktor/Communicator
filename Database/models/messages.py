from Database.init import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum
from enum import Enum


# Выбор данных для типа сообщения
class MessageTypeEnum(Enum):
    text = "text"
    image = "file"


# Таблица messages
class Messages(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    type = Column(SQLEnum(MessageTypeEnum), default=MessageTypeEnum.text, nullable=False)
    text = Column(Text)
    file_id = Column(Integer)
    creation_date_time = Column(DateTime, server_default=func.now())
    chat_id = Column(Integer, ForeignKey('chats.id', ondelete='CASCADE'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)

    chat = relationship("Chats", back_populates="messages")
    sender = relationship("Users", back_populates="messages")
