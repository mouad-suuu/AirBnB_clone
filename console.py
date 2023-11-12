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
    cls_l = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    prompt = "(hbnb) "

    def do_quit(self, args):
        '''
        exit program
        '''
        return True

    def do_EOF(self, args):
        '''
        Exits after receiving the EOF signal.
        '''
        return True

    def emptyline(self):
        '''
        print anything with an empty line
        '''
        pass

    def do_create(self, inp):
        '''
        create new instance base model and save it in file json print id user
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
        '''
        Prints the string representation of an instance based on the
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
        verifies that class exists
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
        verifies if the id exists or not
        '''
        if len(ar) < 2:
            print("** instance id missing **")
            return False

        return True

if __name__ == "__main__":
    '''
    Entry point for the loop.
    '''
    HBNBCommand().cmdloop()

