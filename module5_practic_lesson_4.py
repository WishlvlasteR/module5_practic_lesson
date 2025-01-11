class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        """Добавляем названия объектов в список атрибута houses_history """
        if args:
            cls.houses_history.append(args[0])
            return super().__new__(cls)

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

    def __del__(self):
        """Удаляет объект и выводит сообщение"""
        print(f'{self.name} снесён, но он останется в истории"')

    def __len__(self):
        """Возвращает количество этажей в здании."""
        return self.number_of_floors

    def __str__(self):
        """
        Возвращает строку с названием зданий
        и количеством этажей в этом здании.
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, value):
        """
        Увеличение количества этажей на значение value,
        с проверкой на принадлежность типа объектов
        """
        if isinstance(value,int):
            self.number_of_floors += value
            return self
        else:
            print('Ошибка введено не число,кол-во этажей осталось прежним.')
            return self

    def __iadd__(self, value):
        """
        Делегируем возврат значения методу __add__
        разница между ними что __iadd__ изменяет
        текущий объект, а не создаёт новый.
        """
        return self.__add__(value)

    def __radd__(self, value):
        """
        Делегируем возврат значения методу __add__
        разница между ними что __add__ применяется
        когда объект класса находится слева, а __radd__
        справа, обеспечивает симметричность операции +.
        """
        return self.__add__(value)

    def __gt__(self, other):
        """Сравнение: больше > по количеству этажей."""
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self,other):
        """Сравнение: больше > или равно = по количеству этажей."""
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self,other):
        """Сравнение: меньше < по количеству этажей."""
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self,other):
        """Сравнение: меньше < или = по количеству этажей."""
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __eq__(self, other):
        """
        Сравнение на равенство == по количеству этажей,
        Сравнение: не равно != по количеству этажей.
        С проверкой на принадлежность типа объектов.
        Если other — int, возвращается результат
        сравнения количества этажей с этим числом.
        Если other — объект класса House, сравнивается
        количество этажей обоих зданий.
        """
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors


    def __ne__(self, other):
        """
        Сравнение: не равно != по количеству этажей.
        С проверкой на принадлежность типа объектов.
        Если other — int, возвращается результат
        сравнения количества этажей с этим числом.
        Если other — объект класса House, сравнивается
        количество этажей обоих зданий.
        Если other не относится ни к числам, ни к классу House,
        возвращает значение NotImplemented. Это позволяет
        вызвать обратный метод.
        """
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
