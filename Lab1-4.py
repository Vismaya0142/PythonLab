
ListColour = [["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000", "800000", "FFFF00"]]

def convert_to_dicts(colors, codes):
    return [{"colorName": name, "colorCode": code} for name, code in zip(colors, codes)]

color_dicts = convert_to_dicts(ListColour[0], ListColour[1])

for color_dict in color_dicts:
    print(color_dict)
