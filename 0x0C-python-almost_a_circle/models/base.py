#!/usr/bin/python3
""" Base class module file """
import json as js
import os.path
import csv
import turtle


class Base:
    """ The “base” of all other classes in this project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        result = "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return result
        else:
            result = js.dumps(list_dictionaries)
            return str(result)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        list_dictionaries = []

        if list_objs:
            for i in range(len(list_objs)):
                list_dictionaries.append(list_objs[i].to_dictionary())

            with open(filename, 'w', encoding="utf-8") as a_files:
                a_files.write(cls.to_json_string(list_dictionaries))
        else:
            with open(filename, 'w', encoding="utf-8") as a_files:
                a_files.write(cls.to_json_string(""))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        result = []
        if json_string:
            result = js.loads(json_string)
            return result
        else:
            return result

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            result = cls(20, 20)
        else:
            result = cls(20)
        result.update(**dictionary)
        return result

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as a_files:
            list_str = a_files.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes and deserializes in CSV """
        filename = cls.__name__ + ".json"
        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        result = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                result.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(result)

    @classmethod
    def load_from_file_csv(cls):
        """ Serializes and deserializes in CSV """
        filename = cls.__name__ + ".json"
        result = []
        if os.path.exists(filename) is False:
            return result

        with open(filename, 'r', encoding="utf-8") as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            result.append(dict_csv)

        list_ins = []
        for index in range(len(result)):
            list_ins.append(cls.create(**result[index]))
        return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares """
        turtle_r = turtle.Turtle()
        turtle_r.screen.bgcolor("#1E6292")
        turtle_r.pensize(2)
        turtle_r.shape("circle")

        turtle_r.color("#FFFFFF")
        for r in list_rectangles:
            turtle_r.showturtle()
            turtle_r.up()
            turtle_r.goto(r.x, r.y)
            turtle_r.down()
            for i in range(2):
                turtle_r.forward(r.width)
                turtle_r.left(90)
                turtle_r.forward(r.height)
                turtle_r.left(90)
            turtle_r.hideturtle()

        turtle_r.color("#FFAE42")
        for s in list_squares:
            turtle_r.showturtle()
            turtle_r.up()
            turtle_r.goto(s.x, s.y)
            turtle_r.down()
            for i in range(2):
                turtle_r.forward(s.width)
                turtle_r.left(90)
                turtle_r.forward(s.height)
                turtle_r.left(90)
            turtle_r.hideturtle()
        turtle.exitonclick()
