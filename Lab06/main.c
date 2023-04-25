#include <stdio.h>

char *x;

void foo()
{
    char stack_buffer[3];
    x = &stack_buffer[1];
}

int main()
{
    foo();
    *x = 42; // use-after-return write
    return 0;
}