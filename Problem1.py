list1 = []
for i in range(1000):
    # i%3 will produce zero if i is divisable by 3 - zero is seen as false that is why
    # it is not(i%3)
    if not(i%3) or not(i%5):
        list1.append(i)
sum = 0
for i in list1:
    sum += i
print(sum)