<h1>0x07. Python - Test-driven development</h1>
<h2>Tasks</h2>
<p>0. Write a function that adds 2 integers.</p>
<p>1. Write a function that divides all elements of a matrix.</p>
<p>2. Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>
<p>3. Write a function that prints a square with the character <code>#</code>.</p>
<p>4. Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>
<p>5. In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>
<pre><code>guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i &lt; len(list):
        if list[i] &gt; result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2&gt;&amp;1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
</code></pre>
<p>100. Write a function that multiplies 2 matrices: (without <code>NumPy</code>)</p>
<p>101. Write a function that multiplies 2 matrices by using the module <a href="/rltoken/sXnBuOVSyhKEGt-biOyOWg" title="NumPy" target="_blank">NumPy</a></p>
<p>102. Create a function that prints Python strings.</p>
