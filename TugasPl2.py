A = int(input("Masukkkan bilangan 1 = "))
B = int(input("Masukkkan bilangan 2 = "))
C = int(input("Masukkkan bilangan 3 = "))
D = int(input("Masukkkan bilangan 4 = "))

asu = [A,B,C,D]
asu.sort()
mid = len(asu) 
datatengah = mid // 2
median = (asu[datatengah - 1] + asu[datatengah]) / 2
#me = deret[datatengah - 1] + deret[datatengah] / 2

print ("Bilangan terbesar adalah = ", asu)
print ("Bilangan terbesar adalah = ", median)