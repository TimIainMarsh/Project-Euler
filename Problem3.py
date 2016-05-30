value = 600851475143

valueTest = 13195
def is_prime(a):
    return all(a % i for i in range(2, a))

primes = []
for i in range(2,round(value/2)):
    if not(value%i):
        if(is_prime(i)):
            primes.append(i)
            print(i)


