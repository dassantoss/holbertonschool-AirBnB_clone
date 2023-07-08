#!/usr/bin/python3
'''This module contains the entry point of the command interpreter.'''


import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
