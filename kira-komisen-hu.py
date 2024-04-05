# Atur cara mengira komisen
# Pengisytiharan pemboleh ubah
jumlah = 0
jualan = 0
komisen = 0
ulang = "Y"
while ulang == "Y":
    # Input
    jualan = float(input("Masukkan jumlah jualan: RM"))
    # Proses
    if jualan > 80:
        kadar_komisen = 0.055
    elif jualan > 70:
        kadar_komisen = 0.05
    elif jualan > 60:
        kadar_komisen = 0.04
    elif jualan > 50:
        kadar_komisen = 0.03
    else:
        kadar_komisen = 0.02
    komisen = jualan * kadar_komisen
    # Output
    print("komisen anda ialah RM", round(komisen,2))
    jumlah = jumlah + komisen
    # Input
    ulang = input("Masukkan Y untuk terus atau N untuk berhenti")
#Output
print("\nJumlah komisen ialah RM", round(jumlah,2))
print("Sekian, tamat")
