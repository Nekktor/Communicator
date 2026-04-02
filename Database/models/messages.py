from Database.init import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum
import sqlalchemy as sql


# Выбор данных для типа сообщения
allowedListMessageTypes = ("text", "file", "image", "video")


# Таблица messages
class Messages(Base):
    __tablename__ = 'messages'
    __table_args__ = (CheckConstraint(
        f"type IN {allowedListMessageTypes}", name="allowed list of types message"),)  # Для колонки type

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, default="text")
    text = Column(Text)
    file_id = Column(Integer)
    creation_date_time = Column(String(16), nullable=False, server_default=sql.text("to_char(current_timestamp, 'DD-MM-YYYY HH24:MI')"))
    chat_id = Column(Integer, ForeignKey('chats.id', ondelete='CASCADE'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)

    chat = relationship("Chats", back_populates="messages")
    sender = relationship("Users", back_populates="messages")
