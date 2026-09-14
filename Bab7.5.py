#local scope
x = 10

def fungsiku():
    print("Inside = " ,x)
fungsiku()
print("Outside = " ,x)


print("-------------------------")


#global scope
def fungsiku():
    global x
    x = x + 2
    print("Inside = " ,x)
fungsiku()
print("Outside = " ,x) 