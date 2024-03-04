class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class SistemPendaftaranLowongan:
    def __init__(self):
        self.head = None
        self.tail = None
        self.admin_username = "admin"
        self.admin_password = "sistem informasi"

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def tambah_pelamar(self, nama, email, telepon, pengalaman, keahlian, lowongan, posisi="akhir"):
        new_node = Node({
            "nama": nama,
            "email": email,
            "telepon": telepon,
            "pengalaman": pengalaman,
            "keahlian": keahlian,
            "lowongan": lowongan
        })

        if posisi == "awal":
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif posisi == "tengah":
            if len(self) % 2 == 0:
                index = len(self) // 2
            else:
                index = (len(self) + 1) // 2
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node
        else:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

    def hapus_pelamar(self, idx):
        if 0 <= idx < len(self):
            current = self.head
            if idx == 0:  # Jika node pertama yang akan dihapus
                if self.head.next:  # Jika masih ada node lain setelahnya
                    self.head = self.head.next
                    self.head.prev = None
                else:  # Jika ini adalah satu-satunya node dalam linked list
                    self.head = None
                    self.tail = None
            elif idx == len(self) - 1:  # Jika node terakhir yang akan dihapus
                current = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
            else:  # Jika node di tengah yang akan dihapus
                for _ in range(idx):
                    current = current.next
                current.prev.next = current.next
                current.next.prev = current.prev
            print("___________________________________________________________")
            print(f"Data pelamar dengan nomor indeks {idx+1} berhasil dihapus.")
            print("___________________________________________________________")
        else:
            print("Nomor indeks tidak valid.!!!")

    def tampilkan_pelamar(self):
        if not self.head:
            print("||||||||||||||||||||||||||||||||||||||||||||||||")
            print("||||||Tidak ada data pelamar yang tersedia.|||||")
            print("||||||||||||||||||||||||||||||||||||||||||||||||")
        else:
            print("\nData Pelamar:")
            current = self.head
            idx = 1
            while current:
                print(f"{idx}. Nama: {current.data['nama']}, Email: {current.data['email']}, Telepon: {current.data['telepon']}, Pengalaman: {current.data['pengalaman']}, Keahlian: {current.data['keahlian']}, Lowongan: {current.data['lowongan']}")
                current = current.next
                idx += 1

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
            print("||||||||||||||||||||||||||||||||||")
            print("|||||Pilihan tidak valid.!!!!|||||")
            print("||||||||||||||||||||||||||||||||||")

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
            self.hapus_pelamar(len(self) - 1)  # hapus node terakhir
        else:
            print("||||||||||||||||||||||||||||||||||")
            print("|||||Pilihan tidak valid.!!!!!||||")
            print("||||||||||||||||||||||||||||||||||")

    def update_pelamar_admin(self):
        idx = int(input("Masukkan nomor indeks pelamar yang ingin diupdate: ")) - 1
        if 0 <= idx < len(self):
            current = self.head
            for _ in range(idx):
                current = current.next
            nama = input("Masukkan nama baru: ")
            email = input("Masukkan email baru: ")
            telepon = input("Masukkan telepon baru: ")
            pengalaman = input("Masukkan pengalaman baru: ")
            keahlian = input("Masukkan keahlian baru (pisahkan dengan koma): ").split(',')
            lowongan = input("Masukkan lowongan baru: ")
            current.data = {
                "nama": nama,
                "email": email,
                "telepon": telepon,
                "pengalaman": pengalaman,
                "keahlian": keahlian,
                "lowongan": lowongan
            }
            print("________________________________")
            print("Data pelamar berhasil diupdate.")
            print("________________________________")
        else:
            print("|||||||||||||||||||||||||||||||||||||||")
            print("|||||Nomor indeks tidak valid.!!!!!||||")
            print("|||||||||||||||||||||||||||||||||||||||")

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
                    print("Pilihan tidak valid.!!!!")

if __name__ == "__main__":
    sistem_pendaftaran = SistemPendaftaranLowongan()

    while True:
        peran = input("Apakah Anda admin atau pelamar? (admin/pelamar): ")

        if peran.lower() == "admin":
            sistem_pendaftaran.crud_admin()
        elif peran.lower() == "pelamar":
            sistem_pendaftaran.daftar_sebagai_pelamar()
        else:
            print("||||||||||||||||||||||||||||||||||")
            print("|||||Pilihan tidak valid.!!!!|||||")
            print("||||||||||||||||||||||||||||||||||")
