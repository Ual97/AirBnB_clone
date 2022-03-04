#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb)"
    classes = ["BaseModel", "User", "City", "Amenity",
               "Review", "State", "Place"]

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
            # Checking if class given exists in list of classes
            if elements == lines[0]:
                # If found, break the loop
                isfound = 0
                break
            else:
                # Continue until finds or iterates it all
                continue
        if isfound == 1:
            print("** class doesn't exist **")
        else:
            # Class exists, it'll be created and saved
            # finally being printed
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an
           instance based on the class name and id"""
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
                # No ID was passed
                print("** instance id missing **")
            else:
                id_list = []
                aux_list = []
                for key in storage.all().keys():
                    # Gets all ID's stored in keys.
                    aux_list = str(key).split(".")
                    # Format [class, ID], getting ID from list.
                    id_list.append(aux_list[1])
                for possibleid in id_list:
                    # Comparing ID given with ID's list.
                    if lines[1] == possibleid:
                        isfound = 0
                        break
                    else:
                        isfound = 1
                        continue
                if isfound == 1:
                    print("** no instance found **")
                else:
                    # If instance is found, get its str repr.
                    print(storage.all().get("{}.{}"
                                            .format(lines[0], lines[1])))

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
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
                    # Instance exist, so we'll just pop it from __obj
                    # and save changes.
                    storage.all().pop("{}.{}".format(lines[0], lines[1]), None)
                    storage.save()

    def do_all(self, line):
        """ Prints all string representation of
            all instances based or not on the class name.
        """
        lines = line.split()
        isfound = 1
        aux_list = []
        split_list = []
        print(lines[0])
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
            # If name of class is given, print only str of
            # those class instances.
            for key, value in storage.all().items():
                # Identifying instances with respective class name.
                split_list = str(key).split(".")
                if split_list[0] == lines[0]:
                    # When key is proper, gets str repr of value.
                    aux_list.append(str(value))
        else:
            # When no class name given, print all str repr
            for key, value in storage.all().items():
                aux_list.append(str(value))
        print(aux_list)

    def do_update(self, line):
        """Updates an instance based on the class name
           and id by adding or updating attribute
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
                print("** value missing **")
                return
            else:
                possiblekey = ""
                for key, values in storage.all().items():
                    try:
                        possiblekey = "{}.{}".format(lines[0], lines[1])
                        setattr(storage.all().get(possiblekey),
                                lines[2], lines[3])
                        storage.save()
                    except Exception:
                        continue

    def count(self):
        """ """
        pass

    def default(self, line):
        """ Another way to identify commands """
        auxlist = line.split(".")
        dictfun = {"all()": self.do_all, "count()": self.count,
                   "show()": self.do_show, "destroy()": self.do_destroy}
        try:
            dictfun.get(auxlist[1])(auxlist[0])
        except Exception:
            pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
