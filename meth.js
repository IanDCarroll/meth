function modd(numerator,modulator) {
	while (numerator > modulator) {
		numerator -= modulator;
	}
	return numerator;
}

function timz(factor1,factor2) {
	var product = 0;
	while (factor2 > 0) {
		product += factor1;
		factor2 -= 1;
	}
	return product;
}

function cDiv(numerator,denominator) {
	var quotient = 0;
	while (numerator > 0) {
		quotient += 1;
		numerator -= denominator;
	}
	return quotient;
}

function sqar(number) {
	var square = timz(number,number);
	return square;
}

function qoob(number) {
	var cube = timz(sqar(number),number);
	return cube;
}

function paow(number,exponent) {
	var result = 1;
	while (exponent > 0) {
	    result = timz(number,result);
	    exponent -= 1;
	}
	return result;
}

function afib(sequent) {
	var first = 0,
	    second = 1,
	    savSecond = 0;
	while (sequent > 0) {
	     savSecond = second;
	     second += first;
	     first = savSecond;
	     sequent -= 1;
	}
	return first;
}

function fibs(start,end) {
	var ra = [];
	for (i=start;i<end+1;i++)
	    { ra.push(afib(i)); }
	return ra;
}

function fect(number) {
	fector = 1
	for (i=1;i<number+1;i++) {
	    fector = timz(fector,i);
	}
	return fector;
}

//console.log(modd(122,60));
//console.log(timz(6,7));
//console.log(cDiv(525600,1440));
//console.log(sqar(5));
//console.log(qoob(5));
//console.log(paow(5,0));
//console.log(paow(10,2));
//console.log(paow(2,6));
//console.log(afib(7));
//console.log(fibs(0,13));
console.log(fect(5));
