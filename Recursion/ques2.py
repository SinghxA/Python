num = int (input("ENTER THE VALUE OF NUM : "))
count=1
def recursion(count):
    if count>num:
        return

    print(count)
    count+=1

    recursion(count)

class main:
    def med(self,count):
        recursion(count)


obj=main()
obj.med(count)



