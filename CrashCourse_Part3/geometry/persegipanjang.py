from CrashCourse_Part3.geometry.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        # Fungsi yang dipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f"Ini adalah object dari PersegiPanjang dengan Panjang {self.p} dan Lebar {self.l}"

    def hitung_luas(self):
        return self.p * self.l
