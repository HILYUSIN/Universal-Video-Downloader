# 🎬 Universal Video Downloader

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-green.svg)
![License](https://img.shields.io/badge/License-Free-brightgreen.svg)

**Aplikasi desktop simpel untuk download video & musik dari 1000+ platform**

[🚀 Quick Start](#-cara-install-untuk-pemula) | [📖 Dokumentasi](#-cara-penggunaan) | [❓ FAQ](#-faq) | [🐛 Report Bug](../../issues)

</div>

---

## 📸 Screenshot

```
┌─────────────────────────────────────────────────┐
│  Universal Video Downloader                     │
│  ✓ YouTube  ✓ Instagram  ✓ TikTok  ✓ Facebook  │
├─────────────────────────────────────────────────┤
│  📥 Tipe Download:  ⚪ Video (MP4)  ⚪ Audio    │
│                                                  │
│  🔗 URL Video (Semua Platform):                │
│  ┌─────────────────────────────────────────┐   │
│  │ Paste link di sini...                   │   │
│  │                                          │   │
│  └─────────────────────────────────────────┘   │
│                                                  │
│  📁 Lokasi: C:\Users\...\Downloads  [Browse]   │
│                                                  │
│  [📥 Download] [🗑 Clear URLs] [🗑 Clear Logs]  │
│                                                  │
│  📊 Progress: ████████████░░░░ 75%             │
│  ⏱ Log Console: Downloading... 5.2MB/s         │
└─────────────────────────────────────────────────┘
```

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 🌐 **Multi-Platform** | YouTube, Instagram, TikTok, Facebook, Twitter, Vimeo, dan 1000+ lainnya |
| 🎬 **Video & Audio** | Download video MP4 atau ekstrak audio ke MP3 |
| 📦 **Batch Download** | Download banyak video sekaligus |
| 📊 **Progress Bar** | Pantau progress download secara real-time |
| 📁 **Pilih Lokasi** | Bebas pilih folder penyimpanan |
| 🖥️ **GUI Friendly** | Interface sederhana dan mudah digunakan |
| 🆓 **100% Gratis** | Open source, tanpa iklan, tanpa malware |

---

## 🚀 Cara Install untuk Pemula

### **Opsi 1: Download dari GitHub (MUDAH)** ⭐ Recommended

#### Langkah 1: Download Aplikasi
1. **Klik tombol hijau "Code"** di bagian atas halaman GitHub ini
2. **Pilih "Download ZIP"**
3. **Ekstrak file ZIP** ke folder yang Anda inginkan (misalnya: `C:\Downloads\video-downloader`)

#### Langkah 2: Install Python
1. **Download Python** dari: https://www.python.org/downloads/
   - Pilih versi terbaru (Python 3.8 atau lebih baru)
2. **Jalankan installer** yang sudah didownload
3. ⚠️ **PENTING**: Centang "Add Python to PATH" sebelum install!
4. Klik **"Install Now"**
5. Tunggu sampai selesai

#### Langkah 3: Install Dependencies
1. **Buka folder aplikasi** yang sudah diekstrak
2. **Klik pada address bar** di File Explorer (bagian atas yang menampilkan path)
3. **Ketik `cmd`** lalu tekan Enter (akan membuka Command Prompt di folder tersebut)
4. **Copy paste command ini**:
   ```bash
   pip install -r requirements.txt
   ```
5. Tekan **Enter** dan tunggu sampai selesai

#### Langkah 4: Install FFmpeg (untuk download MP3) ⭐ AUTO-INSTALLER!

**Windows - MUDAH! Auto-Installer tersedia:**
1. **Otomatis**: Jalankan aplikasi, pilih mode Audio, aplikasi akan menawarkan auto-install FFmpeg
2. **Manual**: Jalankan `python install_ffmpeg.py` di folder aplikasi
3. **Alternatif**: Download manual dari https://www.gyan.dev/ffmpeg/builds/ dan copy `ffmpeg.exe` ke folder aplikasi

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

💡 **Catatan**: Aplikasi akan otomatis deteksi FFmpeg dan menawarkan install jika tidak ditemukan!

#### Langkah 5: Jalankan Aplikasi
1. Di folder aplikasi, **double-click file `yt_downloader.py`**, atau
2. Buka Command Prompt di folder aplikasi dan ketik:
   ```bash
   python yt_downloader.py
   ```

✨ **Aplikasi akan otomatis cek FFmpeg saat startup dan menawarkan install jika diperlukan!**

---

### **Opsi 2: Clone dengan Git**

Jika Anda familiar dengan Git:

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/video-downloader.git
cd video-downloader

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python yt_downloader.py
```

---

## 📖 Cara Penggunaan

### 1️⃣ Pilih Tipe Download
- **Video (MP4)**: Download video lengkap dengan gambar dan suara
- **Audio/Music (MP3)**: Download hanya audionya, bagus untuk musik

### 2️⃣ Masukkan URL
Copy link video dari platform apapun, paste ke aplikasi:

| Platform | Contoh URL |
|----------|-----------|
| **YouTube** | `https://www.youtube.com/watch?v=dQw4w9WgXcQ` |
| **Instagram** | `https://www.instagram.com/p/ABC123/` |
| **TikTok** | `https://www.tiktok.com/@user/video/123456` |
| **Facebook** | `https://www.facebook.com/watch/?v=123456` |
| **Twitter** | `https://twitter.com/user/status/123456` |

**💡 Tips:** Untuk download banyak video, masukkan satu URL per baris!

### 3️⃣ Pilih Lokasi Penyimpanan
- Klik tombol **"Browse..."**
- Pilih folder tempat menyimpan video
- Default: Folder Downloads Anda

### 4️⃣ Klik Download!
- Tekan tombol **"Download"**
- Pantau progress di progress bar
- Lihat detail di log console

---

## 🌍 Platform yang Didukung

<details>
<summary>📺 Video Sharing (Klik untuk expand)</summary>

- YouTube (Video, Music, Shorts, Live)
- Vimeo
- Dailymotion
- Rumble
- Bitchute
</details>

<details>
<summary>📱 Social Media</summary>

- Instagram (Posts, Reels, Stories, IGTV)
- TikTok
- Facebook & Facebook Watch
- Twitter/X
- Reddit
- Pinterest
- LinkedIn
</details>

<details>
<summary>🎮 Streaming & Gaming</summary>

- Twitch (VODs, Clips)
- StreamRecorder
- Mixer
</details>

<details>
<summary>🎓 Educational</summary>

- Coursera
- Udemy
- Khan Academy
- TED Talks
</details>

**Dan 1000+ platform lainnya!**  
Lihat daftar lengkap: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## 🔧 Troubleshooting

<details>
<summary>❌ Error: "Python tidak ditemukan"</summary>

**Solusi:**
1. Install Python dari https://www.python.org/downloads/
2. Pastikan centang "Add Python to PATH" saat install
3. Restart Command Prompt
4. Coba lagi
</details>

<details>
<summary>❌ Error: "yt-dlp belum terinstall"</summary>

**Solusi:**
```bash
pip install yt-dlp
```
</details>

<details>
<summary>❌ Error saat download MP3: "ffmpeg not found"</summary>

**Solusi:**
- Install FFmpeg (lihat Langkah 4 di atas)
- Atau copy `ffmpeg.exe` ke folder aplikasi
</details>

<details>
<summary>❌ Video tidak bisa didownload</summary>

**Kemungkinan penyebab:**
- URL tidak valid atau video sudah dihapus
- Video private/region-locked
- Platform memerlukan login (tidak didukung)
- Koneksi internet bermasalah

**Solusi:**
- Pastikan URL benar dan video masih ada
- Coba URL langsung dari browser, bukan short link
- Pastikan koneksi internet stabil
</details>

<details>
<summary>❌ Instagram/TikTok download gagal</summary>

**Solusi:**
- Gunakan URL lengkap dari browser desktop
- Untuk konten private, download tidak bisa
- Update yt-dlp ke versi terbaru: `pip install --upgrade yt-dlp`
</details>

<details>
<summary>⚠️ Download sangat lambat</summary>

**Solusi:**
- Cek kecepatan internet Anda
- Beberapa platform membatasi kecepatan
- Pilih kualitas lebih rendah jika perlu
</details>

---

## 💡 Tips & Tricks

| Tip | Deskripsi |
|-----|-----------|
| 🎵 **Download Playlist** | Paste URL playlist YouTube untuk download semua video |
| 📦 **Batch Download** | Paste banyak URL sekaligus (satu per baris) |
| 🎬 **Instagram Reels** | URL sama seperti post biasa, langsung copy dari browser |
| 🎶 **YouTube Music** | Pilih mode Audio untuk kualitas musik terbaik |
| ⚡ **Kualitas Otomatis** | Aplikasi otomatis pilih kualitas terbaik yang tersedia |
| 📁 **Organisasi File** | Buat folder terpisah untuk setiap platform/kategori |

---

## 📋 Persyaratan Sistem

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **OS** | Windows 7 / macOS 10.12 / Linux | Windows 10 / macOS 11+ / Ubuntu 20.04+ |
| **Python** | 3.8+ | 3.10+ |
| **RAM** | 2 GB | 4 GB+ |
| **Storage** | 100 MB (app) + space untuk video | SSD dengan space cukup |
| **Internet** | 1 Mbps | 10 Mbps+ |

---

## ❓ FAQ

<details>
<summary><b>Q: Apakah aplikasi ini gratis?</b></summary>
A: Ya, 100% gratis dan open source. Tidak ada biaya tersembunyi.
</details>

<details>
<summary><b>Q: Apakah aman digunakan?</b></summary>
A: Ya, aplikasi ini menggunakan library resmi yt-dlp yang aman dan open source. Tidak ada malware atau spyware.
</details>

<details>
<summary><b>Q: Bisa download dari Spotify/Netflix?</b></summary>
A: Tidak. Streaming service berbayar seperti Spotify, Netflix, Disney+ tidak didukung karena dilindungi DRM.
</details>

<details>
<summary><b>Q: Apakah legal?</b></summary>
A: Download untuk keperluan pribadi umumnya legal, namun redistribusi atau penggunaan komersial tanpa izin melanggar copyright. Gunakan dengan bijak.
</details>

<details>
<summary><b>Q: Kenapa beberapa video tidak bisa didownload?</b></summary>
A: Video mungkin private, region-locked, atau platform membatasi download. Beberapa konten juga memerlukan login.
</details>

<details>
<summary><b>Q: Bagaimana cara update aplikasi?</b></summary>
A: 
```bash
# Update yt-dlp
pip install --upgrade yt-dlp

# Download versi terbaru aplikasi dari GitHub
```
</details>

<details>
<summary><b>Q: Bisa download video 4K/8K?</b></summary>
A: Ya, jika video tersedia dalam kualitas tersebut. Aplikasi otomatis pilih kualitas terbaik.
</details>

---

## 🤝 Kontribusi

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests
- ⭐ Star repo ini jika bermanfaat!

---

## 📜 Lisensi

Free to use untuk keperluan pribadi dan edukasi.

---

## ⚠️ Disclaimer

**PENTING - BACA DENGAN SEKSAMA:**

- ✅ Aplikasi ini **untuk keperluan pribadi dan edukasi**
- ✅ Gunakan dengan **bijak dan bertanggung jawab**
- ❌ **JANGAN** gunakan untuk tujuan komersial tanpa izin
- ❌ **JANGAN** redistribute konten yang didownload tanpa izin pemilik
- ⚖️ **PATUHI** Terms of Service dari setiap platform
- 💙 **HORMATI** hak cipta dan karya content creator

**Developer tidak bertanggung jawab atas penyalahgunaan aplikasi ini.**

---

## 🙏 Credits

- **yt-dlp**: https://github.com/yt-dlp/yt-dlp
- **FFmpeg**: https://ffmpeg.org/
- **Python**: https://www.python.org/

---

## 📞 Support

Jika ada masalah atau pertanyaan:
1. Cek [FAQ](#-faq) dan [Troubleshooting](#-troubleshooting)
2. Search di [Issues](../../issues) untuk melihat apakah sudah ada solusi
3. Buat [New Issue](../../issues/new) jika belum ada

---

<div align="center">

**Made with ❤️ for everyone who loves to download videos**

⭐ Star repo ini jika bermanfaat! ⭐

[⬆ Back to Top](#-universal-video-downloader)

</div>
