# list kosong
my_list = []
# list berisi integer
my_list = [1,2,3,4,5]

# list berisi tipe campuran
my_list1 = [1, 3.5, "Hello"]
my_list = ["I", "love","python","programming",2021]

# output: I
my_list[0]
print(my_list[0])

#output: python
my_list[2]
print(my_list[2])

# list dalam list
your_list = ["hello", [1,2,3], "python"]
print(your_list)

# output 1
print(your_list[1][0])

# output 3
print(your_list[1][2])

# IndexError
my_list[6]
#hal ini terjadi karena jumlah index pada list hanya sampai 4 (0-4)