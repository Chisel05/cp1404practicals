"""
CP1404/CP5632 Practical
Program for looking up the hexadecimal value of a colour from a dictionary of 10 colours.
"""
COLOUR_TO_HEXADECIMAL = {'apricot': '#fbceb1', 'aqua': '#00ffff', 'beaver': '#9f8170', 'beige': '#f5f5dc',
                         'bistre': '#3d2b1f', 'black': '#000000', 'bole': '#79443b', 'bone': '#e3dac9',
                         'brass': '#b5a642', 'buff': '#f0dc82'}

colour = input("Colour: ").lower()
while colour != "":
    try:
        print(COLOUR_TO_HEXADECIMAL[colour])
    except KeyError:
        print("Colour not found")
    colour = input("Colour: ").lower()
