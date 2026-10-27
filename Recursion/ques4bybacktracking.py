def BACKT (i,n):
    if i<1:
        return
    BACKT(i-1,n)
    print(i)


BACKT(3,3)