import random
import time
from string import capwords
import json

from functions import (
  black,
  c_print,
  clear,
  dark_grey,
  light_gray,
  magenta,
  purple,
  t_print,
  white,
  yellow,
)


class ChatBot():
  def __init__(self):
    self.name = "RetailBot"
    self.phrases = [f"{purple}I hope that helped!", 
                    f"{purple}Can I assist you further?",
                    f"{purple}Is there anything else you might want to know?"]
    
    self.questions = [
                      {'question': "What does our store sell?",
                       'answer': "Our store sells Yogurt, Rice, Fish and More!"}, 
                      {'question': "How much do our items cost?", 
                       'answer': "Each of our items cost 1 Dollar!"}, 
                      {'question': "What are our work hours?", 
                       'answer': "Each of our employs work from 9 AM to 5 PM!"},
                      {'question': "What are our customer reviews?",
                       'answer': "We are rated at 4 stars globally!"},
                      {'question': "What are out return policies?", 
                       'answer': "We allow anything to be returned within a week!"},
                      {'question': "Exit.",
                       'answer': "Thank you for your time!"}
    ]
  def chat(self):
    response = random.choice(self.phrases)
    print(response)

class User():
  def __init__(self, name, age):
    self.name = name
    self.age = age

def print_options():
  print(f"{dark_grey}-----------------------------------{white}")
  for i, question in enumerate(robot.questions, start=1):
    print(f"{yellow}{i}{white}: {question['question']}")
  print(f"{dark_grey}-----------------------------------{white}")

robot = ChatBot()

t_print(f"{magenta}Hello, this is RetailBot, your personal Chat Bot!\n\n")
  
time.sleep(0.3)

while True:
  try:
    user_age = int(input(f"{light_gray}How old are you?\n{light_gray}>"))
    if user_age <= 4 or user_age > 100:
      clear()
      continue
    break
  except ValueError:  
    clear()
    continue
    
clear()

while True:
  user_name = capwords(input(f"{light_gray}What is your name?\n{light_gray}>")) 
  x = user_name.replace(" ", "")
  if not x.isalpha():
    clear()
    print(f"{magenta}Sorry, {user_name} is not a valid name. Please try again.\n")
  elif len(x) > 15:
    clear()
    print(f"{magenta}Name is too long, please try again.\n")
  elif len(x) < 3:
    clear()
    print(f"{magenta}Name is too short, please try again.\n")
  else:
     break


clear()

print(f"{light_gray}How can I help you {user_name}?{white}\n")

user = User(user_name, user_age)
userJSON = json.dumps(user.__dict__, indent=4)

time.sleep(3)

while True:
  print_options()
  print("")
  
  try:
    choice = int(input(f"{white}Enter your choice: {white}"))
    selected_question = robot.questions[choice - 1]
  except (ValueError, IndexError):
    clear()
    print("Invalid.")
    continue
  
  robot.questions.remove(selected_question)
  
  clear()
  print(f"{light_gray}{selected_question['question']}{white}\n")
  print(f"{black}---------------------------------")
  print(f"\n{white}{selected_question['answer']}")

  if selected_question['question'] == 'Exit.':
    exit()


  print("")
  ChatBot.chat(robot)
  input(f"\n{black}Press enter to continue.\n>")

  clear()

  


#https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string


          
    