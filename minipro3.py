class Node:
    def __init__(self, data=None, id=None):
        self.data = data
        self.id = id
        self.prev = None
        self.next = None

class SistemPendaftaranLowongan:
    def __init__(self):
        self.head = None
        self.tail = None
        self.admin_username = "admin"
        self.admin_password = "sistem informasi"
        self.id_counter = 1  #saya menambah Inisialisasi counter ID di sini untuk mensorting nantinya

    def generate_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id

    def tambah_pelamar(self, nama, email, telepon, pengalaman, keahlian, lowongan, posisi="akhir"):
        id = self.generate_id()  # Menghasilkan ID untuk pelamar
        new_node = Node({
            "nama": nama,
            "email": email,
            "telepon": telepon,
            "pengalaman": pengalaman,
            "keahlian": keahlian,
            "lowongan": lowongan
        }, id)

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
            if new_node.next is None:
                self.tail = new_node
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
            print(f"Data pelamar dengan ID {current.id} berhasil dihapus.")
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
            while current:
                print(f"ID: {current.id}, Nama: {current.data['nama']}, Email: {current.data['email']}, Telepon: {current.data['telepon']}, Pengalaman: {current.data['pengalaman']}, Keahlian: {current.data['keahlian']}, Lowongan: {current.data['lowongan']}")
                current = current.next

    def daftar_sebagai_pelamar(self, posisi="akhir"):
        nama = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        telepon = input("Masukkan telepon: ")
        pengalaman = input("Masukkan pengalaman: ")
        keahlian = input("Masukkan keahlian (pisahkan dengan koma): ").split(',')
        print("Pilihan lowongan:")
        print("1. Web Developer")
        print("2. UI/UX Designer")
        print("3. Software Developer")
        lowongan_input = input("Masukkan nomor lowongan yang diminati: ")
        if lowongan_input == "1":
            lowongan = "Web Developer"
        elif lowongan_input == "2":
            lowongan = "UI/UX Designer"
        elif lowongan_input == "3":
            lowongan = "Software Developer"
        else:
            print("Pilihan lowongan tidak valid.")
            return
        self.tambah_pelamar(nama, email, telepon, pengalaman, keahlian, lowongan, posisi)
        print("##########################")
        print("Data berhasil di tambahkan")
        print("###########################")

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
            print("Pilihan lowongan:")
            print("1. Web Developer")
            print("2. UI/UX Designer")
            print("3. Software Developer")
            lowongan_input = input("Masukkan nomor lowongan baru: ")
            if lowongan_input == "1":
                lowongan = "Web Developer"
            elif lowongan_input == "2":
                lowongan = "UI/UX Designer"
            elif lowongan_input == "3":
                lowongan = "Software Developer"
            else:
                print("Pilihan lowongan tidak valid.")
                return
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

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def merge_sort(self, arr, key, reverse):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = self.merge_sort(left_half, key, reverse)
        right_half = self.merge_sort(right_half, key, reverse)

        return self.merge(left_half, right_half, key, reverse)

    def merge(self, left, right, key, reverse):
        result = []
        while left and right:
            if reverse:
                if left[0][key] >= right[0][key]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            else:
                if left[0][key] <= right[0][key]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result

    def sorting_pelamar(self, key, order):
        pelamar_list = []
        current = self.head
        while current:
            pelamar_list.append({"id": current.id, **current.data})  # Menambahkan ID ke dalam data pelamar
            current = current.next

        if key not in pelamar_list[0]:
            print("Atribut yang diminta tidak tersedia.")
            return

        if order.lower() == "asc":
            sorted_pelamar = self.merge_sort(pelamar_list, key, False)
        elif order.lower() == "desc":
            sorted_pelamar = self.merge_sort(pelamar_list, key, True)
        else:
            print("Order sorting tidak valid.")
            return

        print("\nData Pelamar setelah sorting:")
        for pelamar in sorted_pelamar:
            print(f"ID: {pelamar['id']}, Nama: {pelamar['nama']}, {key.capitalize()}: {pelamar[key]}")

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
                print("5. Sorting pelamar")
                print("6. Keluar")

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
                    key = input("Masukkan atribut untuk sorting (id, nama): ")
                    order = input("Masukkan order sorting (asc/desc): ")
                    self.sorting_pelamar(key, order)
                elif pilihan == "6":
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
