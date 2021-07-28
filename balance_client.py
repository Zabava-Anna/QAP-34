# В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек. То есть система будет хранить данные о своих клиентах и об их финансовых операциях. 

Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее: Клиент "Иван Петров". Баланс: 50 руб.
class Client:
    def __init__(self, name=str, balance=int):
        self.name = name
        self.balance = balance

    def about(self):
        return "Клиент '{0}', Баланс: {1} руб.".format(self.name, self.balance)

Ivanov = Client("Иванов", 50)
print(Ivanov.about())
