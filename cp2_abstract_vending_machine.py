from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def make_burp(self):
        pass


class Snack(ABC):
    @abstractmethod
    def make_thirsty(self):
        pass


class RegularBeverage(Beverage):
    def make_burp(self):
        return "BURP"


class RegularSnack(Snack):
    def make_thirsty(self):
        return "I'm thirsty"


class DietBeverage(Beverage):
    def make_burp(self):
        return "Diet - BURP"


class DietSnack(Snack):
    def make_thirsty(self):
        return "Diet - I'm thirsty"


class AbstractVendingMachine(ABC):
    @abstractmethod
    def create_beverage(self):
        pass

    @abstractmethod
    def create_snack(self):
        pass

    def show_beverage_info(self):
        beverage = self.create_beverage()
        info = {
            **beverage.__dict__,
            "type": type(beverage),
            "burp_sound": beverage.make_burp(),
        }
        return info

    def show_snack_info(self):
        snack = self.create_snack()
        info = {
            **snack.__dict__,
            "type": type(snack),
            "thirsty_sound": snack.make_thirsty(),
        }
        return info


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
        print(vending_machine.show_beverage_info())
        print(f'       - "{beverage_vending_machine.make_burp()}"')
        snack_vending_machine = vending_machine.create_snack()
        print(vending_machine.show_snack_info())
        print(f'       - "{snack_vending_machine.make_thirsty()}"')
