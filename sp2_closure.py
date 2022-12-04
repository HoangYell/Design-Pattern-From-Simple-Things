popsicle_ice_cream = "PopsicleIceCream"
cone_ice_cream = "IceCreamCone"
print("[original ice creams] ")
print(popsicle_ice_cream)
print(cone_ice_cream)


# main function
def decorate_ice_cream(layer_3, layer_2, layer_1, ice_cream):
    magic_number = 9
    layer_2_a, layer_2_b = layer_2[:magic_number], layer_2[magic_number:]
    decorated_ice_cream = f"{layer_3}({layer_2_a}({layer_1}({ice_cream})){layer_2_b})"
    return decorated_ice_cream


# closure
def prepare_recipe(func, layer_3, layer_2, layer_1):
    def updated_func(ice_cream):
        return func(layer_3, layer_2, layer_1, ice_cream)

    return updated_func


if __name__ == "__main__":
    # closure's outcome: updated function
    recipe = prepare_recipe(decorate_ice_cream, "Almond", "CondensedMilk", "Chocolate")
    almond_condensed_milk_chocolate_popsicle = recipe(popsicle_ice_cream)
    almond_condensed_milk_chocolate_cone = recipe(cone_ice_cream)
    print("\n[decorated ice creams] ")
    print(almond_condensed_milk_chocolate_popsicle)
    print(almond_condensed_milk_chocolate_cone)
