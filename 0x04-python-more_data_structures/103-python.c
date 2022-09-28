#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints python bytes
 * @pyObject: pointer to python object
 *
 * Return: void has no return
 */
void print_python_bytes(PyObject *pyObject)
{
	char *str;
	long int length, i = 0, maximum;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(pyObject))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	length = ((PyVarObject *)(pyObject))->ob_size;
	str = ((PyBytesObject *)pyObject)->ob_sval;

	printf("  size: %ld\n", length);
	printf("  trying string: %s\n", str);

	if (length >= 10)
		maximum = 10;
	else
		maximum = length + 1;

	printf("  first %ld bytes:", maximum);

	while (i < maximum)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - prints the python list info
 * @pyObject: pointer to python object
 *
 * Return: has no return
 */
void print_python_list(PyObject *pyObject)
{
	long int length, i = 0;
	PyListObject *pyListObject;
	PyObject *pyObj;

	length = ((PyVarObject *)(pyObject))->ob_size;
	pyListObject = (PyListObject *)pyObject;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", pyListObject->allocated);

	while (i < length)
	{
		pyObj = ((PyListObject *)pyObject)->ob_item[i];
		printf("Element %ld: %s\n", i, ((pyObj)->ob_type)->tp_name);
		if (PyBytes_Check(pyObj))
			print_python_bytes(pyObj);
		i++;
	}
}
