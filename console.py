#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb)"
    classes = {"BaseModel"}

    def do_EOF(self, line):
        """handles EOF"""
        print()
        return True
    
    def do_quit(self, line):
        """handles quit"""
        return True

    def emptyline(self):
        """if emptyline, do nothing"""
        pass
    
    def do_create(self, line):
        """Creates new instance of BaseModel, saves it to JSON file and prints id"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print (new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            lines = line.split()
            if lines[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(lines) > 1:
                if lines[1] not in storage.all().keys():
                    print("** instance id missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()