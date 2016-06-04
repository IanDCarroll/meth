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

//console.log(modd(122,60));
//console.log(timz(6,7));
//console.log(cDiv(525600,1440));