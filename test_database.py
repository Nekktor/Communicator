"""
Файл основного кода
"""

from Database.main import Session, DataBase


def health_check_users(db):
    def views():
        print('-' * 150)

        users = db.users.select_all()
        for user in users:
            print(user)

        print('-' * 150)

    views()

    # print(db.users.exists('username', 'Nikita'))  # >>> True
    # print(db.users.exists('username', 'Nikitka')) # >>> False
    # print(db.users.exists('username', 'Yura3'))  # >>> False
    # print(db.users.exists('username', 'Seva2'))   # >>> False
    # print(db.users.exists('username', 'Seva'))    # >>> True
    # print(db.users.exists('username', 'Yura'))    # >>> True


    # db.users.add(name='Никита', username='Nikita', lastname='Соколов',
    #              birthday='12-01-2011', phone='89012345678', email='mail@yandex.ru')
    # db.users.add(name='Сева', username='Seva', lastname=None, birthday=None, phone='89876543210', email=None)
    # db.users.add(name='Юра', username='Yura', lastname='Мельник', birthday='14-07-2011', phone=None, email=None)
    # db.users.add(name='Юра2', username='Yura2', lastname='Мельник',
    #              birthday='14-07-2011', phone=None, email=None)
    # views()

    # db.users.update(3, 'name', 'Юрчик')
    # views()

    # db.users.delete(4)
    # views()

def health_check_chats(db):

    def views():
        print('-' * 150)

        chats = db.chats.select_all()
        for chat in chats:
            print(chat)

        print('-' * 150)

    views()

    print(f'Чаты пользователя с id= 10')
    chats = db.chats.select_all_chats_by_id_user(user_id=1)
    for chat in chats:
        print(chat)

    print('-' * 150)

    # db.chats.add(name='Разработка немыслимого')
    # db.chats.add(name='ЮН')
    # db.chats.add(name='НС')
    # db.chats.add(name='СЮ')
    # db.chats.add(name='СЮ')
    # views()

    # db.chats.update(1, 'avatar_url', '12345')
    # views()

    # db.chats.delete(5)
    # views()

def health_check_participants(db):
    def views():
        print('-' * 150)
        participants = db.participants.select_all()
        for participant in participants:
            print(participant)

        print('-' * 150)

    views()

    # db.participants.add(chat_id=1, user_id=1)
    # db.participants.add(chat_id=1, user_id=2)
    # db.participants.add(chat_id=1, user_id=3)
    #
    # db.participants.add(chat_id=2, user_id=1)
    # db.participants.add(chat_id=2, user_id=3)
    #
    # db.participants.add(chat_id=3, user_id=1)
    # db.participants.add(chat_id=3, user_id=2)
    #
    # db.participants.add(chat_id=4, user_id=1)
    # db.participants.add(chat_id=4, user_id=2)
    # db.participants.add(chat_id=4, user_id=3)
    # views()
    #
    # db.participants.update(chat_id=1, user_id=1, attr_name='role', value='Админ')
    # views()
    #
    # db.participants.delete(chat_id=4, user_id=1)
    # views()

def health_check_messages(db):
    def views():
        print('-' * 150)
        messages = db.messages.select_all()
        for message in messages:
            print(message)

        print('-' * 150)

    views()

    # db.messages.add(chat_id=1, user_id=1, text='Привет всем от Никиты!')
    # db.messages.add(chat_id=1, user_id=2, text='Привет всем от Севы!')
    # db.messages.add(chat_id=1, user_id=3, text='Привет всем от Юры!')
    # db.messages.add(chat_id=2, user_id=3, text='Никит, как дела? (от Юры)')
    # db.messages.add(chat_id=4, user_id=2, text='Юр, как дела? (от Севы)')
    # db.messages.add(chat_id=1, user_id=2, text='Как удалить это сообщение?')
    # db.messages.add(chat_id=1, user_id=1, text='Как вам моя БД?')
    # views()
    #
    # db.messages.update(3, 'text', '嗨 everyone!')
    # views()
    #
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


