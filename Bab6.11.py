# membuat dictionary baru
pangkat = {1:1, 2:4, 3:9, 4:16, 5:25}

# menghapus anggota tertentu
# output: 9
print(pangkat.pop(3))

# menghapus anggota secara acak
# output: (5,25)
print(pangkat.popitem())

# yang tersisa adalah {1:1, 2:4, 4:16,}
print(pangkat)

#fungsi error
# delete 5
#del pangkat[5]
# output: {2:4, 4:16}
#print(pangkat)

# menghapus semua anggota
pangkat.clear()
# menghapus dictionary pangkat
del pangkat