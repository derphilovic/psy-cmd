#import modules
import os
import time
import random
import shutil
import datetime
os.system('cls')
os.system('color')
#startup variables
i = 1
s = 0
c = 0
commands =  [ 'psy', 'help', 'exit', 'version', 'clear', 'newdir', 'godir', 'listdir', 'homedir', 'deldir', 'color', 'newfile', 'number-game', 'echo', 'delfile', 'readfile', 'editfile',
              'run', 'calc', 'net', 'install', 'time', 'sysinfo', 'timer', 'uptime']
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
    'newfile' : 'newfile - creates a new file. Please don\'t enter the name of the file with the command itself.',
    'number-game' : 'number-game - plays a number guessing game',
    'echo' : 'echo - repeats your input',
    'delfile' : 'delfile - deletes a file. Please don\'t enter the name of the file with the command itself.',
    'readfile' : 'readfile - reads a file. Please don\'t enter the name of the file with the command itself.',
    'editfile' : 'editfile - edits a file. Please don\'t enter the name of the file with the command itself.',
    'run' : 'run - runs a file. Please don\'t enter the name of the file with the command itself.',
    'calc' : 'calc - opens psy-calc',
    'net' : 'net - opens psy-net',
    'install' : 'install - installs a python program',
    'time' : 'time - gives you the time',
    'sysinfo' : 'sysinfo',
    'timer' : 'timer - makes an timer',
    'uptime' : 'uptime'
}

logo = """                                                       __     
                                                      /\\ \\    
 _____     ____  __  __             ___    ___ ___    \\_\\ \\   
/\\ '__`\\  /',__\\/\\ \\/\\ \\  _______  /'___\\/' __` __`\\  /'_` \\  
\\ \\ \\L\\ \\/\\__, `\\ \\ \\_\\ \\/\\______\\/\\ \\__//\\ \\/\\ \\/\\ \\/\\ \\L\\ \\ 
 \\ \\ ,__/\\/\\____/\\/`____ \\/______/\\ \\____\\ \\_\\ \\_\\ \\_\\ \\___,_\\ 
  \\ \\ \\/  \\/___/  `/___/> \\        \\/____/\\/_/\\/_/\\/_/\\/__,_ / 
   \\ \\_\\             /\\___/                                   
    \\/_/             \\/__/                                    """

logo2 = """                                 __                   __      
                                /\ \__               /\ \__   
 _____     ____  __  __         \ \ ,_\    __   __  _\ \ ,_\  
/\ '__`\  /',__\/\ \/\ \  _______\ \ \/  /'__`\/\ \/'\\\ \ \/  
\ \ \L\ \/\__, `\ \ \_\ \/\______\\\ \ \_/\  __/\/>  </ \ \ \_ 
 \ \ ,__/\/\____/\/`____ \/______/ \ \__\ \____\/\_/\_\ \ \__\\
  \ \ \/  \/___/  `/___/> \         \/__/\/____/\//\/_/  \/__/
   \ \_\             /\___/                                   
    \/_/             \/__/                                    """
vers = "psy-cmd 0.1.0"
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
randnum = 0
timerCurrent = 0
wantedTimer = 0
#startup functions

if not os.path.exists('psy-data'):
    os.mkdir('psy-data')

if not os.path.exists('psy-extensions'):
    print("Critical Error: psy-extensions not found. Please reinstall psy-cmd.")
    time.sleep(10)
    exit()

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
            shutil.rmtree(deldir)
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

    #numbergame command
    if c == 1 and inputcmd == 'number-game':
        numberguess = input("Name a number between 1 and 10: ")
        randnum = random.randint(1, 10)
        try:
            numberguess = int(numberguess)
            if numberguess == randnum:
                print("you won!")
            else:
                print("you lose!")
                print("better luck next time!")
                print(f"The number was: {randnum}")
        except ValueError:
            print("That's not a valid number!")
        c = 0
    
    #echo
    if c == 1 and inputcmd == 'echo':
        echo = input("echo: ")
        print(echo)
        c = 0

    #delfile command
    if c == 1 and inputcmd == 'delfile':
        delfile = input("delfile: ")
        if os.path.exists(delfile):
            os.remove(delfile)
            print("deleted file " + delfile)
        else:
            print("file not found")
        c = 0

    #readfile command
    if c == 1 and inputcmd == 'readfile':
        readfile = input("readfile: ")
        if os.path.exists(readfile):
            with open(readfile, 'r') as f:
                content = f.read()
                print("⌄⌄⌄⌄⌄⌄")
                print(content)
                print("⌃⌃⌃⌃⌃⌃")
        else:
            print("file not found")
        c = 0
    
    #editfile command
    if c == 1 and inputcmd == 'editfile':
        editfile = input("editfile: ")
        if os.path.exists(editfile):
            with open(editfile, 'r') as f:
                content = f.read()
            os.system('cls')
            lines = content.split('\n')
            print(logo2)
            print("Commands:")
            print("  :wq - Save and quit")
            print("  :q  - Quit without saving")
            print("  :n  - Go to line number n (e.g., :5)")
            print("  :l  - List all lines")
            print("  :h  - Shows all commands")
            
            current_line = 0
            total_lines = len(lines)
            # Function to display all lines with line numbers
            def display_lines():
                print("\nFile content:")
                for i, line in enumerate(lines):
                    print(f"{i+1:3d}| {line}")
                print()
            # Initial display
            display_lines()
            while True:
                # Show current line position
                if current_line < total_lines:
                    prompt = f"[{current_line+1}/{total_lines}]> "
                    current_content = lines[current_line]
                    print(f"Current line: {current_content}")
                else:
                    prompt = f"[{current_line+1}/new]> "
                    current_content = ""
                # Get user input
                user_input = input(prompt)
                # Process commands
                if user_input == ':wq':
                    # Save and quit
                    with open(editfile, 'w') as f:
                        f.write('\n'.join(lines))
                    print(f"File {editfile} saved successfully.")
                    break
                elif user_input == ':q':
                    # Quit without saving
                    print(f"Exited without saving changes to {editfile}.")
                    break
                elif user_input == ':l':
                    # List all lines
                    display_lines()
                elif user_input == ':h':
                    # Show help
                    print("\nCommands:")
                    print("  :wq - Save and quit")
                    print("  :q  - Quit without saving")
                    print("  :n  - Go to line number n (e.g., :5)")
                    print("  :l  - List all lines")
                    print("  :h  - Show help")
                    print("  :u  - Move up one line")
                    print("  :d  - Move down one line")
                    print()
                elif user_input == ':u':
                    # Move up one line
                    if current_line > 0:
                        current_line -= 1
                    else:
                        print("Already at the first line.")     
                elif user_input == ':d':
                    # Move down one line
                    if current_line < total_lines:
                        current_line += 1
                    else:
                        print("At the end of the file. Adding a new line.")
                        lines.append("")
                        total_lines += 1
                        current_line = total_lines - 1
                elif user_input.startswith(':') and user_input[1:].isdigit():
                    # Go to specific line
                    line_num = int(user_input[1:])
                    if 1 <= line_num <= total_lines:
                        current_line = line_num - 1
                    elif line_num == total_lines + 1:
                        # Allow adding a new line at the end
                        lines.append("")
                        total_lines += 1
                        current_line = total_lines - 1
                    else:
                        print(f"Line number out of range. Valid range: 1-{total_lines+1}")
                        
                else:
                    # Edit the current line
                    if current_line < total_lines:
                        lines[current_line] = user_input
                    else:
                        lines.append(user_input)
                        total_lines += 1
                    
                    # Automatically move to the next line after editing
                    if current_line < total_lines:
                        current_line += 1
        else:
            print("file not found")
        c = 0

    #run command
    if c == 1 and inputcmd == 'run':
        run = input("file to run: ")
        if os.path.exists(run):
            os.system(run)
        else:
            print("file not found")
        c = 0

    #calc command
    if c == 1 and inputcmd == 'calc':
        print("Psy-Calc")
        print("Following Commands are available:")
        print("(+) Addition")
        print("(-) Subtraction")
        print("(/) Division")
        print("(*) Multiplication")
        calc = input("calc: ")
        try:
            result = eval(calc)
            print(result)
        except Exception as e:
            print("Error:", e)
        c = 0

    #net command
    if c == 1 and inputcmd == 'net':
        # Get the parent directory of psy_data_root
        parent_dir = os.path.dirname(psy_data_root)
        extension_path = os.path.join(parent_dir, 'psy-extensions', 'net.py')
        if os.path.exists(extension_path):
            os.system(f'py "{extension_path}"')
        else:
            print("net.py not found please reinstall psy-cmd")
        c = 0

    #install command
    if c == 1 and inputcmd == 'install':
        install = input("Python script to install (with extensions): ")
        if os.path.exists(install):
            modules_to_install = set()
            try:
                with open(install, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('import'):
                            module = line.replace('import', '', 1).strip().split()[0].split('.')[0]
                            modules_to_install.add(module)
                        elif line.startswith('from'):
                            parts = line.split()
                            if len(parts) >= 2:
                                module = parts[1].split('.')[0]
                                modules_to_install.add(module)
                if modules_to_install:
                    print(f"Found {len(modules_to_install)} modules to install: {', '.join(modules_to_install)}")
                    confirm = input("Proceed with installation? (y/n): ")
                    if confirm.lower() == 'y':
                        for module in modules_to_install:
                            print(f"Installing {module}...")
                            os.system(f'py -m pip install {module}')
                        print("Installation complete!")
                    else:
                        print("Installation cancelled.")
                else:
                    print("Error: No modules to install found in the file.")
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print("Error: File not found.")
        c = 0

    #time command
    if c == 1 and inputcmd == 'time':
        timedate = datetime.datetime.now()
        print(timedate)
        c = 0

    #timer command
    if c == 1 and inputcmd == 'timer':
        wantedTimer = input("Timer length(seconds): ")
        wantedTimer = int(wantedTimer)
        time.sleep(wantedTimer)
        print("Timer over!")
        c = 0

    #reset variables
    s = 0
    rootpath = get_truncated_path('psy-data')