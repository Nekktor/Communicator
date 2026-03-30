"""
Файл основного кода
"""

from Database.main import Session, DataBase
import datetime


# Создание сессии
with Session() as session:
    db = DataBase(session)
    try:
        with session.begin():  # ← одна транзакция на всё
            # РАБОЧАЯ ЧАСТЬ

            db.users.add(name='Никита', username='Nikita', lastname='Соколов',
                    birthday=datetime.date(2011, 1, 11), phone='89012345678', email='mail@yandex.ru')
            db.users.add(name='Сева', username='Seva', lastname=None, birthday=None, phone='89876543210', email=None)
            db.users.add(name='Юра', username='Yura', lastname='Мельник', birthday=None, phone=None, email=None)
            db.users.add(name='Юра2', username='Yura2', lastname='Мельник',
                         birthday=datetime.date(2011, 7, 14), phone=None, email=None)

            print('-' * 150)

            users = db.users.select_all()
            for user in users:
                print(user.id, user.name, user.username, user.lastname, user.birthday, user.avatar_url,
                      user.date_created, user.last_time_online, user.phone, user.email)

            print('-' * 150)

            db.users.update(1, 'username', 'NeKit_S')

            print('-'*150)

            users = db.users.select_all()
            for user in users:
                print(user.id, user.name, user.username, user.lastname, user.birthday, user.avatar_url,
                      user.date_created, user.last_time_online, user.phone, user.email)

            print('-' * 150)

            db.users.delete(4)

            print('-' * 150)

            users = db.users.select_all()
            for user in users:
                print(user.id, user.name, user.username, user.lastname, user.birthday, user.avatar_url,
                      user.date_created, user.last_time_online, user.phone, user.email)

            print('-' * 150)



    except Exception as e:
        print(f"Ошибка: {e}")


