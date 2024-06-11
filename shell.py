import os
import sys
from termcolor import cprint,colored
import time
import subprocess

def remove_file(del_file):
     try:
          os.remove(del_file)
     except FileNotFoundError:
          print(f"{del_file}: No such file or directory")
     
def remove_directory(directory):
     try:
          os.rmdir(directory)
     except FileNotFoundError:
          print(f"{directory}: No such file or directory")


def create_directory(create_dir):
     try:
          os.makedirs(create_dir)
     except OSError:
          cprint("mkdir: cannot create directory ","red",attrs=["bold"])
def cat_command(show_file):
     files = show_file
     try:
     # loop durch die datei
          for i in files:
               # öffnen und lesen der datei
               with open(i,"r") as file:
                    # zeige den inhalt
                    cprint(file.read(),"white")
     except FileNotFoundError:
          print(f"{i}: No such file or directory")
     except PermissionError:
          print(f"{i}: Permission denied")
     except OSError:
          print(f"{i}: Invalid argument")

def run_python_file(python_file):
     liste = ["python3"] + python_file
     os.execvp("python3",liste)
      

def main():
     while True:
          path = os.getcwd()
          print(colored(path,"yellow"))
          sys.stdout.write("$ ")
          sys.stdout.flush()
          command = input()
          args = command.split()
          try:
               cmd = args[0]
          except IndexError:
               continue
          


          if cmd == "echo":
               print(" ".join(args[1:]))
          elif cmd == "pwd":
               pwd = os.getcwd()    
               print(pwd)
               return pwd
          elif cmd == "type":
               if len(cmd) > 1:
                    for arg in args[1:]:
                         if args[1] in ["type","echo","exit"]:
                              print(f"{arg} is a shell builtin")
                         else:
                              print(f"{arg} not found")
          elif cmd == "exit":
               sys.exit(0)
          elif cmd == "cd":
               if len(args) > 1:
                    path = args[1]
                    if path == "~":
                         path = os.path.expanduser("~")
                    try:
                         os.chdir(path)
                    except FileNotFoundError:
                         print(f"{args[1]}: No such file or directory")
        
          elif cmd == "file":
                # subprocess-Moduls werden verwendet um einen externen Befehl in einem neuen Prozess auszuführen
                # capture_output=True: Diese Option erfasst die Ausgabe (stdout und stderr) des ausgeführten Befehls.
                # text=True: Diese Option sorgt dafür, dass die Ausgabe als String und nicht als Bytes zurückgegeben wird.
                # check=True: Diese Option bewirkt, dass eine Ausnahme (subprocess.CalledProcessError) ausgelöst wird, wenn der Befehl                  mit einem nicht-null Rückgabewert (Fehler) beendet wird.
                try:
                    result = subprocess.run(['file', args[1]], capture_output=True, text=True, check=True)
                    result = result.stdout.strip()
                    print(result)
                except IndexError:
                    print("im here :c (IndexError)")
    
          elif cmd == "ls":
                   nummer = 0
                   nummer_farbe = "yellow"
                   datei_farbe = "blue" 
                   for i in os.listdir():
                        nummer += 1
                        print(colored(f"{nummer}",nummer_farbe),colored(i,datei_farbe))

          elif cmd == "cat":
               if len(args) > 1:
                    cat_command(args[1:])
          elif cmd == "clear":
               os.system("clear")
          elif cmd == "rmdir":
               if len(args) > 1:
                    remove_directory(args[1])
          elif cmd == "rm":
               if len(args) > 1:
                    remove_file(args[1])
          elif cmd == "mkdir":
               if len(args) > 1:
                    create_directory(args[1])
          elif cmd == "python3":
               run_python_file(args[1:])
               time.sleep(1)
               
          elif cmd == "whoami":
               whoami = os.getlogin()
               print(whoami)
               
          else:
               print(f"{cmd}: command not found")
     

if __name__ == "__main__":
     main() 