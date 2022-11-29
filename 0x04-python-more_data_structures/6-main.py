#!/usr/bin/python3

print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary



a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }

print_sorted_dictionary(a_dictionary)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},

          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print_sorted_dictionary(people)
