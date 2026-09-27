count = 0

def recursion (count):
    if count==8:
        return

    else:
        print(count)

    count+=1
    recursion(count)

class main:  #blueprint
    def m(self,count): #method m
      recursion(count)   #whenver m method run then this function will run

wrap=main()  # we make actual obj for main class
wrap.m(count)  #we take help od obj and call the method m

