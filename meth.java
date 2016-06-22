class ud {
    public static int modd(int numerator, int modulator) {
	while (numerator > modulator) {
	    numerator -= modulator;
 	}
	return numerator;
    }

    public static int timz(int factor1, int factor2) {
	int product = 0;
	while (factor2 > 0) {
	    product += factor1;
	    factor2 -= 1;
	}
	return product;
    }

    public static int cDiv(int numerator, int denominator) {
	int quotient = 0;
	while (numerator > 0) {
	    quotient += 1;
	    numerator -= denominator;
	}
	return quotient;
    }

    public static int sqar(int number) {
	int square = timz(number, number);
	return square;
    }

    public static int qoob(int number) {
	int cube = timz(sqar(number),number);
	return cube;
    }
}

public class meth {
    public static void main(String[] args) {
	//System.out.println(ud.modd(137,60));
	//System.out.println(ud.timz(6,7));
	//System.out.println(ud.cDiv(42,6));
	//System.out.println(ud.sqar(12));
	System.out.println(ud.qoob(5));
    }
}
