# OOP Python
class Karyawan:
    '''Dasar kelas untk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1
    def tampilkan_jumlah(self):
        print("Total Karyawan: ", Karyawan.jumlah_karyawan)
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print()

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000)
# Membuat objek ketiga dari kelas Karyawan
karyawan3 = Karyawan("Riqqo", 10000)

# mengubah atribut objek
karyawan1.gaji =1500000
karyawan1.nama = 'Ratna'

# memodifikasi atribut dengan fungsi-fungsi
getattr(karyawan3, 'gaji')
setattr(karyawan2, 'gaji', 17000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)