 # Pertemuan 03 — Seleksi dalam Python
## Identitas
- **Nama:** Shofwatunnida
- **NIM:** 2225250074
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Pertemuan:** 03
## Tujuan

Pada pertemuan ini, saya mempelajari penggunaan struktur seleksi dalam Python menggunakan `if`, `elif`, `else`, dan nested if. Program yang dibuat digunakan untuk menentukan kondisi berdasarkan input yang diberikan.

## Struktur Folder

- `latihan/01_genap_ganjil.py` — menentukan bilangan genap atau ganjil.
- `latihan/02_bandingkan_dua_bilangan.py` — membandingkan dua bilangan.
- `latihan/03_kelulusan_bersyarat.py` — menentukan kelulusan berdasarkan nilai dan kehadiran.
- `latihan/04_jenis_segitiga.py` — menentukan jenis segitiga berdasarkan panjang sisi.
- `tugas/analisis_persamaan_kuadrat.py` — menganalisis persamaan kuadrat berdasarkan nilai diskriminan.

## Cara Menjalankan Program

Program dapat dijalankan melalui terminal VS Code dengan perintah:

```bash
python nama_file.py
```

Contoh:

```bash
python latihan/01_genap_ganjil.py
```

## Algoritma

### Latihan 1 — Genap atau Ganjil

Program menerima sebuah bilangan bulat. Jika bilangan habis dibagi 2, maka bilangan tersebut dinyatakan genap. Jika tidak, maka dinyatakan ganjil.

### Latihan 2 — Membandingkan Dua Bilangan

Program menerima dua bilangan. Dengan menggunakan nested if, program membandingkan kedua bilangan dan menentukan apakah bilangan pertama lebih besar, lebih kecil, atau sama dengan bilangan kedua.

### Latihan 3 — Kelulusan Bersyarat

Program menerima nilai akhir dan persentase kehadiran. Mahasiswa dinyatakan lulus jika nilai akhir minimal 60 dan kehadiran minimal 80%. Jika salah satu syarat tidak terpenuhi, maka dinyatakan belum lulus.

### Latihan 4 — Jenis Segitiga

Program menerima tiga panjang sisi. Pertama, program memeriksa apakah ketiga sisi dapat membentuk segitiga. Jika valid, program menentukan jenis segitiga berdasarkan kesamaan panjang sisinya.

### Tugas 2 — Analisis Persamaan Kuadrat

Program menerima nilai `a`, `b`, dan `c` dari persamaan `ax² + bx + c = 0`. Jika `a = 0`, maka persamaan bukan merupakan persamaan kuadrat. Jika `a` tidak sama dengan 0, program menghitung diskriminan dengan rumus `D = b² - 4ac`. Nilai diskriminan digunakan untuk menentukan jenis akar dan menghitung akar jika memiliki akar real.

## Pengujian

| Program | Input | Hasil yang Diharapkan | Status |
|---|---|---|---|
| Genap/Ganjil | 88 | 88 adalah bilangan genap | Berhasil |
| Bandingkan | 7 dan 4 | Bilangan pertama lebih besar | Berhasil |
| Kelulusan | 75 dan 90 | Lulus | Berhasil |
| Jenis Segitiga | 3, 3, 3 | Segitiga sama sisi | Berhasil |
| Persamaan Kuadrat | 1, -5, 6 | D = 1,00; x1 = 3,00; x2 = 2,00 | Berhasil |
| Persamaan Kuadrat | 1, 2, 1 | D = 0,00; x = -1,00 | Berhasil |
| Persamaan Kuadrat | 1, 0, 1 | D = -4,00; tidak memiliki akar real | Berhasil |
| Persamaan Kuadrat | 0, 2, 3 | Bukan persamaan kuadrat | Berhasil |

## Refleksi

Pada pertemuan ini saya memahami bahwa struktur seleksi digunakan untuk membuat program dapat mengambil keputusan berdasarkan kondisi tertentu. Saya juga belajar menggunakan nested if dan memahami bahwa kondisi harus diperiksa secara berurutan agar hasil program sesuai dengan aturan yang diberikan. Dari latihan dan tugas yang dikerjakan, saya menjadi lebih terbiasa membuat program Python yang menggunakan percabangan.
