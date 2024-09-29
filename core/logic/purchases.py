import shared




def set_values():
    for building in shared.buildings_array:
        building.set_value(calculate_building_value(building))

# value = (building CPS_per)/(cost)(time to afford)
def calculate_building_value(building):

    numerator = building.get_cps_per()
    denominator = (building.get_price**2) / shared.cps_without_clicking
    return numerator / denominator + 200