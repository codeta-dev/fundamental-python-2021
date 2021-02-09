from geometry.bangun_ruang import BangunRuang
from geometry.persegi import Persegi
from geometry.persegipanjang import PersegiPanjang

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Persegi(4, 2 )
print(s1.info())
print(s1.hitung_luas())

print(f"\nMencoba membuat object dari kelas BangunRuang()")
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorphism : Kemampuan  objek untuk merespon berbeda terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print(f"\nPolymorphism")
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
# Ketika info() di panggil, maka penerapannya berbeda tergantung isi dari method tersebut