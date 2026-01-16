# родительский, суперкласс

class Car:
    # ининциализатор
    def __init__(self,  model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)

# дочерний, подклас
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model, color)
        self.number = number

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Bus {self.number} Driving to", destination)

class Truck(Car):
    def rive_to(self, model, color,):
        print("Truck Driving to")

bus_42 = Bus("Mersedes", "Red", "42")
truck = Truck("MaN", "white")
car_subaru = Car("Subaru", "red")
vehicles = (bus_42, car_subaru)
for v in vehicles:
    v.drive_to("Bishkek")