total = 3
def sum(arg1, arg2) :
    total = arg1 + arg2
    print("Didalam fungsi nilai total = " ,total)
    return total
sum(10, 20)
print("Diluar fungsi nilai total = " ,total)

print("------------------------------------------")

a = 3
def sum(arg1, arg2) :
    global b
    a = arg1 + arg2
    b = a + 5
    print("Didalam fungsi nilai total = " ,a)
    print("Didalam fungsi nilai total = " ,b)
    #return total
sum(10, 20)
print("Diluar fungsi nilai total = " ,a)
print("Diluar fungsi nilai total = " ,b)
