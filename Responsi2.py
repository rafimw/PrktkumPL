data_1 = int(input("Masukkkan data ke- 1 = "))
data_2 = int(input("Masukkkan data ke- 2 = "))
data_3 = int(input("Masukkkan data ke- 3 = "))
data_4 = int(input("Masukkkan data ke- 4 = "))
data_5 = int(input("Masukkkan data ke- 5 = "))
data_6 = int(input("Masukkkan data ke- 6 = "))
data_7 = int(input("Masukkkan data ke- 7 = "))
data_8 = int(input("Masukkkan data ke- 8 = "))
data_9 = int(input("Masukkkan data ke- 9 = "))
data_10 = int(input("Masukkkan data ke- 10 = "))
data_11 = int(input("Masukkkan data ke- 11 = "))
data_12 = int(input("Masukkkan data ke- 12 = "))
data_13 = int(input("Masukkkan data ke- 13 = "))
data_14 = int(input("Masukkkan data ke- 14 = "))
data_15 = int(input("Masukkkan data ke- 15 = "))
data_16 = int(input("Masukkkan data ke- 16 = "))


#Mengurutkan bilangan
all_data = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, 
data_9, data_10, data_11, data_12, data_13, data_14, data_15, data_16]
print("Jadi dari data = ", all_data)
all_data.sort()
print ("Data yang telah diurutkan =\n",all_data)

#Median
x = len(all_data) 
datatengah = x // 2
me = (all_data[datatengah - 1] + all_data[datatengah]) / 2


#Rata_rata
ave = sum(all_data)
rata = ave / x

#Hasil
print("Diperoleh informasi bahwa : ")
print("Median = ", all_data[datatengah-1], "dan", all_data[datatengah])
print("Median = ", me)
print("Dan rata-rata data adalah = ", rata)