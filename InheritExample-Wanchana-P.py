class Vehicle:
    licenseNimber = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass
car1 = Car()
car1.turnOnAirConditioner()
pickup1 = PickUp()
pickup1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estateCar1 = EstateCar()
estateCar1.turnOnAirConditioner()