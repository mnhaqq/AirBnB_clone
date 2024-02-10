#!/usr/bin/python3
"""
Module containing entry point of command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit command interpreter
        """
        return True

    def do_EOF(self, line):
        """End of file
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
