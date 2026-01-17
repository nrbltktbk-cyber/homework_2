
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Геттеры
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    # Сеттеры
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Возраст не может быть отрицательным")

    # Метод для переопределения в дочерних классах
    def make_sound(self):
        return "Some generic animal sound"


# Класс-собака
class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


# Класс-кошка
class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"


# Пример использования
dog1 = Dog("Бобик", 3)
cat1 = Cat("Мурка", 2)

# Демонстрация полиморфизма
animals = [dog1, cat1]
for animal in animals:
    print(f"{animal.name} издаёт звук: {animal.make_sound()}")

# Изменение приватных атрибутов через сеттеры
dog1.name = "Рекс"
dog1.age = 4
cat1.name = "Снежок"
cat1.age = 3

print(f"{dog1.name} теперь {dog1.age} лет")
print(f"{cat1.name} теперь {cat1.age} лет")
