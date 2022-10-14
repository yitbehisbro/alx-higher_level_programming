#include <stdio.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_string - prints Python strings.
 * @p: Python Object
 *
 * Return: void has no return
 */
void print_python_string(PyObject *p)
{

	PyObject *pyObject, *point;

	(void)point;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	point = PyObject_Repr(p);
	pyObject = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(pyObject));
}
