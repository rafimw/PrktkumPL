# membuat tuple kosong
# Output: ( )
my_tuple = ()
print(my_tuple)

# tuple dengan 1 elemen
# Output: (1,)
my_tuple = (1,)
print (my_tuple)

# tuple berisi integer
# output = (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple bersarang
# Output: ("hello", [1, 2, 3], (4, 5, 6))
my_tuple = ("hello", [1, 2, 3], (4, 5, 6))
print(my_tuple)

# Tuple bisa tidak menggunakan tanda ()
# Output (1, 2, 3)
my_tuple = 1, 2, 3
print(my_tuple)

# memasukkan anggota tuple ke variabel yang bersesuaian
# a akan berisi 1, b berisi 2, dan c berisi 3
# output 1 2 3
a, b, c = my_tuple
print(a)