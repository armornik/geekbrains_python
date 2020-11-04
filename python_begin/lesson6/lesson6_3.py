class Worker:
    def __init__(self, name, surname, position=None, __income=None):
        if __income is None:
            __income = {'wage': 100000, 'bonus': 5000}
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = __income


class Position(Worker):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'


a = Position('Kostya', 'Zayacev')
print(a.get_full_name())
print(a.position)
print(a._Worker__income)
