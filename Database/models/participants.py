from Database.init import Base
from sqlalchemy import Column, Integer, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum
from enum import Enum


# Выбор данных для роли участника чата
class UserRoleEnum(Enum):
    member = "Участник"
    pre_admin = "Пре-админ"
    admin = "Админ"


# Таблица chats
class Participants(Base):
    __tablename__ = 'participants'
    # composite PK ensures uniqueness: a user can be in a chat only once
    chat_id = Column(Integer, ForeignKey('chats.id', ondelete='CASCADE'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    joined_at = Column(Date, server_default=func.current_date())
    role = Column(SQLEnum(UserRoleEnum), default=UserRoleEnum.member)

    chat = relationship("Chats", back_populates="participants", overlaps="users,chats")
    user = relationship("Users", back_populates="participants", overlaps="users,chats")
