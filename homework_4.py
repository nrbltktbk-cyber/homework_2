class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            print("Номер телефона должен содержать ровно 10 цифр")


# Проверка
ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
    # Вася Пупкин 0700100200
    # Виктор Цой 0500123456

ContactList.add_contact("John Doe", "5551234")  # ❌ ошибка

try:
    ContactList.add_contact("John Doe", "5558881234")
except ValueError as e:
    print("Ошибка:", e)
