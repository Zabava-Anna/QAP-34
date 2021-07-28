class Client:
    def __init__(self, name=str, balance=int):
        self.name = name
        self.balance = balance

    def about(self):
        return "Клиент '{0}', Баланс: {1} руб.".format(self.name, self.balance)

Ivanov = Client("Иванов", 50)
print(Ivanov.about())
