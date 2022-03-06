#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """hbnb command"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]
    @classmethod
    def count(self, class_name, objects_dict):
        """ count the number of instance"""
        counter = 0
        for key in objects_dict.keys():
            if class_name in key:
                counter += 1
        print(counter)

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def emptyline(self):
        pass

    def do_help(self, args):
        cmd.Cmd.do_help(self, args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
