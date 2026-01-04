class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(
            f"Меня зовут {self.name}, я родился {self.birth_date}, "
            f"по профессии {self.occupation}, высшего образования {education}."
        )


person1 = Person("Нурбол", "29.08.2005", "backend разработчик", False)
person2 = Person("Азиз", "12.03.2005", "энергетик", True)
person3 = Person("Ислам", "05.11.2005", "медбрат", True)

print(person1.__dict__)
print(person2.__dict__)
print(person3.__dict__)

print()


person1.introduce()
person2.introduce()
person3.introduce()
