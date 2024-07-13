class User:
    def __init__(self, user_id, name, access_level='User'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level
        print(f"Уровень доступа {self.__name} изменен на {self.__access_level} !")

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='Admin')
        self.__admin_access_level = 'Admin'

    def get_admin_access_level(self):
        return self.__admin_access_level

    def __is_admin(self):
        return self.get_access_level() == 'Admin'

    def add_user(self, user_list, user):
        if self.__is_admin():
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: доступ запрещен. Только администраторы могут добавлять пользователей.")

    def remove_user(self, user_list, user_id):
        if self.__is_admin():
            user_to_remove = next((u for u in user_list if u.get_user_id() == user_id), None)
            if user_to_remove:
                user_list.remove(user_to_remove)
                print(f"Пользователь {user_to_remove.get_name()} удален.")
            else:
                print(f"Ошибка: пользователь с ID {user_id} не найден.")
        else:
            print("Ошибка: доступ запрещен. Только администраторы могут удалять пользователей.")


# Просмотр списка пользователей
def User_List():
    print("Список пользователей:")
    for user in global_user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


# Глобальный список пользователей
global_user_list = []

# Примеры использования
admin1 = Admin(1, 'Admin1')
user1 = User(2, 'User1')
user2 = User(3, 'User2')
user3 = User(4, 'User3', "Admin")
admin2 = Admin(5, 'Admin2')
user4 = User(6, 'User4')

# Добавление пользователей
admin1.add_user(global_user_list, admin1)
admin1.add_user(global_user_list, user1)
admin1.add_user(global_user_list, user2)
admin1.add_user(global_user_list, user3)
admin2.add_user(global_user_list, user4)
admin1.add_user(global_user_list, admin2)


# Попытка добавить пользователя обычным пользователем (ожидается ошибка)
# user1.add_user(global_user_list, User(4, 'User3'))  # Это вызовет ошибку, так как User не имеет метода add_user

User_List()
# Удаление пользователя
admin1.remove_user(global_user_list, user1.get_user_id())
admin2.remove_user(global_user_list, user3.get_user_id())

User_List()
admin2.set_access_level('User')
admin2.add_user(global_user_list, user1)
User_List()
admin2.set_access_level('Admin')
admin2.add_user(global_user_list, user1)
User_List()
admin1.set_access_level('User')
admin2.set_access_level('User')
admin1.remove_user(global_user_list, user1.get_user_id())
admin1.set_access_level('Admin')
admin1.remove_user(global_user_list, user1.get_user_id())
