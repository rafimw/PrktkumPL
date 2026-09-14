my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
my_list.remove('p')
# output ['y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
print(my_list)

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
my_list.remove('n')
# remove hanya menghapus elemen pertama yang dijumpai
# output: ['p', 'y', 't', 'h', 'o', 'i', 'n', 'd', 'o']
print(my_list)

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
# Output 'y'
#instruksi my_list.pop(1) berfungsi untuk mencetak indeks ke 1 dari list
print(my_list.pop(1))

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
del my_list[2]
#instrusi del my_list[2], berfungsi untuk menghapus indeks ke 2 dari list
#output ['p', 'y', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
print(my_list)

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
my_list.clear()
# Fungsi my_list.clear() untuk menghapus keseluruhan isi list
# Output []
print(my_list)