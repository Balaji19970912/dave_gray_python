class Vehicle:
    def __init__(self, make, model) :
        self.make = make
        self.model = model
    def moves(self):
        print('Moves along...')
    def getModelDetails(self):
        print(f"I'm {self.make} and my model is {self.model}")

myCar = Vehicle('Ford Bronco','Raptor')

print(myCar.make)
print(myCar.model)
myCar.moves()

class Aeroplane(Vehicle):
    def moves(self):
        print("Flies...")

class Truck(Vehicle):
    def moves(self):
        print("Rumles...")

myCar.getModelDetails()

aeroPlaneName1 = Aeroplane('Boeing','370')

aeroPlaneName1.getModelDetails()
aeroPlaneName1.moves()