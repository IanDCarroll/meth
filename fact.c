#include <stdio.h>


//An example of a recursive function. To be modified and merged with meth.c
int getFactorial(int n) {
    int local;
    if (n > 1) {
	local = n * getFactorial(n - 1);
	return local;
    } else {
	return 1;
    }
}

int main() {
    printf("%d\n", getFactorial(5));
    return 0;
}
