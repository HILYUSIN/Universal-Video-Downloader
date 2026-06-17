"""
Auto-installer untuk FFmpeg
Script ini akan otomatis download dan install FFmpeg untuk Windows
"""

import os
import sys
import platform
import urllib.request
import zipfile
import shutil
from pathlib import Path

def get_ffmpeg_url():
    """Get FFmpeg download URL based on OS"""
    system = platform.system()
    
    if system == "Windows":
        # FFmpeg essentials build untuk Windows
        return "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    elif system == "Darwin":  # macOS
        print("Untuk macOS, gunakan Homebrew:")
        print("brew install ffmpeg")
        return None
    elif system == "Linux":
        print("Untuk Linux, gunakan package manager:")
        print("sudo apt install ffmpeg  # Debian/Ubuntu")
        print("sudo yum install ffmpeg  # CentOS/RHEL")
        return None
    else:
        print(f"OS {system} tidak didukung untuk auto-install")
        return None

def download_ffmpeg(url, output_path):
    """Download FFmpeg dengan progress bar"""
    print(f"\n📥 Mendownload FFmpeg...")
    print(f"URL: {url}")
    print("Ini mungkin memakan waktu beberapa menit tergantung koneksi internet...\n")
    
    def progress_hook(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        bar_length = 50
        filled = int(bar_length * percent / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        mb_downloaded = (count * block_size) / (1024 * 1024)
        mb_total = total_size / (1024 * 1024)
        
        sys.stdout.write(f'\r[{bar}] {percent}% ({mb_downloaded:.1f}/{mb_total:.1f} MB)')
        sys.stdout.flush()
    
    try:
        urllib.request.urlretrieve(url, output_path, progress_hook)
        print("\n✓ Download selesai!")
        return True
    except Exception as e:
        print(f"\n✗ Error saat download: {e}")
        return False

def extract_ffmpeg(zip_path, extract_to):
    """Extract FFmpeg dari ZIP"""
    print(f"\n📦 Mengekstrak FFmpeg...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("✓ Ekstrak selesai!")
        return True
    except Exception as e:
        print(f"✗ Error saat ekstrak: {e}")
        return False

def find_ffmpeg_exe(extract_dir):
    """Cari file ffmpeg.exe di folder hasil ekstrak"""
    for root, dirs, files in os.walk(extract_dir):
        if 'ffmpeg.exe' in files:
            return os.path.join(root, 'ffmpeg.exe')
    return None

def install_ffmpeg():
    """Main installation function"""
    print("=" * 60)
    print("  FFmpeg Auto-Installer untuk Universal Video Downloader")
    print("=" * 60)
    
    # Cek OS
    system = platform.system()
    print(f"\n🖥️  OS terdeteksi: {system}")
    
    if system != "Windows":
        print("\n⚠️  Auto-installer hanya untuk Windows.")
        url = get_ffmpeg_url()
        return False
    
    # Cek apakah FFmpeg sudah ada
    app_dir = Path(__file__).parent
    ffmpeg_exe = app_dir / "ffmpeg.exe"
    
    if ffmpeg_exe.exists():
        print(f"\n✓ FFmpeg sudah terinstall di: {ffmpeg_exe}")
        response = input("\nInstall ulang? (y/n): ").lower()
        if response != 'y':
            print("Dibatalkan.")
            return True
    
    # Get download URL
    url = get_ffmpeg_url()
    if not url:
        return False
    
    # Setup paths
    temp_dir = app_dir / "temp_ffmpeg"
    temp_dir.mkdir(exist_ok=True)
    zip_path = temp_dir / "ffmpeg.zip"
    
    try:
        # Download
        if not download_ffmpeg(url, zip_path):
            return False
        
        # Extract
        if not extract_ffmpeg(zip_path, temp_dir):
            return False
        
        # Find ffmpeg.exe
        print("\n🔍 Mencari ffmpeg.exe...")
        ffmpeg_source = find_ffmpeg_exe(temp_dir)
        
        if not ffmpeg_source:
            print("✗ ffmpeg.exe tidak ditemukan dalam file ZIP")
            return False
        
        print(f"✓ Ditemukan: {ffmpeg_source}")
        
        # Copy ke folder aplikasi
        print(f"\n📋 Menyalin ke: {ffmpeg_exe}")
        shutil.copy2(ffmpeg_source, ffmpeg_exe)
        
        # Cleanup
        print("\n🧹 Membersihkan file sementara...")
        shutil.rmtree(temp_dir)
        
        print("\n" + "=" * 60)
        print("✅ FFmpeg berhasil diinstall!")
        print("=" * 60)
        print(f"\nLokasi: {ffmpeg_exe}")
        print("\nSekarang Anda bisa download audio/musik ke format MP3!")
        print("Jalankan aplikasi dengan: python yt_downloader.py")
        
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        # Cleanup on error
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        return False

if __name__ == "__main__":
    try:
        success = install_ffmpeg()
        input("\nTekan Enter untuk keluar...")
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Instalasi dibatalkan oleh user")
        sys.exit(1)
