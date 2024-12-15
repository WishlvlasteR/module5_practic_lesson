class House():
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
        if new_floor <= self.number_of_floors > 1:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(19)
h2.go_to(2)
