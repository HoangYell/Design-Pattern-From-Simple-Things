popsicle_ice_cream = "PopsicleIceCream"
cone_ice_cream = "IceCreamCone"
print("[original ice creams] ")
print(popsicle_ice_cream)
print(cone_ice_cream)


# decorator with params
def prepare_recipe_with_params(layer_3, layer_2, layer_1):
    def prepare_recipe(func):
        def updated_func(ice_cream):
            magic_number = 9
            layer_2_a, layer_2_b = layer_2[:magic_number], layer_2[magic_number:]
            front_ice_cream = f"{layer_3}({layer_2_a}({layer_1}("
            back_ice_cream = f")){layer_2_b})"
            half_decorated_ice_cream = func(front_ice_cream + ice_cream)
            decorated_ice_cream = half_decorated_ice_cream + back_ice_cream
            return decorated_ice_cream

        return updated_func

    return prepare_recipe


@prepare_recipe_with_params("Almond", "CondensedMilk", "Chocolate")
# main function
def decorate_ice_cream(ice_cream):
    return ice_cream


if __name__ == "__main__":
    almond_condensed_milk_chocolate_popsicle = decorate_ice_cream(popsicle_ice_cream)
    almond_condensed_milk_chocolate_cone = decorate_ice_cream(cone_ice_cream)
    print("\n[decorated ice creams] ")
    print(almond_condensed_milk_chocolate_popsicle)
    print(almond_condensed_milk_chocolate_cone)
