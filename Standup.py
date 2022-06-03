import os.path
import pickle
import random
from os import path

import pyfiglet

names = ['Alora', 'Grant', 'Sam', 'Arnela','Monika', 'Manager\'s Choice', 'Chris', 'Nudzejma', 'Mirza', 'Jeeka']
selected_name = random.choice(names)

#might err the first time
selected_name_last = ""
if os.path.exists("save.p"):
    if os.path.getsize("save.p") > 0:
        selected_name_last = pickle.load( open( "save.p", "rb" ) )

while selected_name == selected_name_last:
    selected_name = random.choice(names)

pickle.dump( selected_name, open( "save.p", "wb" ) )

#should write it and not use it next time (pickle)
color_list = list(pyfiglet.COLOR_CODES.keys())

color_list.remove('BLACK')
color_choice = pyfiglet.COLOR_CODES.keys
color_choice = random.choice(color_list)
font_list = pyfiglet.FigletFont.getFonts()
font_choice = random.choice(font_list)
print(selected_name, color_choice, font_choice)
pyfiglet.print_figlet(selected_name.upper(), font=font_choice, colors=color_choice)
