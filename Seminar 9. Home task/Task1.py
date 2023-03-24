class IsPositive:
    def __init__(self):
        self._my_value = 0

    def __get__(self, instance, owner):
        return self._my_value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение параметра должно быть положительным!")
        self._my_value = value


class Road:
    length = IsPositive()
    width = IsPositive()
    thickness = IsPositive()
    weight = IsPositive()

    def __init__(self, length, width, thickness, weight):
        self.length = length
        self.width = width
        self.thickness = thickness
        self.weight = weight / 1000

    def asphalt_weight(self):
        print("Масса асфальта необходимого для покрытия дорожного полотна: "
              f"{self.width * self.length * self.thickness * self.weight} т")


road1 = Road(5000, 20, 0.05, 25)
road1.asphalt_weight()
road2 = Road(5000, -20, 0.05, 25)
road1.asphalt_weight()
