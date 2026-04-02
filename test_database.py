"""
Файл основного кода.
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
    #              birthday=date(2011, 7, 14), phone=None, email=None)
    # views()

    # db.users.update(13, 'name', 'Юрчик')
    # views()

    # db.users.delete(14)
    # views()

def health_check_chats(db):

    def views():
        print('-' * 150)

        chats = db.chats.select_all()
        for c in chats:
            print(c.id, c.name, c.avatar_url, c.date_created, c.messages, c.participants, c.users)

        print('-' * 150)

    views()

    # db.chats.add(name='Разработка немыслимого')
    # db.chats.add(name='ЮН')
    # db.chats.add(name='НС')
    # db.chats.add(name='СЮ')
    # db.chats.add(name='СЮ')
    # views()

    # db.chats.update(5, 'avatar_url', '12345')
    # views()

    # db.chats.delete(9)
    # views()

def health_check_participants(db):
    def views():
        print('-' * 150)
        participants = db.participants.select_all()
        for p in participants:
            print(p.chat_id, p.user_id, p.role, p.joined_at, f'Chat: {p.chat}', f'User: {p.user}')

        print('-' * 150)

    views()

    # db.participants.add(chat_id=5, user_id=10)
    # db.participants.add(chat_id=5, user_id=12)
    # db.participants.add(chat_id=5, user_id=13)

    # db.participants.add(chat_id=6, user_id=10)
    # db.participants.add(chat_id=6, user_id=13)

    # db.participants.add(chat_id=7, user_id=10)
    # db.participants.add(chat_id=7, user_id=12)

    # db.participants.add(chat_id=8, user_id=10)
    # db.participants.add(chat_id=8, user_id=12)
    # db.participants.add(chat_id=6, user_id=12)
    # views()

    # db.participants.update(chat_id=5, user_id=10, attr_name='role', value=UserRoleEnum.pre_admin)
    # views()

    # db.participants.delete(chat_id=6, user_id=12)
    # views()

def health_check_messages(db):
    def views():
        print('-' * 150)
        messages = db.messages.select_all()
        for m in messages:
            print(m.id, m.type, m.text, m.file_id, f'chat_ud: {m.chat_id}', f'user_id: {m.user_id}',
                  m.creation_date_time, f'chat: {m.chat}', f'sender: {m.sender}')

        print('-' * 150)

    views()

    # db.messages.add(chat_id=5, user_id=10, text='Привет всем от Никиты!')
    # db.messages.add(chat_id=5, user_id=12, text='Привет всем от Севы!')
    # db.messages.add(chat_id=5, user_id=13, text='Привет всем от Юры!')
    # db.messages.add(chat_id=6, user_id=13, text='Никит, как дела? (от Юры)')
    # db.messages.add(chat_id=8, user_id=12, text='Юр, как дела? (от Севы)')
    # db.messages.add(chat_id=5, user_id=12, text='Как удалить это сообщение?')
    # db.messages.add(chat_id=5, user_id=10, text='Как вам моя БД?')
    # views()

    # db.messages.update(3, 'text', '嗨 everyone!')
    # views()

    # db.messages.delete(6)
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


