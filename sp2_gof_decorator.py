class IceCream:
    def taste(self):
        return "IceCream"


class PopsicleIceCream(IceCream):
    def taste(self):
        return "PopsicleIceCream"


class ConeIceCream(IceCream):
    def taste(self):
        return "ConeIceCream"


popsicle = PopsicleIceCream()
cone = ConeIceCream()
print("[original ice creams] ")
print(popsicle.taste())
print(cone.taste())


class Decorator(IceCream):
    _component = None

    def __init__(self, component):
        print(f"{type(self)} is decorating the {type(component)}")
        self._component = component

    @property
    def component(self):
        return self._component

    def taste(self):
        return self._component.taste()


class ChocolateDecorator(Decorator):
    def taste(self):
        return f"Chocolate({self.component.taste()})"


class CondensedMilkDecorator(Decorator):
    def taste(self):
        return f"Condensed({self.component.taste()})Milk"


class AlmondDecorator(Decorator):
    def taste(self):
        return f"Almond({self.component.taste()})"


if __name__ == "__main__":
    chocolate_popsicle = ChocolateDecorator(popsicle)
    chocolate_cone = ChocolateDecorator(cone)
    condensed_milk_chocolate_popsicle = CondensedMilkDecorator(chocolate_popsicle)
    condensed_milk_chocolate_cone = CondensedMilkDecorator(chocolate_cone)
    almond_condensed_milk_chocolate_popsicle = AlmondDecorator(
        condensed_milk_chocolate_popsicle
    )
    almond_condensed_milk_chocolate_cone = AlmondDecorator(
        condensed_milk_chocolate_cone
    )
    print("\n[decorated ice creams] ")
    print(almond_condensed_milk_chocolate_popsicle.taste())
    print(almond_condensed_milk_chocolate_cone.taste())
