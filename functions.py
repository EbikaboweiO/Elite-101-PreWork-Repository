import os
import sys
import time
import textwrap

green = "\u001b[32m"
dark_yellow = "\u001b[33m"
blue = "\u001b[34m"
red = "\u001b[31m"
magenta = "\u001b[35m"
gray = "\u001b[30m" 
white = "\u001b[37m"
black = "\033[0;30m"
brown = "\033[0;33m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
light_gray = "\033[0;37m"
dark_grey = "\033[1;30m"
light_red = "\033[1;31m"
light_green = "\033[1;32m"
yellow = "\033[1;33m"
light_blue = "\033[1;34m"
light_purple = "\033[1;35m"
light_cyan = "\033[1;36m"
light_white = "\033[1;37m"

def clear():
  os.system('clear')

def t_print(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

def c_print(text):
  wrapstring = textwrap.wrap(text, width=70)
  for line in wrapstring:
      # print(line)
      print('{:^70}'.format(line))