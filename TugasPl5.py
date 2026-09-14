#definisi luas trapesium
def lTrapesium(sTrapesium1, sTrapesium2, tTrapesium):
    return 1/2 * (sTrapesium1+sTrapesium2) * tTrapesium

#Pengaplikasian fungsi
print("--------------------------------")
print("LUAS TRAPESIUM")
print("--------------------------------")
sTrapesium1 = int(input("Sisi Sejajar 1 = "))
sTrapesium2 = int(input("Sisi Sejajar 2 = "))
tTrapesium  = int(input("Tinggi Trapesium = "))
print("Jadi")
print("Luas Trapesium = 1/2 x (Sisi Sejajar 1 + Sisi Sejajar 2) x Tinggi Trapesium")
print("               = 1/2 x","(", sTrapesium1, "+", sTrapesium2, ")", "x", tTrapesium)
print("Luas Trapesium =" ,lTrapesium(sTrapesium1, sTrapesium2, tTrapesium))
print("--------------------------------")