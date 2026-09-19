# a function is a reusable block of organized code that executes a specific task only when it is called.

def greet():
    print("hey whats up")
greet()

# //////////////////////////////////////////////////////////////

def add(c,b):  #Parameter(C,D)
    return c+b
    
add(3,4)  #yaha ans toh ayega but dikhega nhi 
print(add(4,9))

result=add(2,3)
print(result)

# ///////////////////////////////////////////////////////////

def sub_add(x,y):
    j = x + y
    k = x - y

    return j ,k 

result0 , result1 = sub_add(5,6)  #returninig two value you have accept two values

print(result0,result1)

# ///////////////////////////////////////////////////////////////

