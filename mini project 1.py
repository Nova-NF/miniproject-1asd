class SistemPendaftaranLowongan:
    def __init__(self):
        self.pelamar = {}  # Dictionary untuk menyimpan data pelamar

    def tambah_pelamar(self, nama, email, telepon, pengalaman, keahlian, lowongan):
        # Menambahkan data pelamar baru
        self.pelamar[email] = {
            'Nama': nama,
            'Email': email,
            'Telepon': telepon,
            'Pengalaman': pengalaman,
            'Keahlian': keahlian,
            'Lowongan': lowongan
        }
        print("Data Pelamar berhasil ditambahkan!")

    def tampilkan_pelamar(self):
        # Menampilkan semua data pelamar
        if self.pelamar:
            print("Daftar Pelamar:")
            for email, pelamar in self.pelamar.items():
                print(f"Email: {email}")
                for key, value in pelamar.items():
                    print(f"{key}: {value}")
                print()
        else:
            print("Belum ada Data pelamar. !!!!!!!!!!!")

    def update_pelamar(self, email, field, data_baru):
        # Mengupdate data pelamar berdasarkan email
        if email in self.pelamar:
            if field in self.pelamar[email]:
                self.pelamar[email][field] = data_baru
                print("Data pelamar berhasil diupdate.")
            else:
                print("Bidang tidak valid. !!!!!!!!!!!")
        else:
            print("Email pelamar tidak ditemukan.!!!!!!!!!!!")

    def hapus_pelamar(self, email):
        # Menghapus data pelamar berdasarkan email
        if email in self.pelamar:
            del self.pelamar[email]
            print("Data pelamar berhasil dihapus.")
        else:
            print("Email pelamar tidak ditemukan.!!!!!!!!!!!")

    def daftar_sebagai_pelamar(self):
        # Menampilkan opsi lowongan yang tersedia
        print("\nOpsi Lowongan yang Tersedia:")
        print("1. Web Developer")
        print("2. UI/UX Designer")
        print("3. Software Developer")

        # Memilih lowongan
        lowongan = input("\nPilih lowongan yang diminati (1/2/3): ")
        if lowongan == "1":
            lowongan = "Web Developer"
        elif lowongan == "2":
            lowongan = "UI/UX Designer"
        elif lowongan == "3":
            lowongan = "Software Developer"
        else:
            print("Pilihan tidak valid. !!!!!!!!!!!")
            return

        # Meminta data diri pelamar baru
        nama = input("{Masukkan nama}: ")
        email = input("{Masukkan email}: ")
        telepon = input("{Masukkan telepon}: ")
        pengalaman = input("{Masukkan pengalaman}: ")
        keahlian = input("{Masukkan keahlian (pisahkan dengan koma)}: ").split(',')

        self.tambah_pelamar(nama, email, telepon, pengalaman, keahlian, lowongan)

    def crud_admin(self):
        # Meminta username dan password admin
        username = input("Masukkan username: ")
        password = input("Masukkan password ****: ")

        # Validasi username dan password
        if username == "admin" and password == "sistem informasi":
            # Menampilkan menu admin
            while True:
                print("\nPilih operasi yang ingin Anda lakukan:")
                print("1. Tambah pelamar")
                print("2. Tampilkan pelamar")
                print("3. Update pelamar")
                print("4. Hapus pelamar")
                print("5. Keluar")

                pilihan = input("Masukkan nomor operasi: ")

                if pilihan == "1":
                    self.daftar_sebagai_pelamar()
                elif pilihan == "2":
                    self.tampilkan_pelamar()
                elif pilihan == "3":
                    email = input("Masukkan email pelamar: ")
                    field = input("Masukkan data yang ingin diupdate: ")
                    data_baru = input("Masukkan data baru: ")
                    self.update_pelamar(email, field, data_baru)
                elif pilihan == "4":
                    email = input("Masukkan email pelamar yang ingin dihapus: ")
                    self.hapus_pelamar(email)
                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid.")
        else:
            print("!!!!!!!!!!! Username atau password salah. !!!!!!!!!!!")

if __name__ == "__main__":
    sistem_pendaftaran = SistemPendaftaranLowongan()

    # Memilih peran
    peran = input("Apakah Anda admin atau pelamar? (admin/pelamar): ")

    if peran.lower() == "admin":
        sistem_pendaftaran.crud_admin()

    elif peran.lower() == "pelamar":
        sistem_pendaftaran.daftar_sebagai_pelamar()
        print("Terima kasih telah mendaftar!")

    else:
        print("Peran tidak valid. !!!!!!!!!!!")
        
        
