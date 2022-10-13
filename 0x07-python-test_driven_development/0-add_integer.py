#!/usr/bin/python3
def add_integer(a, b=98):
	if type(a) not in [int, float]:
		raise TypeError("a must be an integer")
	if type(b) not in [int, float]:
		raise TypeError("b must be an integer")
	if type(a) not in [int]:
		a = int(a)
	if type(b) not in [int]:
		b = int(b)
	return a + b
