class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0
    
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:" , Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

# Membuat Objek Pertama 
karyawan1 = Karyawan("Sarah", 12000000)
# Membuat Objek Kedua
karyawan2 = Karyawan("Budi", 16500000)

print("Karyawan.__doc__:", Karyawan.__doc__)
print("Karyawan.__name__:", Karyawan.__name__)
print("Karyawan.__module__", Karyawan.__module__)
print("Karyawan.__dict__", Karyawan.__dict__)
print("Karyawan.__bases__", Karyawan.__bases__)