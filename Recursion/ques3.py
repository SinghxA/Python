num = int(input("Enter your nums : "))
count=num
def recursion(count):
    if count==0:
        return


    print(count)
    count-=1

    recursion(count)


recursion(num)

