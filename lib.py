def func (mas):
    N = len(mas)
    k = 0
    for i in range (1, N):
        t = True
        for j in range (N):
            if (mas[i].contains(mas[0][j]) != True):
                t = False
        if t == True:
            k = k + 1
    print (k)