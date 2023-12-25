import random


class Urls:
    MAIN_URL = "https://qa-scooter.praktikum-services.ru/" # адрес главной
    ORDER_URL = "https://qa-scooter.praktikum-services.ru/order" # адрес заказа
    DZEN_URL = "https://dzen.ru/?yredirect=true" # адрес дзена

class Data:
    NAME_LIST = ["Ира", "Иван", "Толя", "Василий"]
    NAME = random.choice(NAME_LIST)

    LASTNAME_LIST = ["Джигарханян", "Слепаков", "Родригез", "Бульдогов"]
    LASTNAME = random.choice(LASTNAME_LIST)

    ADDRESS_LIST = ["Воронеж, ул.Зои, 13", "Тула, ул.Ленина, 7", "Бобруйск, ул. Пугачева, 101"]
    ADDRESS = random.choice(ADDRESS_LIST)

    PHONE = f'+7{random.randint(9000000000, 9999999999)}'

    DATE_LIST = ["01.12.2023", "31.12.2023"]
    DATE = random.choice(DATE_LIST)

    COMMENT_LIST = ["Good day!)", "Написать и позвонить"]
    COMMENT = random.choice(COMMENT_LIST)