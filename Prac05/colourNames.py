
COLOUR_NAMES = {"blueviolet": "#8a2be2", "chocolate": "#d2691e", "coral": "#ff7f50",
                "darkturquoise": "#00ced1", "firebrick": "#b22222", "floralwhite": "#fffaf0",
                "forestgreen": "#228b22", "gray": "#bebebe", "hotpink": "#ff69b4", "khaki": "#f0e68c"}


# print(STATE_NAMES)
colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print("Colour code: {}".format(COLOUR_NAMES[colour]))
    else:
        print("Invalid short state")
    colour = input("Enter short state: ")

for key in COLOUR_NAMES:
    print("{:<15} is {}".format(key, COLOUR_NAMES[key]))