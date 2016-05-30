val = 0
for i in range(100,999):
    for j in range(100,999):
        # print (i *j)
        string1 = str(i*j)
        string2  = string1[::-1]
        if string1 == string2:
            if i*j > val:
                val = i*j
            print (string1)

print ("------------")
print(val)