import sys
import os
import subprocess

def find_path(cmd):
    paths = os.environ.get("PATH","").split(os.pathsep)
    for path in paths:
        executable_path = os.path.join(path,cmd)
        if os.path.isfile(executable_path) and os.access(executable_path,os.X_OK):
            #print(f"{cmd} is {executable_path}")
            
            return executable_path
    return None
    #print(f"{cmd} not found")

def execute_command(args):
    try:
        parts = args.split()
        program = parts[0]
        args_1 = parts[1:]
        # Find program path
        program_path = find_path(program)
        

        # execute program
        if program_path:
            result = subprocess.run([program_path] + args_1,capture_output=True,text=True)
            print(result.stdout,end="")
        else:
            
            print(f"{program}: command not found")
    except Exception as e:
        print(f"Error: {e}")

def main():
    

    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
       
        args = command.split()
        cmd = args[0]

    
        
        builtin = ["echo","exit","type",]
        
        

        

        if cmd == "exit":
            sys.exit(int(args[1]))

        elif cmd == "echo":
            print(" ".join(args[1:]))
        elif cmd == "type":
            for arg in args[1:]:
                if arg in builtin:
                    print(f"{arg} is a shell builtin")
                else:
                    path = find_path(arg)
                    if path:
                        print(f"{arg} is {path}")
                    else:
                        print(f"{arg} not found")
        elif cmd == "pwd":
            pwd = os.getcwd()
            print(pwd)
            
        else:
            execute_command(command)
        
        
      
     

if __name__ == "__main__":
    main()
   
