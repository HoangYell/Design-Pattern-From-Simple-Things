from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def make_burp(self):
        pass

    @abstractmethod
    def make_hungry(self):
        pass


class Snack(ABC):
    @abstractmethod
    def make_thirsty(self):
        pass


class RegularBeverage(Beverage):
    def make_burp(self):
        return "BURP"

    def make_hungry(self):
        return "I'm hungry"


class RegularSnack(Snack):
    def make_thirsty(self):
        return "I'm thirsty"


class DietBeverage(Beverage):
    def make_burp(self):
        return "Diet - BURP"

    def make_hungry(self):
        return "Diet - I'm hungry"

    def lose_weight(self):
        return "Only Diet - I lost weight"


class DietSnack(Snack):
    def make_thirsty(self):
        return "Diet - I'm thirsty"

    def make_anorexia(self):
        return "Only Diet - I'm anorexia"

    def make_healthy(self):
        return "Only Diet - I'm getting better"


class AbstractVendingMachine(ABC):
    @abstractmethod
    def create_beverage(self):
        pass

    @abstractmethod
    def create_snack(self):
        pass


class RegularVendingMachine(AbstractVendingMachine):
    def create_beverage(self):
        return RegularBeverage()

    def create_snack(self):
        return RegularSnack()


class DietVendingMachine(AbstractVendingMachine):
    def create_beverage(self):
        return DietBeverage()

    def create_snack(self):
        return DietSnack()


if __name__ == "__main__":
    for vending_machine in (RegularVendingMachine(), DietVendingMachine()):
        beverage_vending_machine = vending_machine.create_beverage()
        snack_vending_machine = vending_machine.create_snack()
        print(beverage_vending_machine.make_burp())
        print(beverage_vending_machine.make_hungry())
        print(snack_vending_machine.make_thirsty())
