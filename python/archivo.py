class Salmon:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def swim(self):
        print(f"{self.name} está nadando río arriba!")

    def eat(self, food):
        self.weight += food
        print(f"{self.name} comió {food}kg y ahora pesa {self.weight}kg.")

salmon1 = Salmon("Salmónito", 2, 3.5)

salmon1.swim()
salmon1.eat(0.5)