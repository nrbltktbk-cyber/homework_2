class Car:
    #инициализатор
    def __init__(self, model, color, yearofrelaese, max_speed):
        self.model = model
        self.color = color
        self.yearofrelaese = yearofrelaese
        self.max_speed = max_speed

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)

    def chenge_color(self, new_color):
        self.color = new_color

car_subaru = Car("Subaru", "red", "2025", "140" )
car_kia = Car("kia", "black", "2024", "160")

print(type(car_subaru))
print(type(car_kia))
print(car_subaru)
print(car_kia)
print(car_subaru.model)
print(car_subaru.color)
print(car_subaru.yearofrelaese)
print(car_subaru.max_speed)

#print(type("forester"))
car_subaru.drive_to("Bishkek")


print(car_kia.model)
print(car_kia.color)
print(car_kia.yearofrelaese)
car_kia.chenge_color("white")

car_kia.drive_to("Karakol")
print(car_kia.max_speed)
