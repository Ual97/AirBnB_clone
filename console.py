#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd
from logging import exception
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
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
        """Creates new instance of BaseModel,
        saves it to JSON file and prints id"""
        lines = line.split()
        isfound = 0
        if len(line) == 0:
            print("** class name missing **")
            return
        for elements in HBNBCommand.classes:
            if elements == lines[0]:
                isfound = 0
                break
            else:
                continue
        if isfound == 1:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        lines = line.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            isfound = 1
            for elements in HBNBCommand.classes:
                if elements == lines[0]:
                    isfound = 0
                    break
                else:
                    continue
            if isfound == 1:
                print("** class doesn't exist **")
            if len(lines) == 1:
                print("** instance id missing **")
            else:
                id_list = []
                aux_list = []
                for key in storage.all().keys():
                    aux_list = str(key).split(".")
                    id_list.append(aux_list[1])
                for possibleid in id_list:
                    if lines[1] == possibleid:
                        isfound = 0
                        break
                    else:
                        isfound = 1
                        continue
                if isfound == 1:
                    print("** no instance found **")
                else:
                    print(storage.all().get(f"{lines[0]}.{lines[1]}"))

    def do_destroy(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        lines = line.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            isfound = 1
            for elements in HBNBCommand.classes:
                if elements == lines[0]:
                    isfound = 0
                    break
                else:
                    continue
            if isfound == 1:
                print("** class doesn't exist **")
            if len(lines) == 1:
                print("** instance id missing **")
            else:
                id_list = []
                aux_list = []
                for key in storage.all().keys():
                    aux_list = str(key).split(".")
                    id_list.append(aux_list[1])
                for possibleid in id_list:
                    if lines[1] == possibleid:
                        isfound = 0
                        break
                    else:
                        isfound = 1
                        continue
                if isfound == 1:
                    print("** no instance found **")
                else:
                    storage.all().pop(f"{lines[0]}.{lines[1]}", None)
                    storage.save()
    
    def do_all(self, line):
        """ """
        lines = line.split()
        isfound = 1
        aux_list = []
        split_list = []
        if len(lines) != 0:
            for elements in HBNBCommand.classes:
                if elements == lines[0]:
                    isfound = 1
                    break
                else:
                    isfound = 0
                    continue
        if isfound == 0:
            print("** class doesn't exist **")
            return
        if len(lines) == 1:
            for key, value in storage.all().items():
                split_list = str(key).split(".")
                if split_list[0] == lines[0]:
                    aux_list.append(str(value))
        else:
            for key, value in storage.all().items():
                aux_list.append(str(value))
        print(aux_list)

    def do_update(self, line):
        """
        """
        lines = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        else:
            isfound = 1
            for elements in HBNBCommand.classes:
                if elements == lines[0]:
                    isfound = 0
                    break
                else:
                    continue
            if isfound == 1:
                print("** class doesn't exist **")
                return
            if len(lines) == 1:
                print("** instance id missing **")
                return
            id_list = []
            aux_list = []
            for key in storage.all().keys():
                aux_list = str(key).split(".")
                id_list.append(aux_list[1])
            for possibleid in id_list:
                if lines[1] == possibleid:
                    isfound = 0
                    break
                else:
                    isfound = 1
                    continue
            if isfound == 1:
                print("** no instance found **")
                return
            elif len(lines) == 2:
                print("** attribute name missing **")
                return
            elif len(lines) == 3:
                print ("** value missing **")
                return
            else:
                possiblekey = ""
                for key, values in storage.all().items():
                    try:
                        possiblekey = f"{lines[0]}.{lines[1]}"
                        setattr(storage.all().get(possiblekey), lines[2], lines[3])
                        storage.save()
                    except Exception:
                        continue

if __name__ == "__main__":
    HBNBCommand().cmdloop()
