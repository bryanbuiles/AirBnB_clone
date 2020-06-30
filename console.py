#!/usr/bin/python3
"""This file contain a class that create a console usin cmd module"""
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

allclases = {"BaseModel": BaseModel, "User": User, "State": State,
    "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

def errors(arg):
    """This function check if the input data is complete
    to take the different actions with class instances"""
    if len(arg) == 0:
        print("** class name missing **")
        return 2
    elif arg[0] not in allclases:
        print("** class doesn't exist **")
        return 2
    elif arg[0]not in allclases and len(arg) == 1:
        print("** instance id missing **")
        return 2


def parsing(var):
    """This funtion check the type of input and cast it
    Args:
        - Value to save like instance value
    Return:
        - Value casted"""
    a = 0
    if var[0] == '"' and var[-1] == '"':
        return var[1: -1]
    for i in var:
        if i == ".":
            a += 1
    if a == 0:
        return int(var)
    else:
        return float(var)

def count(arg):
        a = storage.all()
        b = 0
        for i in a.keys():
            c = str(i)
            c = c.split(".")
            if arg == c[0]:
                b += 1
        return b

def advance(self, arg, cls):
    if len(arg) != 0:
        if arg == ".all()":
            self.do_all(cls) 
        elif arg == ".count()":
            print(count(cls))
        elif arg[0:9] == ".destroy(":
            c = arg.split('"')
            self.do_destroy(cls + " " + c[1])
        elif arg[0:6] == ".show(":
            c = arg.split('"')
            self.do_show(cls + " " + c[1])
        elif arg[0:8] == ".update(":
            c = arg.split("(")
            d = c[1].split(", ")
            print(cls + " " + d[0][1:-1] + " " + d[1][1:-1]
                + " " + d[2][:-1])
            self.do_update(cls + " " + d[0][1:-1] + " " + d[1][1:-1]
                + " " + d[2][:-1])


class HBNBCommand(cmd.Cmd):
    """This class create a Python console that allow create, show, update,
    a destroy class instances"""

    def __init__(self):
        """Class constructor"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """This funtion allow exit from the console using the command
        'quit'"""
        sys.exit(1)

    def do_EOF(self, line):
        """This function allow exit from the console using EOF signal
        'ctrl + d'"""
        return True

    def postloop(self):
        """This funtion manage when the user tip enter in a new line"""
        print

    def do_create(self, arg):
        """"This funtion Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        Args:
            - Class name"""
        if not arg:
            print("** class name missing **")
            return
        elif arg in allclases:
            My_Object = allclases[arg]()
            My_Object.save()
            print(My_Object.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """This funtion prints the string representation of an instance
        based on the class name and id
        Args:
            - Class name
            - id"""
        var = arg.split()
        k = errors(var)
        if k != 2:
            z = 0
            a = storage.all()
            b = var[0] + "." + var[1]
            for i in a.keys():
                if i == b:
                    print(a[i])
                    z = 1
            if z == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        """This funtion deletes an instance based on the class name and id
        (save the change into the JSON file).
        Args:
            - Class name
            - id"""
        var = arg.split()
        k = errors(var)
        if k != 2:
            z = 0
            a = storage.all()
            b = var[0] + "." + var[1]
            for i in a.keys():
                if i == b:
                    del a[i]
                    storage.save()
                    z = 1
                    break
            if z == 0:
                print("** no instance found **")

    def do_all(self, arg):
        """This funtion prints all string representation of all instances
        based or not on the class name
        Args:
            - Class Name"""

        if arg not in allclases:
            print("** class doesn't exist **")
        else:
            a = storage.all()
            b = []
            for i in a.keys():
                c = str(i)
                c = c.split(".")
                if arg == c[0]:
                    b.append(a[i].__str__())
            print(b)


    def do_update(self, arg):
        """This funtion updates an instance based on the class name
        and id by adding or updating attribute (save the change into
        the JSON file)
        Args:
            - Class name
            - id
            - Attribute name
            - Attribute value"""
        var = arg.split()
        k = errors(var)
        if k != 2:
            z = 0
            a = storage.all()
            b = var[0] + "." + var[1]
            for i in a.keys():
                if i == b:
                    z = 1
            if z == 0:
                print("** no instance found **")
                return
            if len(var) == 2:
                print("** attribute name missing **")
                return
            elif len(var) == 3:
                print("** value missing **")
                return
            l = ["id", "created_at", "update_at"]
            if var[2] in l:
                return
            try:
                for j in a.keys():
                    if j == b:
                        k = parsing(var[3])
                        setattr(a[j], var[2], k)
            except:
                ValueError


    def do_User(self, arg):
        if len(arg) != 0:
            advance(self, arg, "User")
        #Falta error

    
    def do_City(self, arg):
        if len(arg) != 0:
            advance(self, arg, "City")
    
    def do_BaseModel(self, arg):
        if len(arg) != 0:
            advance(self, arg, "BaseModel")
    
    def do_Review(self, arg):
        if len(arg) != 0:
            advance(self, arg, "Review")
    
    def do_Amenity(self, arg):
        if len(arg) != 0:
            advance(self, arg, "Amenity")

    def do_State(self, arg):
        if len(arg) != 0:
            advance(self, arg, "State")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
