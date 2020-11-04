class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self) -> str:
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self) -> str:
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self) -> str:
        return f'Запуск отрисовки {self.title}. Можно легко стереть'


class Handle(Stationery):
    def draw(self) -> str:
        return f'Запуск отрисовки {self.title}. Осторожно, очень маркий'


stationery = Stationery('Pencil')
print(stationery.draw())

pen = Pen('ручкой')
print(pen.draw())

pencil = Pencil('карандашом')
print(pencil.draw())

handle = Handle('маркером')
print(handle.draw())
