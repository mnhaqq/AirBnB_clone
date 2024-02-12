#!/usr/bin/python3
"""
Module containing entry point of command interpreter
"""
import cmd
from models.engine.file_storage import FileStorage
import models
import re
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Entry point of command interpreter
    """
    prompt = '(hbnb) '

    def pre_cmd(self, line):
        """Defines instructions to execute before <line> is interpreted.
        """
        if not line:
            return '\n'

    def do_create(self, args):
        """Create new instance of BaseModel and saves it
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in FileStorage.class_dict:
            print("** class doesn't exist **")
            return

        obj = FileStorage.class_dict[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Prints string representation of an instance
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in FileStorage.class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        object_id = args[1]
        objects = models.storage.all()
        key = f"{class_name}.{object_id}"

        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroys an instance and saves changes to json file
        """
        objects = models.storage.all()
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in FileStorage.class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        object_id = args[1]
        key = f"{class_name}.{object_id}"

        if key in objects:
            del objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints string representation of all instances based on class name
        """
        objects = models.storage.all()
        args = args.split()
        class_name = None

        if len(args) == 1:
            class_name = args[0]

        if class_name and class_name not in FileStorage.class_dict:
            print("** class doesn't exist **")
            return

        if class_name:
            print([f"{str(val)}" for val in objects.values()
                   if type(val).__name__ == class_name])
        else:
            print([f"{str(val)}" for val in objects.values()])

    def do_update(self, args):
        """Updates an instance by adding or updating attribute
        """
        objects = models.storage.all()
        args = args.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in FileStorage.class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        object_id = args[1]
        key = f"{class_name}.{object_id}"

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        attr_val = args[3]
        attr_val = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        attr_val = attr_val[0]

        obj = objects.get(key)
        obj_dict = obj.to_dict()
        prev = obj_dict.get(attr_name)

        if type(prev) is int:
            attr_val = int(attr_val)
        elif type(prev) is float:
            attr_val = float(attr_val)

        setattr(obj, attr_name, attr_val)
        for key, value in obj_dict.items():
            if key == '__class__':
                continue
            if key == 'created_at' or key == 'updated_at':
                value = datetime.fromisoformat(value)
            setattr(obj, key, value)
        models.storage.save()

    def do_quit(self, args):
        """Quit command to exit command interpreter
        """
        return True

    def do_EOF(self, args):
        """End of file
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
