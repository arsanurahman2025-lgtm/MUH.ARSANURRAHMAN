import math

def persegi():
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling


def persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling


def segitiga():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi1 = float(input("Masukkan sisi 1: "))
    sisi2 = float(input("Masukkan sisi 2: "))
    luas = 0.5 * alas * tinggi
    keliling = alas + sisi1 + sisi2
    return luas, keliling


def lingkaran():
    r = float(input("Masukkan jari-jari: "))
    luas = math.pi * r * r
    keliling = 2 * math.pi * r
    return luas, keliling


print("===== APLIKASI BANGUN DATAR =====")
nama = input("Masukkan nama anda: ")
print(f"Halo {nama}, selamat datang di aplikasi Bangun Datar")

print("\nMenu:")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")

pilih = input("Pilih menu (1-4): ")

if pilih == "1":
    luas, keliling = persegi()
elif pilih == "2":
    luas, keliling = persegi_panjang()
elif pilih == "3":
    luas, keliling = segitiga()
elif pilih == "4":
    luas, keliling = lingkaran()
else:
    print("Pilihan tidak valid")
    exit()

print(f"Luas = {luas}")
print(f"Keliling = {keliling}")
