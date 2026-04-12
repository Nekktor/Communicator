"""
Файл основного кода
"""

from Database.main import Session, DataBase

def health_check_users(db):
    def views():
        print('-' * 150)

        users = db.users.select_all()
        if users['isSuccess']:
            for user in users['data']:
                # print(user['id'], user['name'], user['username'])
                print(user)

        # else:
            # print(users['error'])
            # print(users['long_error'])

        print('-' * 150)

    views()

    # users = db.users.select_all_users_by_chat_id(chat_id=2)
    # if users['isSuccess']:
    #     for user in users['data']:
    #         print(user['id'], user['name'], user['username'])

    # print(db.users.exists(username='Nikita'))  # >>> True
    # print(db.users.exists(username='Nikitka')) # >>> False
    # print(db.users.exists(username='Yura3'))  # >>> False
    # print(db.users.exists(username='Seva2'))   # >>> False
    # print(db.users.exists(username='Seva'))    # >>> True
    # print(db.users.exists(username='Yura'))    # >>> True

    # print('-' * 150)

    # print(db.users.add(name='Никита', username='Nikita', lastname='Соколов',
    #              birthday='12-01-2011', phone='89012345678', email='mail@yandex.ru', password='1'))
    # print(db.users.add(name='Сева', username='Seva', lastname=None, birthday=None, phone='89876543210', email=None,
    #                    password='11'))
    # print(db.users.add(name='Юра', username='Yura', lastname='Мельник', birthday='14-07-2011', phone=None, email=None,
    #                    password=None))
    # print(db.users.add(name='123', username='123', lastname=None,
    #              birthday=None, phone=None, email=None, password='1111'))
    # views()

    # print(db.users.update(1, 'password', 'Nik'))
    # print(db.users.update(2, 'password', 'Sev'))
    # print(db.users.update(3, 'password', 'Yur'))
    # print(db.users.update(5, 'password', 'Nik2'))
    # views()

    # isRealId = db.users.exists(id=17)
    # if isRealId:
    #     print(db.users.delete(17))
    # views()

def health_check_chats(db):

    def views():
        print('-' * 150)

        chats = db.chats.select_all()
        if chats['isSuccess']:
            for chat in chats['data']:
                # print(chat['id'], chat['name'])
                print(chat)

        print('-' * 150)

    views()

    # print(f'Чаты пользователя с id= 1')
    # chats = db.chats.select_all_chats_by_id_user(user_id=1)
    # if chats['isSuccess']:
    #     for chat in chats['data']:
    #         print(chat)

    # print('-' * 150)

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
        if participants['isSuccess']:
           for participant in participants['data']:
                # print(f'chat_id: {participant['chat_id']}, user_id: {participant["user_id"]}')
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

    # print(db.participants.update(chat_id=1, user_id=1, attr_name='role', value='Админ'))
    # views()


    # print(db.participants.delete(user_id=1 , chat_id=4))
    # views()

def health_check_messages(db):
    def views():
        print('-' * 150)
        messages = db.messages.select_all()
        if messages['isSuccess']:
            for message in messages['data']:
               print(message)

        print('-' * 150)

    views()

    # messages = db.messages.select_all_messages_in_by_chat_id(chat_id=4)
    # if messages['isSuccess']:
    #     for message in messages['data']:
    #         print(message)


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

def test_real_simulated(db):
    """
    Проверка работоспособности кода.
    Ты, надеюсь сможешь переделать это в рабочий интерфейс
    """


    sing = input('1- зарегистрироваться\n2 - войти\nНомер действия: ')
    if sing == '1':
        username = input('Придумайте свой username: ')
        # Пока username существует
        while db.users.exists(username=username):
            print('Такой username уже занят. Попробуйте другой')
            username = input('username: ')

        name = input('Придумайте свой Ник: ')
        password = input('Придумайте свой пароль: ')

        # Добавление пользователя в БД
        response = db.users.add(name=name, username=username, password=password)
        if response['isSuccess']:
            print('Вы успешно зарегистрировались')

            # Вывод всех пользователй
            users = db.users.select_all()
            if users['isSuccess']:
                print('Список всех пользователей:')
                for user in users['data']:
                    print(user['name'], user['username'])

            else:
                print('Если вы видите это, значит знайте: это ошибка.')
                print(users)

        else:
            print('Если вы видите это, значит знайте: это ошибка')
            print(response)


    elif sing == '2':
        username = input('Введите свой username: ')
        password = input('Введите свой пароль: ')

        # Пока username и password не будут относиться к одной строчке
        isAble = db.users.exists(username=username, password=password)
        while not isAble:
            print('Неправильный username или пароль')
            username = input('username: ')
            password = input('пароль: ')
            isAble = db.users.exists(username=username, password=password)

        # Получение словаря в user_response['data'], где есть id и name
        user_response = db.users.select_by_username(username=username)
        if user_response['isSuccess']:
            user = user_response['data']
            print(f'Жалуйте добро, {user['name']}')

            # Получение всех чатов, которые есть у пользователя (вся инфа об чате, подробнее см. в models/chats.py)
            chats = db.chats.select_all_chats_by_id_user(user_id=user['id'])
            if chats['isSuccess']:
                print('Выберите чат из списка доступных:', end=' ')
                for chat in chats['data']:
                    print(chat['name'], end=', ')

                selected_chat = input('\nЧат: ')
                for chat in chats['data']:
                    if chat['name'] == selected_chat:
                        chat_id = chat['id']
                        break

                # Получение всех сообщений, которые есть в чате (вся инфа об сообщении, подробнее см. в models/messages.py)
                messages = db.messages.select_all_messages_by_chat_id(chat_id=chat_id)
                if messages['isSuccess']:
                    for message in messages['data']:
                        # Получение имени пользователя по id
                        name_response = db.users.select_name_by_id(message['user_id'])
                        if name_response['isSuccess']:
                            print(f'[{name_response['data']['name']}]: {message['text']}')
                        else:
                            print('Если вы видите это, значит знайте: это ошибка')
                            print(name_response)

                else:
                    print('Если вы видите это, значит знайте: это ошибка')
                    print(chats)

            else:
                print('Если вы видите это, значит знайте: это ошибка.')
                print(chats)

        else:
            print('Если вы видите это, значит знайте: это ошибка')
            print(user_response)


    # print('Выберите чат из доступных:')
    # print(f'[{'user'}]: {'message'}')


# Создание сессии
with Session() as session:
    db = DataBase(session)
    # try:
    with session.begin():  # ← одна транзакция на всё
            # РАБОЧАЯ ЧАСТЬ

            health_check_users(db)  # Посмотреть всех пользователей
            health_check_chats(db)  # Посмотреть чаты
            health_check_participants(db)  # Участники групп
            health_check_messages(db)  # Сообщения
            print('\n')
            test_real_simulated(db)  # Интерактивный тест базовейших функций

    # except Exception as e:
    #     print(f"Ошибка: {e}")


