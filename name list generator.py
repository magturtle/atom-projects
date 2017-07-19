import time
import random

girl_name = [ "Lily", "Grace", "Nancy", "Amy", "Paige", "Nicole", "Paiton", "Jan", "Mia", "Riley", "Piper", "Emery", "Margaret", "Anastasia"]
boy_name = ["Peter", "Noah", "Mason", "Lucas", "Oliver", "James", "Benjamin", "Logan", "Daniel", "Phillip", "William", "Owen", "Henry", "Nathan", "Pascal"]

while True:
    user_input = input ("type 'boy' or 'girl':  ")
    if user_input == "boy":
        print (random.choice(boy_name)+ "\n")
    elif user_input == "girl":
        print (random.choice(girl_name)+ "\n")
