#Uses random package to give fortune
#has 5 different fortunes
import random
name = input("For a fortune please enter your name: ")
fortune = random.randrange (4)

if fortune == 0:
        print("You will live a happy life")

elif fortune == 1:
        print("You will become wealthy")

elif fortune == 2:
        print("You will past all your test")

elif fortune == 3:
        print("Your dog will live forever")

elif fortune == 4:
        print("You will recieve a dollar bill")
print("Your fortune might come true",name)

input("\n\nPress the enter key to exit.")
