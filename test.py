class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner


owner = Owner("mana", 12)

dog = Dog("puppy", 1, owner)

print(dog.owner)
