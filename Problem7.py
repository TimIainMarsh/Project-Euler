def is_prime(a):
    return all(a % i for i in range(2, a))

count = 0
for i in range(2,10000000):
    if is_prime(i):
        count += 1
        print (i,"--->",count)
    if count == 10001:
        print (i)
        break