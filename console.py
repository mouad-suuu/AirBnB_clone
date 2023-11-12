#!/usr/bin/python3
'''
Class of console for the Airbnb project
'''
import cmd
from models.engine.file_storage import FileStorage



class HBNBCommand(cmd.Cmd):
'''
console entry point command
'''
prpt = ("(hbnb) ")




def do_quit(self, args):
'''
exit programm
'''
return True


def do_EOF(self, args):
'''
exit after receiving signal
'''
return True


def emptyline(self):
'''
print any thing with a empty line
'''
pass


if __name__ == "__main__":
'''
Entry point for the loop.
'''
HBNBCommand().cmdloop()

