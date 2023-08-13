#!/usr/bin/python3
"""console module"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.

        Args:
            args (str): arguments passed to function"""
        args = line.split(' ')
        if not line:
            print("** class name missing **")
        elif HBNBCommand.cls_dict.get(args[0]) is None:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs_dict = storage.all()
            for key, value in objs_dict.items():
                cls_name = value.__class__.__name__
                cls_id = value.id
                if cls_name == args[0] and cls_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into JSON file)

        Args:
            line (str): arguments passed to function"""
        args = line.split(' ')
        if not line:
            print("** class name missing **")
        elif HBNBCommand.cls_dict.get(args[0]) is None:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs_dict = storage.all()
            for key, value in objs_dict.items():
                cls_name = value.__class__.__name__
                cls_id = value.id
                if cls_name == args[0] and cls_id == args[1].strip('"'):
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")


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
