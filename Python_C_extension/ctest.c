#include <Python.h>
#include <stdio.h>

int greeting(int a, int b)
{
    printf("%d + %d = %d\n", a, b, a + b);
    return a+b;
}
