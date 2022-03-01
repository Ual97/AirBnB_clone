#!/usr/bin/python3
"""Program that contains entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb)"

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
   
if __name__ == "__main__":
    HBNBCommand().cmdloop()