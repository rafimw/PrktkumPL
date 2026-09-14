#Menulis file
try :
    f = open("d:\\vscode\\PrktkumPL\\T.txt")
    with open("d:\\vscode\\PrktkumPL\\T.txt", 'w') as f:
        f.write("Institut Teknology\n")
        f.write("Dirgantara Adisutjipto\n")
        f.write("Yogyakarta\n")
finally :
    f.close()
#Membaca file yang telah di rubah
f = open("d:\\vscode\\PrktkumPL\\T.txt")
print(f.read())
print(f.read(10))
print(f.read(5))
print(f.read())