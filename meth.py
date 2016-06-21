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

def afib(sequent):
	first = 0
	second = 1
	savSecond = 0
	while sequent > 0:
	    savSecond = second
	    second += first
	    first = savSecond
	    sequent -= 1
	return first

def fibs(start,end):
	ra = []
	for i in range(start,end+1):
	    ra.append(afib(i))
	return ra

def fect(number):
	fector = 1
	for i in range(1,number+1):
	    fector = timz(fector,i)
	return fector

def isPm(number):
	bouillon = True
	for i in range(2,number):
	    if number % i == 0:
		bouillon = False
	return bouillon

def main():
    arg0 = raw_input('Do you want modd, timz, cDiv, sqar, qoob, paow, afib, fibs, fect, isPm or something else? ')

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
    elif arg0 == 'afib':
	arg1 = int(raw_input('Which place in Fibonacci sequence? '))
	print afib(arg1)
    elif arg0 == 'fibs':
	arg1 = int(raw_input('Start of Sequence: '))
	arg2 = int(raw_input('End of Sequence: '))
	print fibs(arg1,arg2)
    elif arg0 == 'fect':
	arg1 = int(raw_input('Number to be fectorialized: '))
	print fect(arg1)
    elif arg0 == 'isPm':
	arg1 = int(raw_input('Enter the number that may be prime: '))
	print isPm(arg1)
    else:
	print 'Well we haven\'t got that option yet, so tough noogies!'

if __name__ == '__main__':
    main()
