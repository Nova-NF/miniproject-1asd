class SistemPendaftaranLowongan:
    def __init__(self):
        self.pelamar_data = []
        self.admin_username = "admin"
        self.admin_password = "sistem informasi"

    def tambah_pelamar(self, nama, email, telepon, pengalaman, keahlian, lowongan, posisi="akhir"):
        data_pelamar = {
            "nama": nama,
            "email": email,
            "telepon": telepon,
            "pengalaman": pengalaman,
            "keahlian": keahlian,
            "lowongan": lowongan
        }
        if posisi == "awal":
            self.pelamar_data.insert(0, data_pelamar)
        elif posisi == "tengah":
            if len(self.pelamar_data) % 2 == 0:
                index = len(self.pelamar_data) // 2
            else:
                index = (len(self.pelamar_data) + 1) // 2
            self.pelamar_data.insert(index, data_pelamar)
        else:
            self.pelamar_data.append(data_pelamar)
        print("════════════════════════════════")
        print("Data Pelamar berhasil ditambahkan")
        print("════════════════════════════════")

    def hapus_pelamar(self, idx):
        if idx < len(self.pelamar_data):
            del self.pelamar_data[idx]
            print(f"Data pelamar dengan nomor indeks {idx+1} berhasil dihapus.")
        else:
            print("|||||||||||||||||||||||||||||")
            print("Nomor indeks tidak valid.!!!")
            print("|||||||||||||||||||||||||||||")

    def tampilkan_pelamar(self):
        if not self.pelamar_data:
            print("Tidak ada data pelamar yang tersedia.")
        else:
            print("\nData Pelamar:")
            for idx, pelamar in enumerate(self.pelamar_data, start=1):
                print(f"{idx}. Nama: {pelamar['nama']}, Email: {pelamar['email']}, Telepon: {pelamar['telepon']}, Pengalaman: {pelamar['pengalaman']}, Keahlian: {pelamar['keahlian']}, Lowongan: {pelamar['lowongan']}")

    def daftar_sebagai_pelamar(self, posisi="akhir"):
        nama = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        telepon = input("Masukkan telepon: ")
        pengalaman = input("Masukkan pengalaman: ")
        keahlian = input("Masukkan keahlian (pisahkan dengan koma): ").split(',')
        lowongan = input("Masukkan lowongan yang diminati: ")
        self.tambah_pelamar(nama, email, telepon, pengalaman, keahlian, lowongan, posisi)

    def tambah_pelamar_admin(self):
        print("\nPilih posisi untuk menambahkan pelamar:")
        print("1. Tambah di awal")
        print("2. Tambah di tengah")
        print("3. Tambah di akhir")
        posisi = input("Masukkan nomor posisi: ")
        if posisi == "1":
            self.daftar_sebagai_pelamar("awal")
        elif posisi == "2":
            self.daftar_sebagai_pelamar("tengah")
        elif posisi == "3":
            self.daftar_sebagai_pelamar("akhir")
        else:
            print("|||||||||||||||||||||||||||||")
            print("||Pilihan tidak valid.!!!!|||")
            print("|||||||||||||||||||||||||||||")

    def hapus_pelamar_admin(self):
        print("\nPilih posisi untuk menghapus pelamar:")
        print("1. Hapus di awal")
        print("2. Hapus di tengah")
        print("3. Hapus di akhir")
        posisi = input("Masukkan nomor posisi: ")
        if posisi == "1":
            self.hapus_pelamar(0)
        elif posisi == "2":
            idx = int(input("\nMasukkan nomor indeks pelamar yang ingin dihapus: ")) - 1
            self.hapus_pelamar(idx)
        elif posisi == "3":
            self.hapus_pelamar(-1)
        else:
            print("|||||||||||||||||||||||||||||")
            print("||Pilihan tidak valid.!!!!!||")
            print("|||||||||||||||||||||||||||||")

    def update_pelamar_admin(self):
        idx = int(input("Masukkan nomor indeks pelamar yang ingin diupdate: ")) - 1
        if 0 <= idx < len(self.pelamar_data):
            nama = input("Masukkan nama baru: ")
            email = input("Masukkan email baru: ")
            telepon = input("Masukkan telepon baru: ")
            pengalaman = input("Masukkan pengalaman baru: ")
            keahlian = input("Masukkan keahlian baru (pisahkan dengan koma): ").split(',')
            lowongan = input("Masukkan lowongan baru: ")
            self.pelamar_data[idx] = {
                "nama": nama,
                "email": email,
                "telepon": telepon,
                "pengalaman": pengalaman,
                "keahlian": keahlian,
                "lowongan": lowongan
            }
            print("════════════════════════════════")
            print("Data pelamar berhasil diupdate.")
            print("════════════════════════════════")
        else:
            print("Nomor indeks tidak valid.!!!!!")

    def crud_admin(self):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == self.admin_username and password == self.admin_password:
            while True:
                print("\nPilih operasi yang ingin Anda lakukan:")
                print("1. Tampilkan pelamar")
                print("2. Tambah pelamar")
                print("3. Hapus pelamar")
                print("4. Update pelamar")
                print("5. Keluar")

                pilihan = input("Masukkan nomor operasi: ")

                if pilihan == "1":
                    self.tampilkan_pelamar()
                elif pilihan == "2":
                    self.tambah_pelamar_admin()
                elif pilihan == "3":
                    self.hapus_pelamar_admin()
                elif pilihan == "4":
                    self.update_pelamar_admin()
                elif pilihan == "5":
                    break
                else:
                    print("|||||||||||||||||||||||||||||")
                    print("||Pilihan tidak valid.!!!||||")
                    print("|||||||||||||||||||||||||||||")

# Main Program
if __name__ == "__main__":
    sistem_pendaftaran = SistemPendaftaranLowongan()

    while True:
        peran = input("Apakah Anda admin atau pelamar? (admin/pelamar): ")

        if peran.lower() == "admin":
            sistem_pendaftaran.crud_admin()
        elif peran.lower() == "pelamar":
            sistem_pendaftaran.daftar_sebagai_pelamar()
        else:
            print("Pilihan tidak valid.!!!!!!")
