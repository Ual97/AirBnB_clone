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

    def do_EOF(self):
        """ End of file command """
        print()
        return True

    def do_quit(self):
        """ Command to quit the CMD interface """
        print()
        return True

    def emptyline(self):
        """if emptyline, do nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
