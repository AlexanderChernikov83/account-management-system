# Класс User и класс  Admin с инкапсуляцией

class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = "user"

    # Геттеры
    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттеры (если потребуется изменить имя)
    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"User[ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level}]"
# Класс admin, наследующий класс user

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = "admin"

    def get_admin_level(self):
        return self.__admin_access_level

    # Добавление пользователя в систему
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"✅ Пользователь '{user.get_name()}' добавлен.")
        else:
            print("❌ Ошибка: можно добавлять только объекты класса User.")

    # Удаление пользователя по ID
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"🗑 Пользователь с ID {user_id} удалён.")
                return
        print(f"⚠️ Пользователь с ID {user_id} не найден.")
