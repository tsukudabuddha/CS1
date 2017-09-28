"""OOP_Example."""


class Car(object):
    """Car Class."""

    def __init__(self, player_name, make, model, color):
        """Initialize Car."""
        self.wheels = 4
        self.player_name = player_name
        self.make = make
        self.model = model
        self.color = color

    def honk(self):
        """Beep-Beep."""
        print("Beep-Beep")


my_new_car = Car("Andrew", "Acura", "NSX", "Red")
my_other_new_car = Car("Andrew", "Nissan", "Silvia S15", "White")
print("car make: " + my_new_car.make)
print("new car: " + my_other_new_car.make + " " + my_other_new_car.model)
my_new_car.honk()
