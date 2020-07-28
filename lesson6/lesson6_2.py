class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_of_asphalt(self):
        return f'Масса асфальта: {self.__length * self.__width * 25 * 5 / 1000} т'


a = Road(20, 5000)
print(a.mass_of_asphalt())
