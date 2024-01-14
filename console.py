#!/usr/bin/python3
"""
This module represents the `console` (CLI)
Current file: console.py
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The HBNBCommand inherits from Cmd class provided by the cmd module.
    This HBNBCommand implements a number of methods that we will use to
    interact with the command line interpretr. """

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exit the console"""
        return True

    def do_EOF(self, args):
        """Exit the console using EOF"""
        print()
        return True

    def emptyline(self):
        """Ensures not executing anything when the user click `Enter`
        with empty line as input (args)"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the `id`
        Usage:
            $ create BaseModel"""

        if args == '':
            print('** class name missing **')
        elif args == 'BaseModel':
            new_instance = BaseModel()
        elif args == 'User':
            new_instance = User()
        elif args == 'State':
            new_instance = State()
        elif args == 'City':
            new_instance = City()
        elif args == 'Amenity':
            new_instance = Amenity()
        elif args == 'Place':
            new_instance = Place()
        elif args == 'Review':
            new_instance = Review()
        else:
            print("** class doesn't exist **")
            return

        storage.new(new_instance)
        storage.save()
        print('{}'.format(new_instance.id))

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and `id`
        Usage:
            $ show BaseModel 1234-1234-1234"""

        objects_dict = storage.all()
        arguments = args.split()

        if len(arguments) == 0:
            print('** class name missing **')
        elif len(arguments) == 1:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        elif len(arguments) == 2:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                for key, value in objects_dict.items():
                    if value.id == arguments[1]:
                        print(str(value))
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
        the class name
        Usage:
            $ all BaseModel or $ all"""

        str_objs_list = []
        objects_dict = storage.all()

        if args == '':
            for key, value in objects_dict.items():
                str_objs_list.append(str(value))
            print(str_objs_list)
        elif args in [
                'BaseModel', 'User', 'State', 'City',
                'Amenity', 'Place', 'Review']:
            for key, value in objects_dict.items():
                if value.to_dict()['__class__'] == args:
                    str_objs_list.append(str(value))
            print(str_objs_list)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file)
        Usage:
            $ destroy BaseModel 1234-1234-1234"""

        objects_dict = storage.all()
        arguments = args.split()

        if len(arguments) == 0:
            print('** class name missing **')
        elif len(arguments) == 1:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        elif len(arguments) == 2:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                for key, value in objects_dict.items():
                    if value.id == arguments[1]:
                        del objects_dict[key]
                        storage.save()
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute
        Usage:
            $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'"""

        objects_dict = storage.all()
        arguments = args.split()

        if len(arguments) == 0:
            print('** class name missing **')
        elif len(arguments) == 1:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        elif len(arguments) == 2:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                for key, value in objects_dict.items():
                    if value.id == arguments[1]:
                        print("** attribute name missing **")
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(arguments) == 3:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                for key, value in objects_dict.items():
                    if value.id == arguments[1]:
                        print("** value missing **")
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(arguments) == 4:
            if arguments[0] in ['BaseModel', 'User', 'State', 'City',
                                'Amenity', 'Place', 'Review']:
                for key, value in objects_dict.items():
                    if value.id == arguments[1]:
                        if value.to_dict()['__class__'] != arguments[0]:
                            continue
                        if arguments[2] not in [
                                'id', 'created_at', 'updated_at']:
                            attr_value = arguments[3].strip('"')
                            if attr_value.isdigit():
                                attr_value = int(attr_value)
                            elif attr_value.replace('.', '', 1).isdigit():
                                attr_value = float(attr_value)
                            setattr(value, arguments[2], attr_value)
                            storage.save()
                            break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
