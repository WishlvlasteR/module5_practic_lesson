class House:
    def __init__(self, name, number_of_floors):
        """Инициализация объекта House с названием и количеством этажей."""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Переход на заданный этаж.
        Выводит этажи от 1 до new_floor, если он существует.
        Если этаж недопустим, выводит сообщение об ошибке.
        """
        if self.number_of_floors >= new_floor > 0:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """Возвращает количество этажей в здании."""
        return self.number_of_floors

    def __str__(self):
        """
        Возвращает строку с названием зданий
        и количеством этажей в этом здании.
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
