#RAFIF RAFI MUZAKKI WIDODO
#Nim 19010007
#81, 89, 80, 81, 80, 80, 80, 87, 91, 79, 90, 71, 90, 70, 90, 97

start = True
div = 0
while start :
    sum = 0
    number = [81,89,80,81,80,80,80,87,91,79,90,71,90,70,90,97]
    for each in number :
        sum = sum + each
    if div == 15 :
        start = False
    div += 1  

ave = sum / div
print("81, 89, 80, 81, 80, 80, 80, 87, 91, 79, 90, 71, 90, 70, 90, 97")
print("Banyak data = ", div)
print("Rata rata = ",sum, "Dibagi", div)
print("Rata - rata dari bilangan - bilangan tersebut adalah = ",ave )