import numpy as np

print("Fitur Resep Sederhana")
resep = {
    "Nasi Goreng": ["nasi", "telur", "kecap", "bawang"],
    "Sayur Sop": ["wortel", "kentang", "kubis", "bawang putih"],
    "Telur Dadar": ["telur", "garam", "minyak"],
    "Tempe Goreng": ["tempe", "minyak", "bumbu halus"]
}

print("Masukkan bahan yang kamu punya (pisahkan dengan koma):")
input_user = input(">> ")

bahan_user = [b.strip().lower() for b in input_user.split(",")]
print("Bahan kamu: ", bahan_user)

bahan_user_array = np.array(bahan_user)
print("Rekomendasi Resep Berdasarkan Bahan Kamu")

rekomendasi = [] 

for nama_resep, bahan_resep in resep.items():
    bahan_resep_array = np.array(bahan_resep)

    cocok = np.isin(bahan_resep_array, bahan_user_array)
    jumlah_cocok = np.sum(cocok)
    total_bahan = len(bahan_resep_array)

    rasio = jumlah_cocok / total_bahan

    if rasio >= 0.5:
        rekomendasi.append((nama_resep, jumlah_cocok, total_bahan, round(rasio * 100, 1)))

if len(rekomendasi) == 0:
    print("Maaf, tidak ada resep yang cocok 😢")
else:
    for r in rekomendasi:
        print(f"- {r[0]} ({r[1]}/{r[2]} bahan cocok, {r[3]}%)")

semua_bahan = []

for bahan in resep.values():
    semua_bahan.extend(bahan)

semua_bahan_array = np.unique(np.array(semua_bahan))
print("Total bahan unik dalam semua resep:", len(semua_bahan_array))
print("Daftar bahan unik:", semua_bahan_array)
