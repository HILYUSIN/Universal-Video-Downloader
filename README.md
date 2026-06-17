# 🚀 Cara Install Universal Video Downloader

Panduan ini dibuat untuk pengguna yang belum pernah menggunakan Python atau Command Prompt sebelumnya.

---

# 📥 Langkah 1 - Download Aplikasi

1. Klik tombol hijau **Code** di halaman GitHub.
2. Pilih **Download ZIP**.
3. Tunggu hingga proses download selesai.
4. Klik kanan file ZIP yang sudah didownload.
5. Pilih **Extract All...**.
6. Klik **Extract**.

Sekarang Anda akan memiliki folder aplikasi yang siap digunakan.

---

# 🐍 Langkah 2 - Install Python

Aplikasi ini membutuhkan Python agar dapat berjalan.

1. Download Python dari website resmi:

   https://www.python.org/downloads/

2. Download versi terbaru.

3. Jalankan file installer yang sudah didownload.

4. Saat jendela instalasi muncul, pastikan Anda mencentang:

```text
✓ Add Python to PATH
```

5. Klik **Install Now**.

6. Tunggu hingga proses instalasi selesai.

---

# ✅ Langkah 3 - Cek Python Berhasil Terinstall

1. Tekan tombol Windows.
2. Ketik:

```text
cmd
```

3. Buka Command Prompt.

4. Ketik:

```cmd
python --version
```

5. Tekan Enter.

Jika muncul seperti berikut:

```text
Python 3.x.x
```

berarti Python berhasil terinstall.

---

# 📦 Langkah 4 - Install Komponen Aplikasi

1. Buka folder aplikasi yang sudah diekstrak.

2. Klik bagian paling atas File Explorer yang berisi alamat folder.

Contoh:

```text
C:\Downloads\Universal-Video-Downloader
```

3. Ketik:

```text
cmd
```

4. Tekan Enter.

Command Prompt akan terbuka pada folder aplikasi.

5. Jalankan perintah berikut:

```cmd
pip install -r requirements.txt
```

6. Tunggu hingga proses selesai.

Jika tidak muncul tulisan ERROR berwarna merah, berarti proses instalasi berhasil.

Jika muncul error bahwa pip tidak ditemukan, jalankan:

```cmd
python -m pip install -r requirements.txt
```

---

# ▶️ Langkah 5 - Jalankan Aplikasi

Masih di Command Prompt yang sama, jalankan:

```cmd
python yt_downloader.py
```

Tunggu beberapa saat.

Saat pertama kali dijalankan, aplikasi mungkin akan mengunduh komponen tambahan yang diperlukan secara otomatis. Tunggu hingga proses selesai.

Setelah itu aplikasi akan terbuka dan siap digunakan.

---

# 📖 Cara Menggunakan

## Download Video (MP4)

1. Pilih mode **Video (MP4)**.
2. Paste link video.
3. Pilih folder penyimpanan.
4. Klik **Download**.

---

## Download Audio (MP3)

1. Pilih mode **Audio (MP3)**.
2. Paste link video.
3. Pilih folder penyimpanan.
4. Klik **Download**.

---

## Download Banyak Video Sekaligus

Masukkan satu URL per baris.

Contoh:

```text
https://youtube.com/watch?v=xxxx

https://www.tiktok.com/@user/video/xxxx

https://www.instagram.com/p/xxxx
```

Aplikasi akan memproses semua link secara otomatis.

---

# 🌐 Platform yang Didukung

* YouTube
* YouTube Shorts
* TikTok
* Instagram
* Facebook
* X (Twitter)
* Dan berbagai platform video lainnya yang didukung oleh yt-dlp

---

# ❓ Troubleshooting

## Python Tidak Ditemukan

Jika muncul pesan:

```text
'python' is not recognized
```

Install ulang Python dan pastikan opsi:

```text
✓ Add Python to PATH
```

dicentang saat instalasi.

---

## Gagal Install Requirements

Coba jalankan:

```cmd
python -m pip install -r requirements.txt
```

---

## Gagal Download Video

Periksa:

* Koneksi internet aktif.
* Link video masih tersedia.
* Link yang dimasukkan benar.
* Platform masih didukung.

---

# 🎉 Selesai

Sekarang aplikasi sudah siap digunakan untuk mengunduh video maupun audio dari berbagai platform dengan mudah.
