class Computer:  

    def __init__(self, name, amount):
        self.name = name
        print("Разработан компуктер ", name)
        self.amount = amount

        def info(self):
            print(f"{self.name} продается, потеря зрения: {self.amount}")



class people:

    def __init__(self, name, h):
        self.name = name
        self.health = h
        print("Создан лунтик 2.0 с именем", self.name)

    def playing(self, play_computer):
        print(f"{self.name} играет в какой-то визюал студиа код")
        self.health -= play_computer.amount
        if (self.health < 70):
           print(f"{self.name} наигрался!")
        if(self.health < 0):
            
            


    def info(self):
        print(f"Зрение {self.health}")


oleg = people("ОЛЕГ", 100)