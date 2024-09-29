import shared


def set_values() -> None:
    for building in shared.buildings_array:
        building.set_value(calculate_building_value(building))

# value = (building CPS_per)/(cost)(time to afford)
def calculate_building_value(building):
    numerator = building.get_cps_per()
    if building.get_price() == 0:
        return 0

    denominator = (building.get_price()**2) / (shared.cps_without_clicking+shared.mouse_cps)
    return numerator / denominator