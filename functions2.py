#functions in python
#parameter less/non-returnable function
def mul():
    a = 6
    b = 5
    print(a * b)
mul()



#parameterized functions

def sub(literal1 = int, literal2 = int):
    print(literal1 - literal2)
sub(30, 20)



#functions with named params

def add(literal1 = int, literal2 = int):
    print(literal1 + literal2)
a = 25
b = 13
add(literal1=a, literal2=b)
add(literal1=b, literal2=a)




#checking given number palindrome or not
def palindrome():

    str = input("Enter the string: ")
    if (str == str[::-1]):
        print("This string is palindrome.")
    else:
        print("This string is not palindrome.")

palindrome()