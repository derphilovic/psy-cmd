#import modules
import os

#setup variables

logo = """
                                                __      
                                               /\ \__   
 _____     ____  __  __             ___      __\ \ ,_\  
/\ '__`\  /',__\/\ \/\ \  _______ /' _ `\  /'__`\ \ \/  
\ \ \L\ \/\__, `\ \ \_\ \/\______\/\ \/\ \/\  __/\ \ \_ 
 \ \ ,__/\/\____/\/`____ \/______/\ \_\ \_\ \____\\ \__\\
  \ \ \/  \/___/  `/___/> \        \/_/\/_/\/____/ \/__/
   \ \_\             /\___/                             
    \/_/             \/__/                              

"""

#startup functions
os.system('cls')
print(logo)

while True:
    inputnet = input("net-cmd> ")

    

    if inputnet == "exit":
        os.system('cls')
        exit()