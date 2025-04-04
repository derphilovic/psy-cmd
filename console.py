#import modules
import os

#startup variables
i = 1
s = 0
c = 0
commands =  [ 'psy', 'help', 'exit', 'version', 'clear', 'newdir', 'godir', 'listdir', 'homedir', 'deldir' ]
commandslen = len(commands)
commandinfo = {
    'psy' : 'psy - displays psy-cmd logo',
    'help' : 'help - displays all commands',
    'exit' : 'exit - exits psy-cmd',
    'version' : 'version - displays the psy-cmd version',
    'clear' : 'clear - clears the screen',
    'newdir' : 'newdir - creates a new directory. Please don\'t enter the name of the dir with the command itself.',
    'godir' : 'godir - goes to a directory. Please don\'t enter the name of the dir with the command itself.',
    'listdir' : 'listdir - lists all directories and sub directories in the current directory',
    'homedir' : 'homedir - goes to the home directory',
    'deldir' : 'deldir - deletes a directory. Please don\'t enter the name of the dir with the command itself.',
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
vers = "psy-cmd 0.0.1"
#startup functions

if not os.path.exists('psy-data'):
    os.mkdir('psy-data')

os.chdir('psy-data')
psy_data_root = os.getcwd()

def get_truncated_path(start_folder):
    full_path = os.getcwd()
    index = full_path.find(start_folder)
    if index != -1:
        return full_path[index:]
    return full_path

rootpath = get_truncated_path('psy-data')
os.system('cls')
print(vers)
print(logo)
#main functions
while True:
    inputcmd = input("PSY:/" + rootpath + ">")
    inputcmd = inputcmd.strip()
    inputcmd = inputcmd.lower()
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
        for cmd in commands:
            print(commandinfo[cmd])
        c = 0

    #psy command
    if c == 1 and inputcmd == 'psy':
        print(logo)
        c = 0

    #exit command
    if c == 1 and inputcmd == 'exit':
        os.system('cls')
        exit()

    #version command
    if c == 1 and inputcmd == 'version':
        print(vers)
        c = 0

    #clear command
    if c == 1 and inputcmd == 'clear':
        os.system('cls')
        c = 0
    
    #newdir command
    if c == 1 and inputcmd == 'newdir':
        newdir = input("newdir: ")
        if os.path.exists(newdir):
            print("directory already exists")
        else:
            os.mkdir(newdir)
            print("new directory " + newdir + " created")
        c = 0

    #godir command
    if c == 1 and inputcmd == 'godir':
        targetdir = input("godir: ")
        if os.path.exists(targetdir):
            os.chdir(targetdir)
            print("changed directory to " + targetdir)
        else:
            print("directory not found")
    
    #listdir command
    if c == 1 and inputcmd == 'listdir':
        items = os.listdir()
        print("Contents of current directory:")
        for item in items:
            if os.path.isdir(item):
                print(f"[DIR] {item}")
                sub_items = os.listdir(item)
                for sub_item in sub_items:
                    path = os.path.join(item, sub_item)
                    if os.path.isdir(path):
                        print(f"  ├─[DIR] {sub_item}")
                    else:
                        print(f"  ├─[FILE] {sub_item}")
            else:
                print(f"[FILE] {item}")
        c = 0

    #homedir command
    if c == 1 and inputcmd == 'homedir':
        os.chdir(psy_data_root)
        print("changed directory to " + get_truncated_path('psy-data'))
        c = 0
    
    #deldir command
    if c == 1 and input == 'deldir':
        deldir = input("deldir: ")
        if os.path.exists(deldir):
            os.rmdir(deldir)
            print("deleted directory " + deldir)
        else:
            print("directory not found")
    

    #reset variables
    s = 0
    rootpath = get_truncated_path('psy-data')