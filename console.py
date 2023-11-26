#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
import ast
from models.base_model import BaseModel
from models.user import User
from models import storage
from shlex import split
import shlex
from models.comparison import Comparison
from models.recommendation import Recommendation
from models.product import Product
from models.review import Review


class OLIVEBOOMCommand(cmd.Cmd):
    prompt = '(OliveBoom) '
    classes = {"BaseModel",
               "User", "Comparison", "Recommendation", "Product", "Review"}

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        """creates an object"""
        if not len(line):
            print("** class name missing **")
            return
        if line not in OLIVEBOOMCommand.classes:
            print("** class doesn't exist **")
            return
        newObject = eval(line)()
        print(newObject.id)
        newObject.save()

    def do_show(self, line):
        """shows an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in OLIVEBOOMCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[keyValue])

    def do_destroy(self, line):
        """deletes an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in OLIVEBOOMCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[keyValue]
        storage.save()

    def do_all(self, line):
        """prints all"""
        if not len(line):
            print([obj for obj in storage.all().values()])
            return
        strings = split(line)
        if strings[0] not in OLIVEBOOMCommand.classes:
            print("** class doesn't exist **")
            return
        print([obj for obj in storage.all().values()
               if strings[0] == type(obj).__name__])

    def do_update(self, line):
        """updates an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in OLIVEBOOMCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[keyValue], strings[2], eval(strings[3]))
        except Exception as e:
            setattr(storage.all()[keyValue], strings[2], strings[3])

    def emptyline(self):
        """passes"""
        pass

    def stripper(self, st):
        """strips that line"""
        newstring = st[st.find("(")+1:st.rfind(")")]
        newstring = shlex.shlex(newstring, posix=True)
        newstring.whitespace += ','
        newstring.whitespace_split = True
        return list(newstring)

    def dict_strip(self, st):
        """tries to find a dict while stripping"""
        newstring = st[st.find("(")+1:st.rfind(")")]
        try:
            newdict = newstring[newstring.find("{")+1:newstring.rfind("}")]
            return eval("{" + newdict + "}")
        except (SyntaxError, ValueError, TypeError) as e:
            return None

    def default(self, line):
        """defaults"""
        subArgs = self.stripper(line)
        strings = list(shlex.shlex(line, posix=True))
        if strings[0] not in OLIVEBOOMCommand.classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if strings[2] == "all":
            self.do_all(strings[0])
        elif strings[2] == "count":
            count = 0
            for obj in storage.all().values():
                if strings[0] == type(obj).__name__:
                    count += 1
            print(count)
            return
        elif strings[2] == "show":
            key = strings[0] + " " + subArgs[0]
            self.do_show(key)
        elif strings[2] == "destroy":
            key = strings[0] + " " + subArgs[0]
            self.do_destroy(key)
        elif strings[2] == "update":
            newdict = self.dict_strip(line)
            if type(newdict) is dict:
                for key, val in newdict.items():
                    keyVal = strings[0] + " " + subArgs[0]
                    self.do_update(keyVal + ' "{}" "{}"'.format(key, val))
            else:
                key = strings[0]
                for arg in subArgs:
                    key = key + " " + '"{}"'.format(arg)
                self.do_update(key)
        else:
            print("*** Unknown syntax: {}".format(line))
            return


if __name__ == '__main__':
    OLIVEBOOMCommand().cmdloop()
