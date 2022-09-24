#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @pyObject: pointer to python object
 *
 * Return: void has no return
 */
void print_python_list_info(PyObject *pyObject)
{
	PyListObject *python_list;
	PyObject *objects;
	long int length, counter = 0;

	length = Py_SIZE(pyObject);
	printf("[*] Size of the Python List = %ld\n", length);

	python_list = (PyListObject *)pyObject;
	printf("[*] Allocated = %ld\n", python_list->allocated);

	while (counter < length)
	{
		objects = PyList_GetItem(pyObject, counter);
		printf("Element %ld: %s\n", counter, Py_TYPE(objects)->tp_name);
		counter++;
	}
}
