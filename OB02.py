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
