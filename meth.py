def modd(numerator,modulator):
	while numerator > modulator:
	    numerator -= modulator
	return numerator

def timz(factor1,factor2):
	product = 0
	while factor2 > 0:
	    product += factor1
	    factor2 -= 1
	return product

def cDiv(numerator,denominator):
	quotient = 0
	while numerator > 0:
	    quotient += 1
	    numerator -= denominator
	return quotient

def sqar(number):
	square = timz(number,number)
	return square

def qoob(number):
	cube = timz(sqar(number),number)
	return cube

def paow(number,exponent):
	result = 1
	while exponent > 0:
	    result = timz(number,result)
	    exponent -=1
	return result

def fibs(sequent):
	first = 0
	second = 1
	savSecond = 0
	while sequent > 0:
	    savSecond = second
	    second += first
	    first = savSecond
	    sequent -= 1
	return second

def main():
    arg0 = raw_input('Do you want modd, timz, cDiv, sqar, qoob, paow or something else? ')

    if arg0 == 'modd':
	arg1 = int(raw_input('Numerator: '))
	arg2 = int(raw_input('Modulator: '))
	print modd(arg1,arg2)
    elif arg0 == 'timz':
	arg1 = int(raw_input('First Factor: '))
	arg2 = int(raw_input('Second Factor: '))
	print timz(arg1,arg2)
    elif arg0 == 'cDiv':
	arg1 = int(raw_input('Numerator: '))
	arg2 = int(raw_input('Denominator: '))
	print cDiv(arg1,arg2)
    elif arg0 == 'sqar':
	arg1 = int(raw_input('Number: '))
	print sqar(arg1)
    elif arg0 == 'qoob':
	arg1 = int(raw_input('Number: '))
	print qoob(arg1)
    elif arg0 == 'paow':
	arg1 = int(raw_input('Number: '))
	arg2 = int(raw_input('Exponent: '))
	print paow(arg1,arg2)
    else:
	print 'Well we haven\'t got that option yet, so tough noogies!'

if __name__ == '__main__':
    main()
