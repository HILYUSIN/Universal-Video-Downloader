import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import threading
import os
from pathlib import Path
import queue
from datetime import datetime

try:
    from yt_dlp import YoutubeDL
except ImportError:
    pass  # Will be installed via requirements.txt

class UniversalDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Video Downloader")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        
        # Variables
        self.download_path = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.download_type = tk.StringVar(value="video")
        self.urls_queue = []
        self.is_downloading = False
        self.log_queue = queue.Queue()
        
        # Setup UI
        self.setup_ui()
        
        # Start log updater
        self.update_logs()
        
    def setup_ui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(6, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Universal Video Downloader", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)
        
        # Supported platforms info
        platforms_label = ttk.Label(main_frame, 
                                    text="✓ YouTube  ✓ Instagram  ✓ TikTok  ✓ Facebook  ✓ Twitter/X  ✓ Dan 1000+ platform lainnya", 
                                    font=('Arial', 9), foreground='#006400')
        platforms_label.grid(row=1, column=0, pady=(0, 10), sticky=tk.W)
        
        # Download Type Selection
        type_frame = ttk.LabelFrame(main_frame, text="Tipe Download", padding="10")
        type_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        type_frame.columnconfigure(1, weight=1)
        
        ttk.Radiobutton(type_frame, text="Video (MP4)", variable=self.download_type, 
                       value="video").grid(row=0, column=0, padx=(0, 20))
        ttk.Radiobutton(type_frame, text="Audio/Music (MP3)", variable=self.download_type, 
                       value="audio").grid(row=0, column=1, sticky=tk.W)
        
        # URL Input Section
        url_frame = ttk.LabelFrame(main_frame, text="URL Video (Semua Platform)", padding="10")
        url_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        url_frame.columnconfigure(0, weight=1)
        
        # URL entry with scrollbar
        self.url_text = scrolledtext.ScrolledText(url_frame, height=5, wrap=tk.WORD)
        self.url_text.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Label(url_frame, text="Masukkan URL dari YouTube, Instagram, TikTok, Facebook, Twitter, dll (satu per baris)", 
                 font=('Arial', 9, 'italic')).grid(row=1, column=0, sticky=tk.W)
        
        # Save Location Section
        save_frame = ttk.LabelFrame(main_frame, text="Lokasi Penyimpanan", padding="10")
        save_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        save_frame.columnconfigure(0, weight=1)
        
        path_entry_frame = ttk.Frame(save_frame)
        path_entry_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        path_entry_frame.columnconfigure(0, weight=1)
        
        ttk.Entry(path_entry_frame, textvariable=self.download_path, width=50).grid(
            row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        ttk.Button(path_entry_frame, text="Browse...", 
                  command=self.select_download_path).grid(row=0, column=1)
        
        # Control Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.download_btn = ttk.Button(button_frame, text="Download", 
                                       command=self.start_download, width=20)
        self.download_btn.grid(row=0, column=0, padx=(0, 5))
        
        ttk.Button(button_frame, text="Clear URLs", 
                  command=self.clear_urls, width=15).grid(row=0, column=1, padx=(0, 5))
        
        ttk.Button(button_frame, text="Clear Logs", 
                  command=self.clear_logs, width=15).grid(row=0, column=2)
        
        # Progress Section
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N), pady=(0, 10))
        progress_frame.columnconfigure(0, weight=1)
        
        # Overall progress
        ttk.Label(progress_frame, text="Overall Progress:").grid(row=0, column=0, sticky=tk.W)
        self.overall_progress = ttk.Progressbar(progress_frame, mode='determinate', length=400)
        self.overall_progress.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 10))
        
        self.overall_label = ttk.Label(progress_frame, text="0/0 selesai")
        self.overall_label.grid(row=2, column=0, sticky=tk.W)
        
        # Current download progress
        ttk.Label(progress_frame, text="Current Download:").grid(row=3, column=0, sticky=tk.W, pady=(10, 0))
        self.current_progress = ttk.Progressbar(progress_frame, mode='determinate', length=400)
        self.current_progress.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(2, 10))
        
        self.current_label = ttk.Label(progress_frame, text="Menunggu...")
        self.current_label.grid(row=5, column=0, sticky=tk.W)
        
        # Log Console
        log_frame = ttk.LabelFrame(main_frame, text="Log Console", padding="10")
        log_frame.grid(row=7, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 0))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_console = scrolledtext.ScrolledText(log_frame, height=10, wrap=tk.WORD, 
                                                     state='disabled', bg='#1e1e1e', fg='#00ff00')
        self.log_console.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def select_download_path(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
            self.log(f"Lokasi penyimpanan diubah ke: {folder}")
    
    def clear_urls(self):
        self.url_text.delete('1.0', tk.END)
        self.log("URL dikosongkan")
    
    def clear_logs(self):
        self.log_console.config(state='normal')
        self.log_console.delete('1.0', tk.END)
        self.log_console.config(state='disabled')
    
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_queue.put(f"[{timestamp}] {message}")
    
    def update_logs(self):
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.log_console.config(state='normal')
                self.log_console.insert(tk.END, message + "\n")
                self.log_console.see(tk.END)
                self.log_console.config(state='disabled')
        except queue.Empty:
            pass
        self.root.after(100, self.update_logs)
    
    def start_download(self):
        if self.is_downloading:
            messagebox.showwarning("Peringatan", "Download sedang berjalan!")
            return
        
        # Get URLs
        urls_text = self.url_text.get('1.0', tk.END).strip()
        if not urls_text:
            messagebox.showerror("Error", "Masukkan minimal satu URL!")
            return
        
        urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        
        if not urls:
            messagebox.showerror("Error", "Tidak ada URL yang valid!")
            return
        
        # Validate download path
        if not os.path.exists(self.download_path.get()):
            messagebox.showerror("Error", "Folder tujuan tidak valid!")
            return
        
        # Start download in separate thread
        self.urls_queue = urls
        self.is_downloading = True
        self.download_btn.config(state='disabled')
        
        thread = threading.Thread(target=self.download_worker, daemon=True)
        thread.start()
        
        self.log(f"Memulai download {len(urls)} URL...")
    
    def download_worker(self):
        total = len(self.urls_queue)
        completed = 0
        
        for idx, url in enumerate(self.urls_queue, 1):
            self.log(f"\n{'='*50}")
            self.log(f"Download {idx}/{total}: {url}")
            
            try:
                self.download_single(url)
                completed += 1
                self.log(f"✓ Berhasil download: {url}")
            except Exception as e:
                self.log(f"✗ Error download {url}: {str(e)}")
            
            # Update overall progress
            progress = (completed / total) * 100
            self.overall_progress['value'] = progress
            self.overall_label.config(text=f"{completed}/{total} selesai")
        
        # Reset UI
        self.is_downloading = False
        self.download_btn.config(state='normal')
        self.current_progress['value'] = 0
        self.current_label.config(text="Selesai!")
        
        self.log(f"\n{'='*50}")
        self.log(f"Download selesai! {completed}/{total} berhasil")
        
        messagebox.showinfo("Selesai", f"Download selesai!\n{completed}/{total} berhasil")
    
    def download_single(self, url):
        def progress_hook(d):
            if d['status'] == 'downloading':
                try:
                    percent_str = d.get('_percent_str', '0%').strip('%')
                    percent = float(percent_str)
                    self.current_progress['value'] = percent
                    
                    downloaded = d.get('_downloaded_bytes_str', 'N/A')
                    total = d.get('_total_bytes_str', 'N/A')
                    speed = d.get('_speed_str', 'N/A')
                    eta = d.get('_eta_str', 'N/A')
                    
                    self.current_label.config(
                        text=f"{percent:.1f}% - {downloaded}/{total} - {speed} - ETA: {eta}"
                    )
                except:
                    pass
            elif d['status'] == 'finished':
                self.current_label.config(text="Memproses file...")
                self.log("Download selesai, memproses file...")
        
        download_path = self.download_path.get()
        
        if self.download_type.get() == "video":
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook],
                'quiet': True,
                'no_warnings': True,
            }
        else:  # audio
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
                'no_warnings': True,
            }
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown')
            self.log(f"Judul: {title}")

def main():
    try:
        from yt_dlp import YoutubeDL
    except ImportError:
        import sys
        print("ERROR: yt-dlp belum terinstall!")
        print("Jalankan: pip install -r requirements.txt")
        sys.exit(1)
    
    root = tk.Tk()
    app = UniversalDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
