class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"работаю {self.occupation}"
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я одногруппник, "
            f"родился {self.birth_date}, "
            f"работаю {self.occupation}, "
            f"учусь в группе {self.group_name}"
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я друг, "
            f"родился {self.birth_date}, "
            f"работаю {self.occupation}, "
            f"моё хобби — {self.hobby}"
        )

classmate1 = Classmate("Umut", "12.03.2000", "студент", "Python-01")
classmate2 = Classmate("Бектур", "05.12.2000", "программист", "Python-02")

friend1 = Friend("Алмаз", "10.08.1999", "дизайнер", "рисование")
friend2 = Friend("Руслан", "22.01.2001", "тестировщик", "игры")

classmate1.introduce()
classmate2.introduce()

friend1.introduce()
friend2.introduce()
