import random
import pyfiglet

names = ['Joe', 'Jessica', 'David', 'Alora', 'Martine', 'JoeBob', 'Amelie', 'Sauron', 'Squirtl', 'Naruto', 'Scott']
selected_name = random.choice(names)

color_list = list(pyfiglet.COLOR_CODES.keys())

color_list.remove('BLACK')
color_choice = random.choice(color_list)
font_list = pyfiglet.FigletFont.getFonts()
font_choice = random.choice(font_list)
print(selected_name, color_choice, font_choice)
pyfiglet.print_figlet(selected_name.upper(), font=font_choice, colors=color_choice)
