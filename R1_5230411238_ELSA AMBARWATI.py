# NAMA : ELSA AMBARWATI
# NPM : 5230411238
# KELAS : VIII
# MATKUL: PEMOGRAMAN BERIORIENTASI OBJEK
# RESPONSI

class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

class Transaksi:
    def __init__(self, no_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = []

    def add_produk(self, produk, jumlah):
        self.detail_transaksi.append((produk, jumlah))

    def total_harga(self):
        total = 0
        for produk, jumlah in self.detail_transaksi:
            total += produk.get_harga() * jumlah
        return total

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def get_harga(self):
        return self.harga

class Struk:
    def __init__(self, no_transaksi, nama_pegawai):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.detail_transaksi = []

    def add_detail(self, nama_produk, jumlah_produk, total_harga):
        self.detail_transaksi.append({
            "nama_produk": nama_produk,
            "jumlah_produk": jumlah_produk,
            "total_harga": total_harga,
        })

    def cetak_struk(self):
        print("=============================")
        print("       Struk Pembelian       ")
        print("=============================")
        print(f"No. Transaksi: {self.no_transaksi}")
        print(f"Nama Pegawai: {self.nama_pegawai}")
        print("-----------------------------")
        for detail in self.detail_transaksi:
            print(f"{detail['jumlah_produk']} x {detail['nama_produk']} = Rp{detail['total_harga']}")
        print("-----------------------------")
        print(f"Total: Rp{sum(item['total_harga'] for item in self.detail_transaksi)}")
        print("=============================")

class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk, harga)

class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk, harga)

class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk, harga)

def menu():
    print("\n=== Menu Transaksi ===")
    print("1. Tambah Pegawai")
    print("2. Tambah Transaksi")
    print("3. Tambah Produk")
    print("4. Hitung Total dan Tampilkan Struk")
    print("0. Keluar")

def main():
    pegawai = None
    transaksi = None
    produk_list = []

    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3/4/0): ")

        if pilihan == '1':
            nik = input("Masukkan NIK Pegawai (Angka): ")
            nama = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai = Pegawai(nik, nama, alamat)
            print("Pegawai berhasil ditambahkan.")

        elif pilihan == '2':
            if pegawai is None:
                print("Silakan masukkan pegawai terlebih dahulu.")
                continue
            no_transaksi = input("Masukkan No Transaksi (TR Angka): ")
            transaksi = Transaksi(no_transaksi)
            print("Transaksi berhasil ditambahkan.")

        elif pilihan == '3':
            kode_produk = input("Masukkan Kode Produk(SNK,MKN,MNM Angka): ")
            nama_produk = input("Masukkan Nama Produk: ")
            
            while True:
                try:
                    harga = float(input("Masukkan Harga Produk (Angka): "))
                    break
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk harga.")

            jenis_produk = input("Masukkan Jenis Produk (Snack/Makanan/Minuman): ")

            if jenis_produk.lower() == 'snack':
                produk = Snack(kode_produk, nama_produk, jenis_produk, harga)
            elif jenis_produk.lower() == 'makanan':
                produk = Makanan(kode_produk, nama_produk, jenis_produk, harga)
            elif jenis_produk.lower() == 'minuman':
                produk = Minuman(kode_produk, nama_produk, jenis_produk, harga)
            else:
                print("Jenis produk tidak valid.")
                continue

            produk_list.append(produk)
            print(f"Produk {nama_produk} berhasil ditambahkan.")

        elif pilihan == '4':
            if pegawai is None or transaksi is None or not produk_list:
                print("Pastikan Anda telah memasukkan pegawai, transaksi, dan produk terlebih dahulu.")
                continue

            print("=== Input Jumlah Produk ===")
            for produk in produk_list:
                while True:
                    try:
                        jumlah = int(input(f"Masukkan jumlah untuk {produk.nama_produk} (Angka): "))
                        break
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka untuk jumlah.")

                transaksi.add_produk(produk, jumlah)

            struk = Struk(transaksi.no_transaksi, pegawai.nama)
            for produk, jumlah in transaksi.detail_transaksi:
                struk.add_detail(produk.nama_produk, jumlah, produk.get_harga() * jumlah)

            struk.cetak_struk()

        elif pilihan == '0':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
