#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        facts = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        facts = None

    return facts
