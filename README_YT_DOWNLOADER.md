# Universal Video Downloader

Aplikasi desktop untuk download video dan musik dari **berbagai platform** dengan GUI yang mudah digunakan.

## Fitur

✅ **Download Video (MP4)** - Download video dalam format MP4  
✅ **Download Audio/Music (MP3)** - Download hanya audio/musik  
✅ **Multi-Platform Support** - Mendukung 1000+ platform termasuk:
   - 🎥 YouTube & YouTube Music
   - 📷 Instagram (Posts, Reels, Stories, IGTV)
   - 🎵 TikTok
   - 📘 Facebook & Facebook Watch
   - 🐦 Twitter/X
   - 📺 Vimeo
   - 🎬 Dailymotion
   - 📱 Twitch
   - Dan banyak lagi!

✅ **Multi-Download** - Download lebih dari 1 URL sekaligus  
✅ **Pilih Lokasi Simpan** - Bebas pilih folder penyimpanan  
✅ **Progress Bar** - Progress bar untuk setiap download dan overall progress  
✅ **Log Console** - Monitor real-time semua aktivitas download  

---

## Setup & Instalasi

### 1. Install Python
Pastikan Python 3.8+ sudah terinstall di komputer Anda.

Cek versi Python:
```bash
python --version
```

Jika belum ada, download dari: https://www.python.org/downloads/

### 2. Install Dependencies

Buka Command Prompt atau Terminal di folder aplikasi, lalu jalankan:

```bash
pip install -r requirements.txt
```

**PENTING untuk Download Audio (MP3):**  
Untuk convert audio ke MP3, Anda perlu install **FFmpeg**:

#### Windows:
1. Download FFmpeg dari: https://www.gyan.dev/ffmpeg/builds/
2. Extract file zip
3. Tambahkan folder `bin` ke system PATH, atau
4. Copy `ffmpeg.exe` ke folder aplikasi

#### Linux/Mac:
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Mac
brew install ffmpeg
```

### 3. Jalankan Aplikasi

```bash
python yt_downloader.py
```

---

## Cara Penggunaan

### 1. Pilih Tipe Download
- **Video (MP4)**: Download video lengkap
- **Audio/Music (MP3)**: Download hanya audio/musik

### 2. Masukkan URL
- Masukkan satu atau lebih URL dari platform apapun
- Satu URL per baris
- Contoh URL yang didukung:
  ```
  https://www.youtube.com/watch?v=dQw4w9WgXcQ
  https://www.instagram.com/p/ABC123/
  https://www.tiktok.com/@user/video/123456
  https://www.facebook.com/watch/?v=123456
  https://twitter.com/user/status/123456
  https://vimeo.com/123456
  ```

### 3. Pilih Lokasi Penyimpanan
- Klik tombol **Browse...** untuk pilih folder
- Default: folder Downloads

### 4. Klik Download
- Tombol **Download** untuk mulai
- Monitor progress di progress bar
- Lihat log detail di console

### 5. Kontrol Tambahan
- **Clear URLs**: Hapus semua URL yang dimasukkan
- **Clear Logs**: Bersihkan log console

---

## Platform yang Didukung

Aplikasi ini menggunakan **yt-dlp** yang mendukung 1000+ platform, termasuk:

### Video Sharing
- YouTube, YouTube Music, YouTube Shorts
- Vimeo, Dailymotion
- TikTok
- Twitch (VODs & Clips)

### Social Media
- Instagram (Posts, Reels, Stories, IGTV)
- Facebook & Facebook Watch
- Twitter/X
- Reddit

### Streaming
- Twitch
- StreamRecorder
- Periscope

### Dan banyak lagi!
Lihat daftar lengkap: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## Troubleshooting

### Error: "yt-dlp belum terinstall"
```bash
pip install yt-dlp
```

### Error saat download MP3: "ffmpeg not found"
Install FFmpeg (lihat instruksi di atas)

### Video tidak bisa didownload
- Pastikan URL valid
- Coba gunakan URL langsung (bukan short link)
- Beberapa video mungkin dibatasi region/copyright
- Beberapa platform memerlukan login (tidak didukung otomatis)

### Instagram/Facebook download gagal
- Untuk konten private, download mungkin tidak bisa
- Gunakan URL langsung, bukan short link
- Beberapa konten dibatasi platform

### TikTok download gagal
- Gunakan URL lengkap dari browser, bukan dari app
- Beberapa video mungkin region-locked

### Download lambat
- Kecepatan tergantung koneksi internet
- Untuk video kualitas tinggi, ukuran file lebih besar
- Beberapa platform membatasi kecepatan download

---

## Tips & Tricks

1. **Download Playlist**: Masukkan URL playlist untuk download semua video (YouTube, Vimeo, dll)
2. **Kualitas Terbaik**: Aplikasi otomatis pilih kualitas terbaik yang tersedia
3. **Format Audio**: MP3 dengan bitrate 192kbps (kualitas tinggi)
4. **Nama File**: File otomatis dinamai sesuai judul video/musik
5. **Batch Download**: Copy-paste banyak URL sekaligus untuk download massal
6. **Instagram Reels**: Sama seperti download post biasa
7. **Twitter Video**: Pastikan tweet berisi video/GIF

---

## Contoh URL untuk Berbagai Platform

```
# YouTube
https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID
https://music.youtube.com/watch?v=VIDEO_ID

# Instagram
https://www.instagram.com/p/POST_ID/
https://www.instagram.com/reel/REEL_ID/

# TikTok
https://www.tiktok.com/@username/video/1234567890
https://vt.tiktok.com/SHORT_ID/

# Facebook
https://www.facebook.com/watch/?v=VIDEO_ID
https://fb.watch/SHORT_ID/

# Twitter/X
https://twitter.com/username/status/TWEET_ID
https://x.com/username/status/TWEET_ID

# Vimeo
https://vimeo.com/VIDEO_ID
```

---

## Dependencies

- **Python 3.8+**
- **yt-dlp**: Library utama untuk download dari berbagai platform
- **tkinter**: GUI (sudah built-in di Python)
- **FFmpeg**: (Opsional) Untuk convert audio ke MP3

---

## FAQ

**Q: Apakah aplikasi ini gratis?**  
A: Ya, sepenuhnya gratis dan open source.

**Q: Apakah aman digunakan?**  
A: Ya, aplikasi ini menggunakan library resmi yt-dlp yang aman.

**Q: Bisa download dari Spotify?**  
A: Tidak, streaming service berbayar seperti Spotify, Netflix, dll tidak didukung.

**Q: Apakah melanggar hukum?**  
A: Tergantung penggunaan. Download untuk keperluan pribadi umumnya legal, tapi redistribusi tanpa izin melanggar copyright.

**Q: Kenapa beberapa video tidak bisa didownload?**  
A: Video mungkin private, region-locked, atau platform membatasi akses.

---

## Lisensi

Free to use. Gunakan dengan bijak dan patuhi hak cipta konten yang didownload.

---

## Catatan Penting

⚠️ **Disclaimer**: 
- Aplikasi ini hanya untuk keperluan pribadi dan edukasi
- Patuhi Terms of Service dari setiap platform
- Hormati hak cipta konten creator
- Jangan gunakan untuk tujuan komersial tanpa izin
- Redistribusi konten yang didownload tanpa izin adalah ilegal

---

## Update Log

**v2.0** - Universal Platform Support
- ✅ Mendukung 1000+ platform (Instagram, TikTok, Facebook, Twitter, dll)
- ✅ UI diperbaharui dengan info platform yang didukung
- ✅ Performa download ditingkatkan

**v1.0** - Initial Release
- ✅ Download YouTube video & music
- ✅ Multi-download support
- ✅ Progress bar & logging
