angka = 0 
while (angka < 10) :
    print("Nilai angka adalah = ", angka)
    angka = angka + 1

i = 0 
while (i < 0) :
    i = i + 2
    print(i)

count = 2
while (count < 5):
    print("The count is = ", count)
    count = count + 1
print("Goodbye !!!") 

start = True
dimulaidari = 0
while start :
    print("Didalam while ", dimulaidari)
    if dimulaidari == 5 :
        start = False
        print("ok.done")
    dimulaidari += 1 

jawab = 'gas'
hitung = 0 
while(True) :
    hitung += 1
    jawab = input("Gass lagi gak ? ")
    if jawab == 'males' :
        break
print("Perulangan sebanyak "+str(hitung), "kali")