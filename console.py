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

#!/usr/bin/python3
'''
Class of console for the Airbnb project
'''
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
'''
console entry point command
'''
cls_l = ["BaseModel", "User", "State", "City", "Amenity","Place", "Review"]
prpt = ("(hbnb) ")




def do_exit(self, args):
'''
exit programm
'''
return True


def do_EOF(self, args):
'''
Exits after receiving the EOF signal.
'''
return True


def emptyline(self):
'''
print any thing with a empty line
'''
pass


def do_create(self, inp):
'''create new instance base model and save it in file json print id user
'''
ar = inp.split()
if not self.clas_verf(ar):
return


inst = eval(str(ar[0]) + '()')
if not isinstance(inst, BaseModel):
return
inst.save()
print(inst.id)


def do_show(self, inp):
'''Prints the string representation of an instance based on the
class name and id.
'''
ar = inp.split()


if not self.clas_verf(ar):
return


if not self.verf_id(ar):
return


string_key = str(ar[0]) + '.' + str(ar[1])
objects = models.storage.all()
print(objects[string_key])


@classmethod
def clas_verf(cls, ar):
'''
verfies that class exists


'''
if len(ar) == 0:
print("** class name missing **")
return False


if ar[0] not in cls.cls_l:
print("** class doesn't exist **")
return False


return True


@staticmethod
def verf_id(ar):
'''
verifie if the id exsits or not


'''
if len(ar) < 2:
print("** instance id missing **")
return False

