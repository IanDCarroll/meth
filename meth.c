#include <stdio.h>

int modd(int numerator, int modulator) {
    while (numerator >= modulator) {
	numerator -= modulator;
    }
    return numerator;
}

int main() {
    int numerator;
    int modulator;

    printf("Enter numerator: ");
    scanf("%d", &numerator);
    printf("Enter modulator: ");
    scanf("%d", &modulator);

    printf("Modulus is %d\n", modd(numerator, modulator));
    return 0;
}
