#include <python3.4/cpython/listobject.h>
#include <python3.4/cpython/object.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", PyList_Size(p));
	printf("[*] Allocated = %p\n", p);
	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %p\n", i, item);
	}
}
