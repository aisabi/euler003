import sympy #Python library for symbolic mathematics.

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the given number? 29

def largestPrimeFactor(number):
	#Prime number until 10000
	np = list(sympy.primerange(0, 10000))
	nombre_test = number
	liste_premiers = []

	#Using the prime factors list 'np', get all prime factors of a 
	# number and put them in 'liste_premiers' list
	for i in np:
		while number%i ==0:
			number = number/i
			liste_premiers.append(i)

	# print the prime factors
	print('liste_premiers',liste_premiers) 
	# largest prime factor
	print('largest prime factor for :',nombre_test,' is',liste_premiers[-1]) 


largestPrimeFactor(600851475143)