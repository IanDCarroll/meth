#include <stdio.h>

int main() {
    int numerator;
    int modulator;

    printf("Enter numerator: ");
    scanf("%d", &numerator);
    printf("Enter modulator: ");
    scanf("%d", &modulator);

    while (numerator >= modulator) {
	numerator -= modulator;
    }

    printf("Modulus is %d\n", numerator);
    return 0;
}
