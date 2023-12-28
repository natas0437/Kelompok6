import datetime

data_parkir = []
riwayat_parkir = []
riwayat_parkir2 = []

class Transaksi:
    def __init__(self, plat_nomor, tipe_kendaraan, waktu_masuk, waktu_keluar, tarif, denda):
        self.plat_nomor = plat_nomor
        self.tipe_kendaraan = tipe_kendaraan
        self.waktu_masuk = waktu_masuk
        self.waktu_keluar = waktu_keluar
        self.tarif = tarif
        self.denda = denda

def savedWaktuMasuk():
    waktu_masuk = datetime.datetime.now()
    return waktu_masuk

def savedWaktuKeluar():
    waktu_keluar = datetime.datetime.now()
    return waktu_keluar

def hitung_biaya_parkir(waktu_masuk, waktu_keluar):
    selisih_waktu = waktu_keluar - waktu_masuk
    total_detik = selisih_waktu.total_seconds()

    waktu_parkir = int(total_detik / 60) * 60 + 60 
    
    if waktu_parkir > 240:
        waktu_parkir = 240

    tarif_per_detik = 10000 / 60
    
    biaya_parkir = waktu_parkir * tarif_per_detik
    
    return biaya_parkir

def proses_pembayaran(biaya, pembayaran):
    try:
        pembayaran = int(pembayaran)
        kembalian = pembayaran - biaya
        if kembalian < 0:
            raise ValueError("Pembayaran tidak cukup")
        return kembalian
    except ValueError as ve:
        print("Error:", ve)
        return None
    
def denda_parkir(waktu_masuk, waktu_keluar):
    selisih_waktu = waktu_keluar - waktu_masuk
    total_detik = selisih_waktu.total_seconds()

    maksimal_waktu = 240
    
    if total_detik > maksimal_waktu:
        denda = 0.1 * 40000

        if total_detik > 360:
            denda += 0.15

        return min(denda, 40000)
    else:
        return 0

def proses_keluar(transaksi):
    konfirmasi_plat_nomor = input('Masukkan Plat kendaraan anda: ')
    durasi = (transaksi.waktu_keluar - transaksi.waktu_masuk).total_seconds()

    total_biaya = hitung_biaya_parkir(transaksi.waktu_masuk, transaksi.waktu_keluar)
    denda = denda_parkir(transaksi.waktu_masuk, transaksi.waktu_keluar)

    total_biaya += denda

    print("\n\n=====")
    print(f"Total Biaya: {total_biaya}")
    print("=====")

    pembayaran = input("Masukkan Jumlah Pembayaran: ")
    kembalian = proses_pembayaran(total_biaya, pembayaran)

    if kembalian is not None:
        print(f"Kembalian: {kembalian}")
        print('Terima Kasih')
    else:
        print("Proses pembayaran dibatalkan")

def menu():
    while True:
        print("\n=====Selamat Datang di Anggrek Mall=====")
        print("Silahkan pilih kategori: ")
        print("1. Masuk Area Parkir")
        print("2. Keluar Area Parkir")
        print("3. Admin Parkir")
        print("4. Keluar")
        print("==========================================")

        pilihan = input("Masukkan nomor menu yang ingin Anda pilih: ")

        if pilihan == '1':
            tipe_kendaraan = input("Masukkan Tipe Kendaraan Anda (1 = Motor, 2 = Mobil): ")
            if tipe_kendaraan in ['1', '2']:
                plat_nomor = input("Masukkan Plat Kendaraan Anda: ")
                transaksi = Transaksi(plat_nomor, tipe_kendaraan, datetime.datetime.now(), None, 0, 0)
                waktu_masuk = savedWaktuMasuk()
                data_parkir.append(transaksi)
                riwayat_parkir.append({"data_plat": plat_nomor, "data_masuk": waktu_masuk})
                print("Kendaraan anda sudah tercatat!")
                print(f'Waktu masuk: {waktu_masuk.strftime("%Y-%m-%d %H:%M:%S")}')
                print('Silahkan Masuk')
            else:
                print("Input tidak valid. Silahkan masukkan nomor yang valid!")
        elif pilihan == '2':
            if len(data_parkir) > 0:
                transaksi = data_parkir.pop()
                transaksi.waktu_keluar = datetime.datetime.now()
                waktu_keluar = savedWaktuKeluar()
                proses_keluar(transaksi)
                print(f'Waktu keluar: {waktu_keluar.strftime("%Y-%m-%d %H:%M:%S")}')
                for data in riwayat_parkir:
                    plat = data['data_plat']
                    masuk = data['data_masuk']
                    riwayat_parkir2.append({"riwayat_plat": plat, "riwayat_masuk": masuk, "riwayat_keluar": waktu_keluar})
            else:
                print("Tidak ada data transaksi untuk dikeluarkan")
        elif pilihan == '3':
            input_pin = int(input("Masukkan PIN: "))
            if input_pin == 1:
                print("Data parkiran: ")
                for entry in riwayat_parkir2:
                    print(f" Plat Nomor: {entry['riwayat_plat']}\n Masuk: {entry['riwayat_masuk']}\n Keluar: {entry['riwayat_keluar']}\n")
            else:
                print("PIN Salah, Kamu tidak dapat mengakses fitur Admin!")
        elif pilihan == '4':
            print("Sampai jumpa lagi")
            break
        else:
            print("\n\n=====")
            print("Input tidak valid, silahkan coba lagi")

menu()
