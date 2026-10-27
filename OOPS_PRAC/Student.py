class Student:
    # Class Variable
    college="SIRT COLLEGE"

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    # Instance Method
    def display_info(self):
        return self.name,self.roll_no
    
    #  Class method: updates the class variable
    @classmethod
    def change_college(cls,new_name):
        cls.college=new_name  #existing class variable ko update


# OBJECT
s1=Student("AKASH",56)
s2=Student("LILY",11)
# Update the class variable directly || className.variable_name = new_value
Student.college="wvt college"

# Access instance variables and call an instance method
print(s1.name)
print(s2.name)
print(s1.display_info())

# Update the class variable using a class method
Student.change_college("RSRT COLLEGE")
print(s1.college)

# # Modify an instance variable of s1
s1.name="RAHUL"
print(s1.name)
print(s1.display_info())

print(s2.name)

s1.college="ASD COLLEGE"
print(s1.college)