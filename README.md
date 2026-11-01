# Pertemuan 11 - Dictionary/Map

**Nama:** Rahma Muhrohmah Jalianty

**NIM:** 2225250169

**Kelas:** 3f

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama.

Setiap mahasiswa memiliki value berupa dictionary yang
berisi nama, kelas, dan nilai.

## Struktur Folder

- latihan/
  - 01_dasar_dictionary.py
  - 02_akses_get.py
  - 03_manipulasi_dictionary.py
  - 04_iterasi_dictionary.py
  - 05_dictionary_bersarang.py
  - 06_fungsi_dictionary.py
- praktik/
  - data_mahasiswa.py

## Cara Menjalankan

Jalankan program melalui terminal VS Code:

python praktik/data_mahasiswa.py

## Test Case

| Kasus | Input/Aksi | Hasil |
|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan |
| Pencarian tidak tersedia | A999 | Data tidak ditemukan |
| Pembaruan nilai | A002 menjadi 82 | Nilai berubah menjadi 82 |
| Penambahan data | A006 | Data Fajar berhasil ditambahkan |
| Rekap | items() | Seluruh data mahasiswa tampil |
| Rata-rata | Seluruh nilai | 83.50 |

## Refleksi

Kesalahan yang perlu dihindari dalam penggunaan
dictionary adalah KeyError, yaitu kesalahan yang
terjadi ketika program mengakses key yang tidak tersedia.

Untuk mengatasinya, dapat digunakan method get()
atau operator in sebelum mengakses data.

Melalui praktikum ini, saya memahami cara membuat,
mengakses, menambahkan, mengubah, dan menghapus
data menggunakan dictionary dalam Python.
## Refleksi
Melalui praktikum ini, saya memahami penggunaan dictionary
dalam Python untuk menyimpan data berdasarkan pasangan key-value.
Saya juga belajar mengakses, mengubah, menghapus, dan
menampilkan data menggunakan dictionary.