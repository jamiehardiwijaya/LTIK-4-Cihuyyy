from datetime import datetime

# List untuk menyimpan bahan makanan
bahan_makanan = []

def tambah_bahan():
    nama = input("Masukkan nama bahan: ")
    jumlah = input("Masukkan jumlah: ")
    tanggal = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
    
    bahan = {
        'nama': nama,
        'jumlah': jumlah,
        'tanggal_kadaluarsa': tanggal
    }
    bahan_makanan.append(bahan)
    print("Bahan berhasil ditambahkan!\n")

def hitung_hari_kadaluarsa(tanggal_str):
    try:
        tgl_kadaluarsa = datetime.strptime(tanggal_str, '%Y-%m-%d')
        hari_ini = datetime.now()
        selisih = (tgl_kadaluarsa - hari_ini).days
        return selisih
    except:
        return "Format salah"

def tampilkan_bahan():
    if not bahan_makanan:
        print("Belum ada bahan makanan yang tersimpan.\n")
        return
    
    print("\n=== DAFTAR BAHAN MAKANAN ===")
    for i, bahan in enumerate(bahan_makanan, 1):
        hari = hitung_hari_kadaluarsa(bahan['tanggal_kadaluarsa'])
        
        if isinstance(hari, int):
            if hari < 0:
                status = "KADALUARSA"
            elif hari == 0:
                status = "HARI INI"
            else:
                status = f"{hari} hari lagi"
        else:
            status = "Format salah"
        
        print(f"{i}. {bahan['nama']} - {bahan['jumlah']} - Kadaluarsa: {bahan['tanggal_kadaluarsa']} ({status})")
    print()

# Contoh data awal
bahan_makanan = [
    {'nama': 'Susu', 'jumlah': '2 botol', 'tanggal_kadaluarsa': '2024-12-25'},
    {'nama': 'Telur', 'jumlah': '10 butir', 'tanggal_kadaluarsa': '2024-12-20'},
    {'nama': 'Roti', 'jumlah': '1 bungkus', 'tanggal_kadaluarsa': '2024-12-18'}
]

# Program utama
while True:
    print("=== APLIKASI BAHAN MAKANAN ===")
    print("1. Tambah bahan makanan")
    print("2. Tampilkan semua bahan")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == '1':
        tambah_bahan()
    elif pilihan == '2':
        tampilkan_bahan()
    elif pilihan == '3':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!\n")
