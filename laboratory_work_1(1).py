import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов
class Auto:
    def __init__(self, brand: str, weight: Union[int, float]):
        """
        Создание объекта Автомобиль
        :param brand: Марка автомобиля
        :param weight: Масса автомобиля
        :raise: TypeError: Если название марки автомобиля не принадлежить типу str
        :raise: TypeError: Если масса автомобиля не принадлежит типу int или float
        :raise: ValueError: Если масса автомобиля меньше нуля
        Пример:
        >>> auto = Auto("UAZ", 2.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Название марки автомобиля должно быть типа str")
        self.brand = brand
        if not isinstance(weight, (int, float)):
            raise TypeError("Масса автомобиля должна быть типа int или float")
        if weight <= 0:
            raise ValueError("Масса автомобиля должна быть строго больше нуля")
        self.weight = weight

    def car_moving_forward(self, distance: Union[int, float]) -> None:
        """

        :param distance: Расстояние, которое нужно проехать
        :raise ValueError: Расстояние не может быть отрицательным

        Пример:
        >>> auto = Auto("UAZ", 2.5)
        >>> auto.car_moving_forward(10)
        """
        if distance < 0:
            raise ValueError(f"Расстояние не может быть отрицательным и не может равняться {distance}")
        ...

    def left_turn(self, angle: Union[int, float]) -> None:
        """
        :param angle: Угол поворота автомобиля

        Пример:
        >>> auto = Auto("UAZ", 2.5)
        >>> auto.left_turn(-30)
        """
        ...


class Thermos:
    def __init__(self, brand: str, capacity: Union[int, float]):
        """
        Создание объекта Термос
        :param brand: Марка термоса
        :param capacity: Вместимость термоса
        :raise: TypeError: Если название термоса не принадлежить типу str

        Пример:
        >>> thermos = Thermos("Rondell", 0.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Название термоса должно быть типа str")
        self.brand = brand
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость термоса должна быть типа int или float")
        if capacity <= 0:
            raise ValueError("Вместимость термоса должна быть строго больше нуля")
        self.capacity = capacity

    def pour_into_thermos(self, volume: Union[int, float]) -> None:
        """
        Наливает жидкость в термос
        :param volume: Объем, который нужно налить
        :raise ValueError: Объем не может быть отрицательным
        :raise TypeError: Объем должен быть либо int либо float
        Пример:
        >>> thermos = Thermos("Rondell", 0.5)
        >>> thermos.pour_into_thermos(0.4)
        """
        if volume < 0:
            raise ValueError(f"Объем не может быть отрицательным и не может равняться {volume}")
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть либо int либо float")
        ...

    def drop_thermos(self) -> bool:
        """
        Функция, которая проверяет, разбит термос или нет
        :return: Разбит или нет

        Пример:
        >>> thermos = Thermos("Rondell", 0.5)
        >>> thermos.drop_thermos()
        """
        ...

class Airport:
    def __init__(self, year_of_construction: int, efficiency: int):
        """
        Создание и подготовка к работе объекта Аэропорт
        :param country: страна в которой находится аэропорт
        :param year: год постройки
        Пример:
        >>> airport = Airport(2022, 90) #инициализация
        """
        if not isinstance(year_of_construction, (int)):
            raise TypeError("Год постройки должен быть типа int")
        if year_of_construction <= 0:
            raise ValueError("Год постройки должен быть больше или не равен нулю")
        self.year_of_construction = year_of_construction

        if not isinstance(efficiency, (int)):
            raise TypeError("кпд должен быть типа int")
        if efficiency <= 0:
            raise TypeError("кпд должен быть больше нуля")

    def plane_took_off(self) -> bool:
        """
        Функция которая проверяет, вылетел самолет или нет
        :return: Вылетел ли самолет
        Примеры:
        >>> airport = Airport(2022, 90)
        >>> airport.plane_took_off()
        """
        ...
    def come_in(self) -> bool:
        """
        Функция которая проверяет, зашли ли оюди в самолет
        :return: Зашли или нет
        Примеры:
        >>> airport = Airport(2022, 90)
        >>> airport.come_in()
        """
        ...
    def financing(self, money: Union[int, float]) -> None:
        """
        Финансирование аэропорта
        :param money: количество денег, поступившее в аэропорт
        :raise TypeError: money должен быть int или float
        :return: Деньги
        >>> airport = Airport(2022, 90)
        >>> airport.financing(1000000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("money должен быть int или float")





    if __name__ == "__main__":
        # TODO работоспособность экземпляров класса проверить с помощью doctest
        doctest.testmod()
