#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    length = None
    if sentence is None:
        first = None
        length = None
        return length, first
    elif len(sentence) == 0:
        first = None
        length = 0
        return length, first
    else:
        first = sentence[0]
        return len(sentence), first
