#!/usr/bin/python3
"""
This module serves as the entry point for the command interpreter,
facilitating user interaction with the interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBnB project's command interpreter"""

    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()

    def do_EOF(self, args):
        """Exit the command interpreter."""
        print()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Nothing will be done empty input line."""
        pass

    def do_help(self, args):
        """Display help for commands."""
        super().do_help(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
