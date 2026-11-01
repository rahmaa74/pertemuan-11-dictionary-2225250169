# Fungsi untuk mencari data mahasiswa
def cari_mahasiswa(data, nim):
    return data.get(nim)


# Fungsi untuk menghitung rata-rata nilai mahasiswa
def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


# Data awal mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# 1. Pencarian data mahasiswa
print("=== PENCARIAN DATA MAHASISWA ===")

nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")


# 2. Pencarian NIM yang tidak tersedia
print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")

nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")


# 3. Menambahkan mahasiswa baru
print("\n=== MENAMBAHKAN MAHASISWA ===")

data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Mahasiswa A006 berhasil ditambahkan.")


# 4. Mengubah nilai mahasiswa
print("\n=== MENGUBAH NILAI MAHASISWA ===")

data_mahasiswa["A002"]["nilai"] = 82

print("Nilai Budi berhasil diubah menjadi 82.")


# 5. Menampilkan seluruh data mahasiswa
print("\n=== SELURUH DATA MAHASISWA ===")

for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim}")
    print(f"Nama: {info['nama']}")
    print(f"Kelas: {info['kelas']}")
    print(f"Nilai: {info['nilai']}")
    print("------------------------")


# 6. Menghitung rata-rata nilai mahasiswa
print("\n=== RATA-RATA NILAI MAHASISWA ===")

rata_rata = rata_rata_nilai(data_mahasiswa)

print(f"Rata-rata nilai = {rata_rata:.2f}")
# Praktikum Pertemuan 11 - Dictionary Python