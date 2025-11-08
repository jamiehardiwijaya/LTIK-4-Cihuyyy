import datetime
import json

#fungsi manajer makanan
class ManajerMakanan:
    def __init__(self):
        self.makanan = []
        self.file_data = "data_makanan.json"
        self.muat_data()
    
    def tambah_makanan(self):
        nama = input("Nama makanan: ")
        jumlah = input("Jumlah: ") or "1"
        tanggal = input("Tanggal kadaluarsa (YYYY-MM-DD): ")
        
        try:
            tgl_kadaluarsa = datetime.date.fromisoformat(tanggal)
            item = {
                'nama': nama,
                'jumlah': jumlah,
                'kadaluarsa': tanggal,
                'tgl_kadaluarsa': tgl_kadaluarsa
            }
            self.makanan.append(item)
            self.simpan_data()
            print(f"Berhasil tambah {nama}")
        except:
            print("Format tanggal salah!")
    
    def cek_kadaluarsa(self): #menampilkan waktu kadaluarsa
        hari_ini = datetime.date.today()
        ada_pengingat = False
        
        for item in self.makanan:
            sisa_hari = (item['tgl_kadaluarsa'] - hari_ini).days
            
            if sisa_hari <= 3:
                if not ada_pengingat:
                    print("\nPERINGATAN KADALUARSA:")
                    ada_pengingat = True
                
                if sisa_hari < 0:
                    status = "SUDAH KADALUARSA"
                elif sisa_hari == 0:
                    status = "KADALUARSA HARI INI"
                else:
                    status = f"{sisa_hari} hari lagi"
                
                print(f"- {item['nama']} ({item['jumlah']}) - {status}")
        
        if not ada_pengingat:
            print("\nTidak ada makanan yang hampir kadaluarsa")
    
    def lihat_semua(self):
        if not self.makanan:
            print("\nBelum ada data makanan")
            return
        
        print("\nDAFTAR MAKANAN:")
        for i, item in enumerate(self.makanan):
            sisa_hari = (item['tgl_kadaluarsa'] - datetime.date.today()).days
            status = "KADALUARSA" if sisa_hari < 0 else f"{sisa_hari} hari"
            print(f"{i+1}. {item['nama']} - {item['jumlah']} - {item['kadaluarsa']} ({status})")
    
    def hapus_makanan(self):
        self.lihat_semua()
        if self.makanan:
            try:
                nomor = int(input("Nomor yang dihapus: ")) - 1
                if 0 <= nomor < len(self.makanan):
                    nama = self.makanan[nomor]['nama']
                    self.makanan.pop(nomor)
                    self.simpan_data()
                    print(f"Berhasil hapus {nama}")
                else:
                    print("Nomor tidak valid")
            except:
                print("Input harus angka")
    
    def simpan_data(self):
        # Hapus tgl_kadaluarsa karena tidak bisa disimpan di JSON
        data_simpan = []
        for item in self.makanan:
            data_simpan.append({
                'nama': item['nama'],
                'jumlah': item['jumlah'],
                'kadaluarsa': item['kadaluarsa']
            })
        
        with open(self.file_data, 'w') as f:
            json.dump(data_simpan, f)
    
    def muat_data(self):
        try:
            with open(self.file_data, 'r') as f:
                data = json.load(f)
            
            self.makanan = []
            for item in data:
                tgl_kadaluarsa = datetime.date.fromisoformat(item['kadaluarsa'])
                self.makanan.append({
                    'nama': item['nama'],
                    'jumlah': item['jumlah'],
                    'kadaluarsa': item['kadaluarsa'],
                    'tgl_kadaluarsa': tgl_kadaluarsa
                })
        except:
            self.makanan = []

def main():
    app = ManajerMakanan()
    
    while True:
        print("\n=== APLIKASI KADALUARSA MAKANAN ===")
        print("1. Tambah Makanan")
        print("2. Cek Kadaluarsa")
        print("3. Lihat Semua")
        print("4. Hapus Makanan")
        print("5. Keluar")
        
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            app.tambah_makanan()
        elif pilih == "2":
            app.cek_kadaluarsa()
        elif pilih == "3":
            app.lihat_semua()
        elif pilih == "4":
            app.hapus_makanan()
        elif pilih == "5":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
