#import modules
import os

#setup variables

logo = """                                                __      
                                               /\ \__   
 _____     ____  __  __             ___      __\ \ ,_\  
/\ '__`\  /',__\/\ \/\ \  _______ /' _ `\  /'__`\ \ \/  
\ \ \L\ \/\__, `\ \ \_\ \/\______\/\ \/\ \/\  __/\ \ \_ 
 \ \ ,__/\/\____/\/`____ \/______/\ \_\ \_\ \____\\\ \__\\
  \ \ \/  \/___/  `/___/> \        \/_/\/_/\/____/ \/__/
   \ \_\             /\___/                             
    \/_/             \/__/                              

"""
commands = ['help', 'exit', 'client', 'server']
commandlen = len(commands)
commandhelp = {
    'help' : 'help - List all commands',
    'exit' : 'exit - Exits psy-net',
    'client' : 'client - Starts a client',
    'server' : 'server - Starts a server'
}
c = 0
s = 0

#startup functions
os.system('cls')
print(logo)
print("psy-net v1.0.0")
print("type 'help' for help")

#main functions
while True:
    inputnet = input("net-cmd> ")
    inputnet = inputnet.strip()
    inputnet = inputnet.lower()
    while c < commandlen:
        if inputnet == commands[c]:
            s = 1
        else:
            if s != 1:
                s = 0
        c = c + 1

    if s != 1:
            print("command not found")

    #exit command
    if inputnet == "exit":
        os.system('cls')
        exit()
        s = 0

    #help command
    if inputnet == "help":
        for cmd in commands:
            print(commandhelp[cmd])
        s = 0

    #client command
    if inputnet == "client":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        client_path = os.path.join(script_dir, "client.py")
        if os.path.exists(client_path):
            os.system(f'py "{client_path}"')
        else:
            print("Error: client.py not found")
        s = 0

    #server command
    if inputnet == "server":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        server_path = os.path.join(script_dir, "server.py")
        if os.path.exists(server_path):
            os.system(f'py "{server_path}"')
        else:
            print("Error: server.py not found")
        s = 0

    
    #reset variables
    c = 0