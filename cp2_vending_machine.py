from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def make_burp(self):
        pass

    def show_info(self):
        info = {
            **self.__dict__,
            "type": type(self),
            "burp_sound": self.make_burp(),
        }
        return info


class RegularBeverage(Beverage):
    def make_burp(self):
        return "BURP"


class DietBeverage(Beverage):
    def make_burp(self):
        return "Diet - BURP"


class BeverageVendingMachine:
    def generate(self, beverage_type):
        if beverage_type == "Regular":
            return RegularBeverage()
        elif beverage_type == "Diet":
            return DietBeverage()


if __name__ == "__main__":
    for beverage_type in ("Regular", "Diet"):
        beverage = BeverageVendingMachine().generate(beverage_type)
        print(beverage.show_info())
