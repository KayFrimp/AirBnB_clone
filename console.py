#!/usr/bin/python3
"""console module"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter class that inherits Cmd module

    Attributes:
        prompt: issued to solicit input
        cls_dict (dict): key/value of supported classes"""

    prompt = '(hbnb) '
    cls_dict = {'BaseModel': BaseModel}

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

    def do_create(self, class_name):
        """creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.

        Args:
           class_name (str): class name"""
        if not class_name:
            print("** class name missing **")
        elif HBNBCommand.cls_dict.get(class_name) is None:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.cls_dict[class_name]()
            obj.save()
            print(obj.id)

    def do_show(self):
        """Prints the string representation of an instance
        based on the class name and id."""
        pass

    def do_destroy(self):
        """Deletes an instance based on the class name and id
        (save the change into JSON file)"""
        pass

    def do_all(self):
        """Prints all string representation of all instances
        based or not on the class name."""
        pass

    def do_update(self):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into JSON file"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
