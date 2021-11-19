from encoder import enco
from decoder import deco

base64_text = enco("EMSE.png") # you encode the image

quest = input("Would you like to decode the previous photo? (Y/n) : ")
if quest == "Y" or quest == "y":
    deco(base64_text)