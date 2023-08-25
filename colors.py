import termcolor, os, time
import random

def colored_text(text, color):
    return termcolor.colored(text, color)

def bot_intro(color_list):
    for x in range(len(color_list)):
        os.system("cls")
        colored_text("PyChess By Coulter Stutz", color=color_list[x])
        time.sleep(1)