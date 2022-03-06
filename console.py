#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "City", "Amenity",
               "Review", "State", "Place"]

    def do_create(self, line):
        """Creates new instance of BaseModel,
        saves it to JSON file and prints id"""
        lines = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        if not self.inclasslist(lines):
            print("** class doesn't exist **")
            return
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
        print(lines)
        if len(line) == 0:
            print("** class name missing **")
            return
        else:
            if not self.inclasslist(lines):
                print("** class doesn't exist **")
                return
            if len(lines) == 1:
                # No ID was passed
                print("** instance id missing **")
                return
            else:
                if not self.idvalidator(lines):
                    print("** no instance found **")
                    return
                else:
                    # If instance is found, get its str repr.
                    if storage.all().get("{}.{}"
                                         .format(lines[0], lines[1])) is None:
                        # However, if ID not correspond to the given class
                        print("** no instance found **")
                    else:
                        print(storage.all().get("{}.{}"
                                                .format(lines[0], lines[1])))

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        lines = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        else:
            if not self.inclasslist(lines):
                print("** class doesn't exist **")
                return
            if len(lines) == 1:
                print("** instance id missing **")
                return
            else:
                if not self.idvalidator(lines):
                    print("** no instance found **")
                    return
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
        aux_list = []
        split_list = []
        if lines:
            if not self.inclasslist(lines):
                print("** class doesn't exist **")
                return
            # If name of class is given, print only str of
            # those class instances.
            for key, value in storage.all().items():
                # Identifying instances with respective class name.
                split_list = str(key).split(".")
                if split_list[0] == lines[0]:
                    # When key is proper, gets str repr of value.
                    aux_list.append(str(value))
                if len(aux_list) > 0:
                    print(aux_list)
        else:
            # When no class name given, print all str repr
            for key, value in storage.all().items():
                aux_list.append(str(value))
            if len(aux_list) > 0:
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
            if not self.inclasslist(lines):
                print("** class doesn't exist **")
                return
            if len(lines) == 1:
                print("** instance id missing **")
                return
            if not self.idvalidator(lines):
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

    def count(self, line):
        """Shows count of instances sepcified """
        if line in HBNBCommand.classes:
            count = 0
            for key, value in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """ Another way to identify commands """
        auxlist = line.split(".")
        dictfun = {"all()": self.do_all, "count()": self.count}
        justid = {"show": self.do_show, "destroy": self.do_destroy}
        moreparameters = {"update": self.do_update}

        if auxlist[1] in dictfun:
            # looks for the command in dictionary
            try:
                # Executes command (no parameters needed) 
                dictfun.get(auxlist[1])(auxlist[0])
            except Exception:
                pass
        else:
            # Getting parameters without parenthesis
            auxlist2 = auxlist[1].split("(")
            # Getting ID parameter for show and destroy
            idsplit = auxlist2[1][:-1]
            if auxlist2[0] in justid:
                try:
                    justid.get(auxlist2[0])(auxlist[0] +
                                            ' ' + idsplit)
                except Exception:
                    pass
            elif auxlist2[0] in moreparameters:
                # Update has even moreparameters, needs
                # to be handled differently
                idsplit = idsplit.split(",")
                # Splits by comma, then sends params in a form
                # that update function is made to receive
                try:
                    moreparameters.get(auxlist2[0])(auxlist[0] + ' ' +
                                                    ''.join([str(item) for item
                                                            in idsplit]))
                except Exception:
                    pass

    def do_EOF(self, line):
        """ EOF command to exit the program"""
        print("")
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        print("")
        return True

    def emptyline(self):
        """if emptyline, do nothing"""
        pass

    def inclasslist(self, lines):
        """ Auxiliar function to get if a given class
        exists
        """
        for elements in HBNBCommand.classes:
            # Checking if class given exists in list of classes
            if elements == lines[0]:
                # If found, break the loop
                return True
            else:
                # Continue until finds or iterates it all
                continue
            return False

    def idvalidator(self, lines):
        """ Auxiliary function that helps to identify
        if a given ID is saved into the objs
        dictionary
        """
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
                    # Now compares ID with given class
                    # to see if it corresponds
                    if storage.all().get("{}.{}".
                                         format(lines[0], lines[1])):
                        return True
                    else:
                        # The ID is correct but is for a diff class
                        return False
                else:
                    continue
                return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
