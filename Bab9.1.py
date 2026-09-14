#Membuka file
#File berada pada d:\vscode\PrktkumPL\T.txt
f = open("d:\\vscode\\PrktkumPL\\T.txt")
#Membaca file
print(f.read(8)) # membaca 8 data (karakter) pertama
#'This'
print(f.read(10)) # membaca 10 yang berikutnya lagi
#' is '
print(f.read())# membaca file sisanya sampai akhir file
#'the first line\nThis is the second line\nThis is the third line\n'
print(f.read()) # sudah tidak ada karakter untuk dibaca
