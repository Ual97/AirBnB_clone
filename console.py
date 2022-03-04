#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "City", "Amenity",
               "Review", "State", "Place"]

    def do_EOF(self, line):
        """ End of file command """
        print()
        return True

    def do_quit(self, line):
        """ Command to quit the CMD interface """
        print()
        return True

    def emptyline(self):
        """if emptyline, do nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
