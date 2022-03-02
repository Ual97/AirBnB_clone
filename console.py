#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd
from logging import exception
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb)"
    classes = ["BaseModel", "User"]

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
        lines = line.split()
        print(lines)
        if len(line) == 0:
            print("** class name missing **")
        else:
            if len(lines) == 1:
                print(len(lines))
                isfound = 1
                for elements in HBNBCommand.classes:
                    if elements == lines[1]:
                        isfound = 0
                        break
                    else:
                        continue
                if isfound == 1:
                    print("** class doesn't exist **")
            elif len(lines) == 1:
                print("** instance id missing **")
            else:
                id_list = []
                aux_list = []
                for key in storage.all().keys():
                    aux_list = str(key).split(".")
                    id_list.append(aux_list[1])
                    aux_list.clear()
                for possibleid in id_list:
                    if lines[1] == possibleid:
                        isfound = 0
                        break
                    else:
                        isfound = 1
                        continue
                if isfound == 1:
                    print("** no instance found **")                    
                



if __name__ == "__main__":
    HBNBCommand().cmdloop()