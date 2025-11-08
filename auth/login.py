akun = {}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in akun and akun[username] == password :
        print(f"Login berhasil. Selamat datang, {username}!")
    else:
        print ("Login gagal. Coba kembali.")