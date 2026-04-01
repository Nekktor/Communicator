"""
Файл основного кода
"""

from Database.main import Session, DataBase
from Database.models.participants import UserRoleEnum
from Database.models.messages import MessageTypeEnum
from datetime import date


def health_check_users(db):
    def views():
        print('-' * 150)

        users = db.users.select_all()
        for u in users:
            print(u.id, u.name, u.username, u.lastname, u.birthday, u.avatar_url,
                  u.date_created, u.last_time_online, u.phone, u.email, u.participants, u.chats, u.messages)

        print('-' * 150)

    views()

    # db.users.add(name='Никита', username='Nikita', lastname='Соколов',
    #              birthday=date(2011, 1, 11), phone='89012345678', email='mail@yandex.ru')
    # db.users.add(name='Сева', username='Seva', lastname=None, birthday=None, phone='89876543210', email=None)
    # db.users.add(name='Юра', username='Yura', lastname='Мельник', birthday=None, phone=None, email=None)
    # db.users.add(name='Юра2', username='Yura2', lastname='Мельник',
    #              birthday=datetime.date(2011, 7, 14), phone=None, email=None)
    # views()

    # db.users.update(2, 'name', 'Никита')
    # views()

    # db.users.delete(2)
    # views()

def health_check_chats(db):

    def views():
        print('-' * 150)

        chats = db.chats.select_all()
        for c in chats:
            print(c.id, c.name, c.avatar_url, c.date_created, c.messages, c.participants, c.users)

        print('-' * 150)

    views()

    # db.chats.add(name='Сева')
    # views()

    # db.chats.update(5, 'avatar_url', '12345')
    # views()

    # db.chats.delete(6)
    # views()

def health_check_participants(db):
    def views():
        print('-' * 150)
        participants = db.participants.select_all()
        for p in participants:
            print(p.chat_id, p.user_id, p.role, p.joined_at, p.chat, p.user)

    views()

    # db.participants.add(chat_id=2, user_id=5)
    # db.participants.add(chat_id=2, user_id=7)
    # db.participants.add(chat_id=3, user_id=3)
    # db.participants.add(chat_id=3, user_id=5)
    # views()

    # db.participants.update(chat_id=1, user_id=5, attr_name='role', value=UserRoleEnum.pre_admin)
    # views()

    # db.participants.delete(chat_id=1, user_id=7)
    # views()

def health_check_messages(db):
    def views():
        print('-' * 150)
        messages = db.messages.select_all()
        for m in messages:
            print(m.id, m.type, m.text, m.file_id, m.chat_id, m.user_id, m.creation_date_time, m.chat, m.sender)

        print('-' * 150)

    views()

    # db.messages.add(chat_id=1, user_id=3, text='Привет всем!')
    # views()

    # db.messages.update(2, 'text', 'Хай!')
    # views()

    # db.messages.delete(2)
    # views()

# Создание сессии
with Session() as session:
    db = DataBase(session)
    # try:
    with session.begin():  # ← одна транзакция на всё
            # РАБОЧАЯ ЧАСТЬ

            health_check_users(db)
            health_check_chats(db)
            health_check_participants(db)
            health_check_messages(db)

    # except Exception as e:
    #     print(f"Ошибка: {e}")


