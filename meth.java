import java.util.*;

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

    public static int paow(int number, int exponent) {
	int result = 1;
	while (exponent > 0) {
	    result = timz(number, result);
	    exponent -= 1;
	}
	return result;
    }

    public static int afib(int sequent) {
	int first = 0,
	    second = 1,
	    savSecond = 0;
	while (sequent > 0) {
	    savSecond = second;
	    second += first;
	    first = savSecond;
	    sequent -=1;
	}
	return first;
    }

/* Warning Message:
Note: meth.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
*/
    public static ArrayList fibs(int start, int end) {
	ArrayList ra = new ArrayList();
	for (int i = start; i < end + 1; i++) {
	    ra.add(afib(i));
	}
	return ra;
    }
}

public class meth {
    public static void main(String[] args) {
	//System.out.println(ud.modd(137,60));
	//System.out.println(ud.timz(6,7));
	//System.out.println(ud.cDiv(42,6));
	//System.out.println(ud.sqar(12));
	//System.out.println(ud.qoob(5));
	//System.out.println(ud.paow(2,6));
	//System.out.println(ud.afib(10));
	System.out.println(ud.fibs(0,10));
    }
}
