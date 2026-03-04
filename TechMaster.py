from abc import ABC, abstractmethod


class BarangElektronik(ABC):

    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = stok
        self.__harga_dasar = harga_dasar

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_struk(self, no, jumlah):
        pass


class Laptop(BarangElektronik):

    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor
        self.pajak = 0.10

    def tampilkan_struk(self, no, jumlah):
        pajak_rp = self.get_harga_dasar() * self.pajak
        subtotal = jumlah * (self.get_harga_dasar() + pajak_rp)

        print(f"{no}. [LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(10%): Rp {pajak_rp:,.0f}")
        print(f" Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")

        return subtotal


class Smartphone(BarangElektronik):

    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera
        self.pajak = 0.05

    def tampilkan_struk(self, no, jumlah):
        pajak_rp = self.get_harga_dasar() * self.pajak
        subtotal = jumlah * (self.get_harga_dasar() + pajak_rp)

        print(f"{no}. [SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(5%): Rp {pajak_rp:,.0f}")
        print(f" Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")

        return subtotal


# ================= MAIN =================

print("--- SETUP DATA ---")
laptop = Laptop("ROG Zephyrus", 0, 20_000_000, "Ryzen 9")
hp = Smartphone("iPhone 13", 0, 15_000_000, "12MP")

laptop.tambah_stok(10)
hp.tambah_stok(-5)
hp.tambah_stok(20)

print("\n--- STRUK TRANSAKSI ---")

keranjang = [
    (laptop, 2),
    (hp, 1)
]

total = 0
for i, (barang, jumlah) in enumerate(keranjang, start=1):
    total += barang.tampilkan_struk(i, jumlah)

print("----------------------------------------")
print(f"TOTAL TAGIHAN: Rp {total:,.0f}")
print("----------------------------------------")
