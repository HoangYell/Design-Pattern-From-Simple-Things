from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def make_burp(self):
        pass


class RegularBeverage(Beverage):
    def make_burp(self):
        return "BURP"


class DietBeverage(Beverage):
    def make_burp(self):
        return "Diet - BURP"


class VendingMachine(ABC):
    @abstractmethod
    def create_beverage(self):
        pass

    def show_info(self):
        beverage = self.create_beverage()
        info = {
            **beverage.__dict__,
            "type": type(beverage),
            "burp_sound": beverage.make_burp(),
        }
        return info


class RegularVendingMachine(VendingMachine):
    def create_beverage(self):
        return RegularBeverage()


class DietVendingMachine(VendingMachine):
    def create_beverage(self):
        return DietBeverage()


if __name__ == "__main__":
    for vending_machine in (RegularVendingMachine(), DietVendingMachine()):
        print(vending_machine.show_info())
