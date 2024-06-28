```
$ 
```

# Custom Shell Script
This Python script implements a basic shell environment that supports several common shell commands. It utilizes the os and sys modules to perform file and directory operations, and the termcolor module for colored terminal output.

# Features
- Echo command: echo [text] - Prints the specified text to the terminal.
- Print working directory: pwd - Displays the current directory.
- Type command: type [command] - Indicates whether the given command is a shell builtin or not.
- Exit command: exit - Exits the shell.
- Change directory: cd [path] - Changes the current directory to the specified path.
- List directory contents: ls - Lists the contents of the current directory.
- Concatenate and display files: cat [file1 file2 ...] - Displays the content of the specified files.
- Clear screen: clear - Clears the terminal screen.
- Remove directory: rmdir [directory] - Removes the specified directory.
- Remove file: rm [file] - Removes the specified file.
- Make directory: mkdir [directory] - Creates a new directory.
- Run Python file: python3 [file.py] - Executes the specified Python file.
- Who am I: whoami - Prints the current user's username.

# Usage
```
git clone https://github.com/yourusername/your-repo-name.git
```

# Example Commands

```
$ echo Hello, World!
Hello, World!

$ pwd
/path/to/current/directory

$ cd /path/to/directory
$ ls
1 file1.txt
2 file2.txt

$ cat file1.txt
This is the content of file1.txt

$ mkdir new_directory
$ rmdir new_directory

$ rm file1.txt

$ python3 script.py

$ whoami
Bob123
```
