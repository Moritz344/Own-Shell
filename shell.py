import os
import sys 

def remove_file(del_file):
     try:
          os.remove(del_file)
     except FileNotFoundError:
          print(f"No such file or directory")
     
def remove_directory(directory):
     try:
          os.rmdir(directory)
     except FileNotFoundError:
          print(f"{directory}: No such file or directory")


def create_directory(create_dir):
     try:
          os.makedirs(create_dir)
     except OSError:
          print("mkdir: cannot create directory ")
     

def cat_command(show_file):
     files = show_file
     try:
     # loop durch die datei
          for i in files:
               # öffnen und lesen der datei
               with open(i,"r") as file:
                    # zeige den inhalt
                    print(file.read())
     except FileNotFoundError:
          print(f"{i}: No such file or directory")
     except PermissionError:
          print(f"{i}: Permission denied")

def run_python_file(python_file):
     liste = ["python3"] + python_file
     os.execvp("python3",liste)     

def main():

     while True:
          sys.stdout.write("$ ")
          sys.stdout.flush()

          args = input().split()
          
          cmd = args[0]
          


          if cmd == "echo":
               print(" ".join(args[1:]))
          elif cmd == "pwd":
               pwd = os.getcwd()    
               print(pwd)
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



          elif cmd == "ls":
                   nummer = 0
                   for i in os.listdir():
                        nummer += 1
                        print(nummer,i)
          elif cmd == "cat":
               if len(args) > 1:
                    cat_command(args[1:])
          elif cmd == "clear":
               os.system("cls")
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
          else:
               print(f"{cmd}: command not found")
          

  



if __name__ == "__main__":
     main()    