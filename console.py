#!/usr/bin/python3
"""console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, line):
        """handles end-of-file marker"""
        return True

    def emptyline(self):
        """Overwrites the default method which repeats
        the last command entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
