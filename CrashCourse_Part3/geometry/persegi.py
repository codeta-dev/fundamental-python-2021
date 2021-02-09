from CrashCourse_Part3.geometry.bangun_ruang import BangunRuang


class Persegi(BangunRuang):
    def __init__(self, a,t):
        self.a = a
        self.t = t

    def info(self):
        return f"Ini adalah object dari Persegi dengan Alas {self.a} dan Tinggi {self.t}"

    def hitung_luas(self):
        hasil = (self.a*self.t)/2
        return hasil

