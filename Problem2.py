
evens = []

def fib(i,j):
    if j > 4000000:
        return

    print (i+j)
    if not((i+j)%2):
        evens.append(i+j)
    fib(j,i+j)

fib(1,1)
print("------------------------")
sum = 0
for i in evens:
    print(i)
    sum += i
print("------------------------")
print(sum)