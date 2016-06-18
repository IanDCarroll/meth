class ud {
    public static int modd(int numerator, int modulator) {
	while (numerator > modulator) {
	    numerator -= modulator;
 	}
	return numerator;
    }

    public static int timz(int factor1, int factor2){
	int product = 0;
	while (factor2 > 0) {
	    product += factor1;
	    factor2 -= 1;
	}
	return product;
    }
}

public class meth {
    public static void main(String[] args) {
	System.out.println(ud.modd(137,60));
	System.out.println(ud.timz(6,7));
    }
}
