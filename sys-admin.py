"""
Your module description
"""

# using os.system :: several Bash commmands from Python
import os
os.system("ls")

# uing subprocess.run :: spawn new processes
# include additional args
import subprocess
subprocess.run(["ls", "-l", "README.md"])

# retrieving sys info
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# retrieving info about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information command: {command} {commandArgument}')
subprocess.run([command,commandArgument])