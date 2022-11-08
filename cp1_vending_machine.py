import abc


# Input 1: Having a menu of beverages:
class MENU:
    PEPSI = 1
    COKE = 2
    MONSTER = 3


class Beverage(metaclass=abc.ABCMeta):
    id = ""
    carbon_dioxide = 0

    # @abc.abstractmethod means: in the concrete class, The method have to re-defined
    @abc.abstractmethod
    def make_burp(self):
        return ""


# Input 2: Beverages are being sold.
class Pepsi(Beverage):
    id = MENU.PEPSI
    carbon_dioxide = 3

    def make_burp(self):
        return f"B{'U' * self.carbon_dioxide}RP"


# Input 2: Beverages are being sold.
class Coke(Beverage):
    id = MENU.COKE
    carbon_dioxide = 2

    def make_burp(self):
        return f"BU{'R' * self.carbon_dioxide}P"


# Input 2: Beverages are being sold.
class Monster(Beverage):
    id = MENU.MONSTER
    carbon_dioxide = 1

    def make_burp(self):
        return f"BURP"


class BeverageVendingMachine:
    @property
    def subclasses(self):
        # [<class 'Pepsi'>, <class 'Coke'>, <class 'Monster'>]
        return Beverage.__subclasses__()

    @property
    def subclass_mapping(self):
        # {1: <class 'Pepsi'>, 2: <class 'Coke'>, 3: <class 'Monster'>}
        return {beverage.id: beverage for beverage in self.subclasses}

    def generate(self, key):
        subclass = self.subclass_mapping[key]
        instance = subclass()
        return instance

    @property
    def generate_carbonated_beverages(self):
        return [
            subclass() for subclass in self.subclasses if subclass.carbon_dioxide > 1
        ]


if __name__ == "__main__":
    beverage_vending_machine = BeverageVendingMachine()

    print("generate a beverage by id")
    # Input 3: Knowing the beverage you need to buy.
    coke = beverage_vending_machine.generate(MENU.COKE)
    # Expected Output 1: Get a beverage
    print(coke)
    # Expected Output 2: Drink your beverage and make a burp
    print(coke.make_burp())

    print("generate all carbonated beverages")
    carbonated_beverages = beverage_vending_machine.generate_carbonated_beverages
    print(carbonated_beverages)
