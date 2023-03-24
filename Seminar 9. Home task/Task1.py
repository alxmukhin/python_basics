class Road:
    def __init__(self, length, width, thickness, weight):
        self.length = length
        self.width = width
        self.thickness = thickness
        self.weight = weight

    def asphalt_weight(self):
        print("Масса асфальта необходимого для покрытия дорожного полотна:"
              f" {self.width * self.length * self.thickness * self.weight / 1000} т")


road1 = Road(5000, 20, 0.05, 25)
road1.asphalt_weight()
