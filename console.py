#import modules
import os
import time
os.system('cls')
os.system('color')
#startup variables
i = 1
s = 0
c = 0
commands =  [ 'psy', 'help', 'exit', 'version', 'clear', 'newdir', 'godir', 'listdir', 'homedir', 'deldir', 'color', 'newfile' ]
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
    'color' : 'color - changes the color of the console',
    'newfile' : 'newfile - creates a new file. Please don\'t enter the name of the file with the command itself.'
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

colors = {
    'white' : '07',
    'red' : '04',
    'green' : '02',
    'yellow' : '06',
    'blue' : '01',
    'magenta' : '05',
    'cyan' : '03',
    'gray' : '08',
}
z = 0
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
        
        def print_directory_tree(directory, prefix=""):
            try:
                items = os.listdir(directory)
                if not items:
                    return
                for i, item in enumerate(items):
                    path = os.path.join(directory, item)
                    is_last_item = i == len(items) - 1
                    connector = "└─" if is_last_item else "├─"
                    
                    if os.path.isdir(path):
                        print(f"{prefix}{connector}[DIR] {item}")
                        next_prefix = prefix + ("    " if is_last_item else "│   ")
                        print_directory_tree(path, next_prefix)
                    else:
                        print(f"{prefix}{connector}[FILE] {item}")
            except PermissionError:
                print(f"{prefix}├─[ACCESS DENIED]")
            except Exception as e:
                print(f"{prefix}├─[ERROR: {str(e)}]")
        for item in items:
            if os.path.isdir(item):
                print(f"[DIR] {item}")
                print_directory_tree(item, "  ")
            else:
                print(f"[FILE] {item}")
        c = 0


    #homedir command
    if c == 1 and inputcmd == 'homedir':
        os.chdir(psy_data_root)
        print("changed directory to " + get_truncated_path('psy-data'))
        c = 0
    
    #deldir command
    if c == 1 and inputcmd == 'deldir':
        deldir = input("deldir: ")
        if os.path.exists(deldir):
            os.rmdir(deldir)
            print("deleted directory " + deldir)
        else:
            print("directory not found")
        c = 0
    
    #color command
    if c == 1 and inputcmd == 'color':
        print("Available colors:")
        for color in colors:
            print(color)
        color = input("color: ")
        if color in colors:
            os.system('color ' + colors[color])
            print("color set to " + color)
        elif color == 'rainbow':
            while z < 20:
                print(logo)
                for color in colors:
                    os.system('color ' + colors[color])
                    time.sleep(0.1)
                z = z + 1
            os.system('color 07')
        else:
            print("color not found")
        c = 0

        #newfile command
    if c == 1 and inputcmd == 'newfile':
        newfile = input("newfile: ")
        fileext = input("file extension: ")
        if os.path.exists(newfile + '.' + fileext):
            print("file already exists")
        else:
            open(newfile + '.' + fileext, 'w').close()
            print("new file " + newfile + '.' + fileext + " created")
        c = 0

    #reset variables
    s = 0
    rootpath = get_truncated_path('psy-data')