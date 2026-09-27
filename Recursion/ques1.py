num = int(input("enter your num value : "))
count=0
def recur (count):
    if count==num:
        return

    print("STRIVER",count)
    count+=1

    recur(count)


class main:
    def e(self,count):
        recur(count)

obj=main()
obj.e(count)