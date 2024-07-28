from vehicle import Vehicle

class Car(Vehicle):
    def start_engine(self):
        print("car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine has started")
    