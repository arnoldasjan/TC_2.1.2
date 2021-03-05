from unittest import TestCase


class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__model = model
        self.__color = color
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__autopilot = autopilot
        self.__efficiency = efficiency

    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def color(self) -> str:
        return self.__color

    @property
    def seats_count(self) -> int:
        return self.__seats_count

    @property
    def is_locked(self) -> bool:
        return self.__is_locked

    @seats_count.setter
    def seats_count(self, new_seats_count: int) -> None:
        if new_seats_count >= 2:
            self.__seats_count = new_seats_count
        else:
            print("Seats count cannot be lower than 2!")

    def autopilot(self, obsticle: str) -> str:
        # COMPLETE THE FUNCION
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obsticle}"
        else:
            return f"Autopilot is not available"

    def unlock(self) -> None:
        """Unlocks the door of Tesla if it is locked, prints that it is already unlocked if so"""
        if self.__is_locked:
            self.__is_locked = False
        else:
            print('It is already unlocked.')

    def lock(self) -> None:
        """Locks the door of Tesla if it is unlocked, prints that it is already locked if so"""
        if self.__is_locked:
            print('It is already locked.')
        else:
            self.__is_locked = True

    def open_doors(self) -> str:
        """Opens the door sideways of Tesla if it is unlocked, prints that it is locked if so"""
        # COMPLETE THE FUNCION
        if self.__is_locked:
            return 'Car is locked!'
        else:
            return "Doors opens sideways"

    def check_battery_level(self) -> str:
        # COMPLETE THE FUNCTION
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self):
        # COMPLETE THE FUNCTION
        # BATTERY LEVEL SHOULD BE SET TO 100
        self.__battery_charge = 100

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        # COMPLETE THE FUNCTION
        if self.__battery_charge - battery_discharge_percent >= 0:
            # ADD YOUR CODE
            self.__battery_charge = self.__battery_charge - battery_discharge_percent
            return self.check_battery_level()
        # ADD YOUR CODE
        else:
            print('Battery charge level is too low!')
            return self.check_battery_level()


class TestTesla(TestCase):
    def test_charge_battery(self):
        c = Tesla('Model3', 'black')
        c.charge_battery()
        self.assertEqual(c.check_battery_level(), 'Battery charge level is 100%')

    def test_charge_battery(self):
        c = Tesla('Model3', 'black')
        c.unlock()
        self.assertEqual(c.is_locked, False)
