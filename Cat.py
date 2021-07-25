class Cat:
    def __init__(self, name="", gender="", age=int):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def about(self):
        print(f"Кот: {self.name}")
        print(f"пол: {self.gender}")
        print(f"возраст: {self.age}")
        return
