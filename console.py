#import modules
import os

#startup variables
i = 1
s = 0
c = 0
commands =  [ 'psy', 'help', 'exit', 'version' ]
commandslen = len(commands)
commandinfo = {
    'psy' : 'psy - displays psy-cmd logo',
    'help' : 'help - displays all commands',
    'exit' : 'exit - exits psy-cmd',
    'version' : 'version - displays the psy-cmd version'
}

logo = """                                                        __     
                                                      /\\ \\    
 _____     ____  __  __             ___    ___ ___    \\_\\ \\   
/\\ '__`\\  /',__\\/\\ \\/\\ \\  _______  /'___\\/' __` __`\\  /'_` \\  
\\ \\ \\L\\ \\/\\__, `\\ \\ \\_\\ \\/\\______\\/\\ \\__//\\ \\/\\ \\/\\ \\/\\ \\L\\ \\ 
 \\ \\ ,__/\\/\\____/\\/`____ \\/______/\\ \\____\\ \\_\\ \\_\\ \\_\\ \\___,_\\ 
  \\ \\ \\/  \\/___/  `/___/> \\        \\/____/\\/_/\\/_/\\/_/\\/__,_ / 
   \\ \\_\\             /\\___/                                   
    \\/_/             \\/__/                                    """
#startup functions

if not os.path.exists('psy-data'):
    os.mkdir('psy-data')

os.chdir('psy-data')

def get_truncated_path(start_folder):
    full_path = os.getcwd()
    index = full_path.find(start_folder)
    if index != -1:
        return full_path[index:]
    return full_path

rootpath = get_truncated_path('psy-data')

#main functions
if i == 1:
    inputcmd = input("PSY:/" + rootpath + ">")
    i = 0

while s < commandslen:
    if inputcmd == commands[s]:
        c = 1
    else:
        if c != 1:
            c = 0
    s = s + 1

if c != 1:
    print("command not found")

#commands

#help command
if c == 1 and inputcmd == 'help':
    print(commandinfo['psy'])
    print(commandinfo['help'])
    print(commandinfo['exit'])
    print(commandinfo['version'])

#psy command
if c == 1 and inputcmd == 'psy':
    print(logo)

#exit command
if c == 1 and inputcmd == 'exit':
    exit()