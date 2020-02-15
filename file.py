# How to create and write a file- A very common use case for working with the files system is to log values.


file_builder = open("logger.txt", "w+") # calling open will open the file if it exists, but if it doesn't exisit it will create it. 1st argument is the file and the 2nd argument is how you want to open it.

for i in range(1000):
    file_builder.write(f"I'm on line {i + 1}\n") # +1 so it doesn't start at 0


# file_builder.write("Hey, I'm in a file!")           write is a function

file_builder.close()

# this is how to temp overide
# One of the elements I want you to truly remember is that if you use this syntax, where you're opening a file and you're simply calling right you will overwrite all of the content in that file.

# ------------------

# using regular expressions to list file types
# regular expressions give you the ability to match patterns

import fnmatch # built in python
from fnmatch import fnmatchcase
import os # operating system

# working with files
def list_files():
    for file in os.listdir('.'): # argument the dir that you want . would be current dir
        if fnmatch.fnmatch(file, '*.txt'): # 1st argument is the file name 2nd argument is the type of file. * means we don't care what is before it
            print('Text files:', file, "\b")

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()
# going through a list
players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)

# ----------------

