#include <Python.h>
#include <stdio.h>
#include "ctest.h"
/*
int greeting(int a, int b)
{
    printf("%d + %d = %d", a, b, a + b);
    return a+b;
}
*/
static PyObject *
Addition(PyObject *self, PyObject *args)
{
    int a;
    int b;
    int sum;
    PyArg_ParseTuple(args, "ii", &a, &b); 
    sum = greeting(a, b);
    return Py_BuildValue("i", sum); 
}

static PyMethodDef 
PDevapiMethods[] = {
    {"greeting", Addition, METH_VARARGS, "add two numbers"},
    {NULL, NULL}
};

PyMODINIT_FUNC initPDevapi(void)
{
    Py_InitModule("PDevapi", PDevapiMethods);
}
