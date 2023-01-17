'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''
def nthPrime(n):
    if n < 1:
        return None
    
    primeNumbers = [2]
    length = len(primeNumbers)
    x = 3

    while length < n:
        for y in primeNumbers:

            if not x%y:
                x += 2
                break
            else:
                primeNumbers.append(x)
                x += 2
    
    return primeNumbers

print(nthPrime(2))