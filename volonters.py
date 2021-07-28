# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров. Вам необходимо написать программу, 
# которая позволяла бы составлять список нескольких гостей. Решите задачу с помощью метода конструктора и примените один из принципов наследования.

При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
class Volonter:
    def __init__(self, name=str, lastname = str, city=str, status=str):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.status = status
    def about(self):
        return "{0} {1}, {2}, статус '{3}'".format(self.name, self.lastname, self.city, self.status)

pers1 = Volonter(input("введите Имя \n"), input("Введите Фамилию \n"), input("Введите Городо \n"), input("Ваш статус \n"))
pers2 = Volonter(input("введите Имя \n"), input("Введите Фамилию \n"), input("Введите Городо \n"), input("Ваш статус \n"))
pers3 = Volonter(input("введите Имя \n"), input("Введите Фамилию \n"), input("Введите Городо \n"), input("Ваш статус \n"))


Volonters = [pers1, pers2, pers3]
for pers in Volonters:
    print(pers.about())
