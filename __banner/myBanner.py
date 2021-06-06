import colorama
import random
import sys

def bannerTop():
    banner = '''
 
 Edu Mail Creator By Aamir 
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)