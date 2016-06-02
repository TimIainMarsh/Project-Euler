
for i in range(0,100000000,20):
    if i ==0:continue
    devs = [1,2,20]
    for j in range(3,20):
        # print(not(i%j))
        if not(i%j):
            devs.append(j)
    # print(devs)
    if len(devs) == 20:
        print (devs)
        print(len(devs),i)
        break
# print(devs)
