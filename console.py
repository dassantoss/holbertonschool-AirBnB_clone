#!/usr/bin/python3
'''This module contains the entry point of the command interpreter.'''


import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    '''Represents the command interpreter for the HBNB project.'''

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program.'''
        return True

    def do_EOF(self, arg):
        '''Handles the EOF signal to exit the program.'''
        print()
        return True

    def emptyline(self):
        '''Does nothing when an empty line is entered.'''
        pass

    def help_EOF(self):
        '''Displays help message for EOF command.'''
        print("EOF command to exit the program")

    def help_help(self):
        '''Displays help message for help command.'''
        print("Help command to display help information.")

    def help_quit(self):
        '''Displays help message for quit command.'''
        print("Quit command to exit the program")

    def do_create(self, arg):
        '''Create a new instance of BaseModel, save it, and print the id.'''
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''Print the string representation of an instance
            based on the class name and id.
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        '''Delete an instance based on the class name and id.'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        '''Prints all string representation of all instances based
            or not on the class name.'''
        try:
            if arg:
                instances = [str(obj) for key, obj in storage.all().items()
                             if arg.lower() == key.split('.')[0].lower()]
            else:
                instances = [str(obj) for obj in storage.all().values()]
            if not instances:
                print("** class doesn't exist **")
            else:
                print(instances)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        '''Updates an instance based on the class name and id by adding
            or updating attribute.'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3].strip('"')
            instance = storage.all()[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
