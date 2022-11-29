#!/usr/bin/python3

add_tuple = __import__('7-add_tuple').add_tuple



tuple_a = (1, 89, 45)

tuple_b = (88, 11, 87)

new_tuple = add_tuple(tuple_a, tuple_b)

print(new_tuple)



print(add_tuple(tuple_a, (1, )))

print(add_tuple(tuple_a, ()))

print(add_tuple(tuple_a, (1, 5, 6, 7)))
