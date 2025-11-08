akun = {}

# Fungsi registrasi
def register():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    akun[username] = password

    # Cek apakah username dan password tidak kosong
    if username and password:
        print("Berhasil didaftarkan!")
    else:
        print("Gagal didaftarkan!")