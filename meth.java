class meth {
    public static int modd(int numerator, int modulator) {
	while (numerator > modulator) {
	    numerator -= modulator;
 	}
	return numerator;
    }

    public static void main(String[] args) {
	System.out.println(modd(122,60));
    }
}
