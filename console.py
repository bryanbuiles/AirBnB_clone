#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit the console"""
        sys.exit(1)
                
    def do_EOF(self, line):
        """Quit the console usin EOF signal"""
        return True

    def postloop(self):
        print
        
    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            My_Object = BaseModel()
            My_Object.save()
            print(My_Object.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        
        var = arg.split()
        z = 0
        if len(var) == 0:
            print("** class name missing **")
        elif var[0] != "BaseModel":
            print("** class doesn't exist **")
        elif var[0] == "BaseModel" and len(var) == 1:
            print("** instance id missing **")
        else: 
            a = storage.all()
            b = var[0] + "." + var[1]
            for i in a.keys():
                if i == b:
                    print(a[i])
                    z = 1
            if z == 0:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
