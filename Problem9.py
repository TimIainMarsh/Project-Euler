x = 500
for a in range (x):
    for b in range (x):
        for c in range (x):
            if(a*a + b*b)== (c*c):
                if (a+b+c) == 1000:
                    print(a*b*c)
                    print(a,b,c)
                    break