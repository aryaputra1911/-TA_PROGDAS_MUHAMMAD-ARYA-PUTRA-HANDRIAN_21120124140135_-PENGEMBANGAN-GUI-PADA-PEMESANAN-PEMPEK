import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class AplikasiPemesananPempek:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Pemesanan Pempek")
        self.root.geometry("800x600")  # Ukuran jendela awal

        # Memuat gambar latar belakang
        self.bg_image = Image.open("uatkan saya background dengan tema pempek sederhana(untuk halaman login).jpeg")  # Ganti dengan path gambar latar belakang Anda
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Membuat label untuk menampilkan gambar latar belakang
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Menempatkan label di belakang

        # Mengikat event perubahan ukuran jendela
        self.root.bind("<Configure>", self.resize_bg)
        
        # File teks untuk menyimpan akun dan pesanan
        self.akun_file = 'akun.txt'
        self.pesanan_file = 'pesanan.txt'

        # Variabel untuk menyimpan data pesanan
        self.pesanan = []
        self.username = None

        # Membaca akun yang sudah ada
        self.akun = self.baca_akun()

        # Menampilkan halaman login pertama kali
        self.buat_halaman_login()

    def resize_bg(self, event):
        """Mengubah ukuran gambar latar belakang agar sesuai dengan ukuran jendela."""
        # Mengubah ukuran gambar latar belakang
        new_bg_image = self.bg_image.resize((event.width, event.height))
        self.bg_photo = ImageTk.PhotoImage(new_bg_image)
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Pastikan label mengisi seluruh area

    def baca_akun(self):
        """Membaca akun dari file teks"""
        akun = {}
        try:
            with open(self.akun_file, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    akun[username] = password
        except FileNotFoundError:
            # Jika file tidak ada, kita mulai dengan akun kosong
            pass
        return akun

    def simpan_akun(self):
        """Menyimpan akun ke dalam file teks"""
        with open(self.akun_file, 'w') as file:
            for username, password in self.akun.items():
                file.write(f"{username},{password}\n")

    def simpan_pesanan(self, username, jenis, jumlah, total_harga):
        """Menyimpan pesanan ke dalam file teks"""
        with open(self.pesanan_file, 'a') as file:
            file.write(f"{username},{jenis},{jumlah},{total_harga}\n")

    def buat_halaman_login(self):
        # Menghapus konten sebelumnya
        self.clear_content()

        # Menambahkan label judul
        label_judul = tk.Label(self.root, text="PEMESANAN PEMPEK", font=("Arial", 30, "bold"), fg='#844b0e', bg="#ecb45b")
        label_judul.pack(pady=30)

        # Username
        label_username = tk.Label(self.root, text="ᵘˢᵉʳⁿᵃᵐᵉ", font=("Arial", 18, "bold"), bg="#ecb45b", fg='#844b0e')
        label_username.pack(pady=(0, 0), anchor='center')  # Jarak lebih besar di atas

        self.entry_username = tk.Entry(self.root, width=30)
        self.entry_username.pack(pady=(0, 0), anchor='center')  # Jarak lebih besar di bawah

        # Password
        label_password = tk.Label(self.root, text="ᵖᵃˢˢʷᵒʳᵈ", font=("Arial", 18, "bold"), bg="#ecb45b", fg='#844b0e')
        label_password.pack(pady=(0, 0), anchor='center')  # Jarak lebih besar di atas

        self.entry_password = tk.Entry(self.root, show="*", width=30)
        self.entry_password.pack(pady=(10, 0), anchor='center')  # Jarak lebih besar di bawah
        
        # Tombol Login
        tombol_login = tk.Button(self.root, text="Login", bg="#ecb45b", command=self.proses_login)
        tombol_login.pack(pady=(20, 0), anchor='center')  # Jarak lebih besar di atas

        # Tombol Daftar
        tombol_daftar = tk.Button(
            self.root,
            text="Daftar Akun Baru",
            command=self.buka_halaman_daftar,
            bg="#ecb45b",
        )
        tombol_daftar.pack(pady=(10, 0), anchor='center')  # Jarak lebih besar di bawah

    def clear_content(self):
        """Menghapus konten (form login, daftar, pemesanan)"""
        for widget in self.root.winfo_children():
            if widget != self.bg_label:  # Jangan hapus label background
                widget.destroy()

    def buka_halaman_daftar(self):
        # Menampilkan halaman daftar
        self.clear_content()
        self.buat_halaman_daftar()

    def buat_halaman_daftar(self):
        # Menambahkan label judul
        label_judul = tk.Label(self.root, text="PEMESANAN PEMPEK", font=("Arial", 24, "bold"), fg='#844b0e', bg="#ecb45b")
        label_judul.pack(pady=30)

        # Username
        label_username = tk.Label(self.root, font=("arial", 10, "bold"), text="Username:", bg='#ecb45b', fg='#844b0e')
        label_username.pack(pady=5)
        self.entry_username_daftar = tk.Entry(self.root, width=30)
        self.entry_username_daftar.pack(pady=5)
        
        # Password
        label_password = tk.Label(self.root, font=("arial", 10, "bold"), text="Password:", bg='#ecb45b', fg='#844b0e')
        label_password.pack(pady=5)
        self.entry_password_daftar = tk.Entry(self.root, show="*", width=30)
        self.entry_password_daftar.pack(pady=5)
        
        # Tombol Daftar
        tombol_daftar = tk.Button(self.root, text="Daftar", bg='#ecb45b', fg='black', command=self.proses_daftar)
        tombol_daftar.pack(pady=10)
        
        # Tombol Kembali ke Login
        tombol_kembali = tk.Button(self.root, text="Kembali ke Login", bg='#ecb45b', fg='black', command=self.kembali_ke_login)
        tombol_kembali.pack(pady=5)

    def kembali_ke_login(self):
        # Menampilkan kembali halaman login
        self.clear_content()
        self.buat_halaman_login()

    def proses_daftar(self):
        username = self.entry_username_daftar.get()
        password = self.entry_password_daftar.get()
        
        if not username or not password:
            messagebox.showwarning("Peringatan", "Harap isi semua data!")
            return
        
        if username in self.akun:
            messagebox.showerror("Error", "Username sudah terdaftar!")
            return
        
        # Menambahkan akun baru
        self.akun[username] = password
        self.simpan_akun()  # Simpan akun ke file
        messagebox.showinfo("Sukses", "Akun berhasil dibuat!")
        self.kembali_ke_login()

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username in self.akun and self.akun[username] == password:
            self.username = username
            # Menampilkan halaman pemesanan
            self.clear_content()
            self.buat_halaman_pemesanan()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")

    def buat_halaman_pemesanan(self):
        # Menambahkan label judul
        label_judul = tk.Label(self.root, text="PEMESANAN PEMPEK", font=("Arial", 24, "bold"), fg='#844b0e', bg="#ecb45b")
        label_judul.pack(pady=30)

        # Daftar Pempek
        jenis_pempek = [
            "Pempek Lenjer", 
            "Pempek Kapal Selam", 
            "Pempek Telur", 
            "Pempek Keriting"
        ]
        
        # Label Pilih Pempek
        label_pilih = tk.Label(self.root, text="Pilih Jenis Pempek:", bg="#ecb45b")
        label_pilih.pack()
        
        # Dropdown Pempek
        self.pilihan_pempek = ttk.Combobox(
            self.root, 
            values=jenis_pempek, 
            state="read only"
        )
        self.pilihan_pempek.pack(pady=5)
        
        # Label Jumlah
        label_jumlah = tk.Label(self.root, text="Jumlah:", bg="#ecb45b")
        label_jumlah.pack()
        
        # Entry Jumlah
        self.entry_jumlah = tk.Entry(self.root, width=10)
        self.entry_jumlah.pack(pady=5)
        
        # Harga Pempek
        self.harga = {
            "Pempek Lenjer": 10000,
            "Pempek Kapal Selam": 15000,
            "Pempek Telur": 12000,
            "Pempek Keriting": 11000
        }
        
        # Tombol Pesan
        tombol_pesan = tk.Button(self.root, text="Tambah Pesanan", command=self.tambah_pesanan, bg="#ecb45b")
        tombol_pesan.pack(pady=10)
        
        # Tabel Pesanan
        self.tree = ttk.Treeview(
            self.root, 
            columns=('Jenis', 'Jumlah', 'Total'), 
            show='headings'
        )
        self.tree.heading('Jenis', text='Jenis Pempek')
        self.tree.heading('Jumlah', text='Jumlah')
        self.tree.heading('Total', text='Total Harga')
        self.tree.pack(pady=10)
        
        # Total Keseluruhan
        self.label_total = tk.Label(self.root, text="Total: Rp 0", font=("Arial", 12, "bold"), bg="#ecb45b")
        self.label_total.pack(pady=5)
        
        # Tombol Selesai Pesan
        tombol_selesai = tk.Button(self.root, text="Selesai Pesan", command=self.selesai_pesan, bg="#ecb45b")
        tombol_selesai.pack(pady=10)
    
    def tambah_pesanan(self):
        jenis = self.pilihan_pempek.get()
        jumlah = self.entry_jumlah.get()
        
        if not jenis or not jumlah:
            messagebox.showwarning("Peringatan", "Harap isi semua data!")
            return
        
        try:
            jumlah = int(jumlah)
            if jumlah <= 0:  # Memastikan jumlah tidak negatif atau nol
                messagebox.showerror("Error", "Jumlah tidak bisa negatif!")
                return
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus angka!")
            return
        
        total_harga = self.harga[jenis] * jumlah
        
        # Tambah ke tabel
        self.tree.insert('', 'end', values=(jenis, jumlah, f"Rp {total_harga}"))
        
        # Simpan pesanan
        self.pesanan.append({
            'jenis': jenis,
            'jumlah': jumlah,
            'total': total_harga
        })
        
        # Simpan pesanan ke file
        self.simpan_pesanan(self.username, jenis, jumlah, total_harga)
        
        # Update total
        total_keseluruhan = sum(p['total'] for p in self.pesanan)
        self.label_total.config(text=f"Total: Rp {total_keseluruhan}")

    def selesai_pesan(self):
        if not self.pesanan:
            messagebox.showwarning("Peringatan", "Belum ada pesanan!")
            return
    
        # Mengonfirmasi pesanan
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menyelesaikan pesanan?")
        if konfirmasi:
            # Menampilkan informasi pesanan
            pesan = "Pesanan Anda:\n\n"
            total_harga = 0
            for p in self.pesanan:
                pesan += f"{p['jenis']} - Jumlah: {p['jumlah']} - Total: Rp {p['total']}\n"
                total_harga += p['total']
            pesan += f"\nTotal Keseluruhan: Rp {total_harga}"
        
        # Menampilkan pesan konfirmasi
            messagebox.showinfo("Pesanan Diterima", pesan)
        
        # Lanjut ke halaman pembayaran
            self.buat_halaman_pilih_pembayaran(total_harga)

    def buat_halaman_pilih_pembayaran(self, total_harga):
        """Halaman untuk memilih metode pembayaran"""
        self.clear_content()  # Hapus konten sebelumnya

        # Judul Halaman Pembayaran
        label_judul = tk.Label(self.root, text="Pilih Metode Pembayaran", font=("Arial", 30, "bold"), bg="#ecb45b",fg='#844b0e')
        label_judul.pack(pady=75)

        # Daftar Metode Pembayaran
        metode_pembayaran = [
            ("GoPay", "085173446772"),
            ("ShopeePay", "085173446772"),
            ("OVO", "081294396771")
        ]
    
    # Menampilkan pilihan metode pembayaran
        for metode, nomor in metode_pembayaran:
            button_pembayaran = tk.Button(self.root, 
                                      text=f"{metode} - {nomor}", 
                                      command=lambda m=metode, n=nomor: self.pilih_metode_pembayaran(m, n, total_harga),
                                      bg="#ecb45b")
            button_pembayaran.pack(pady=15)

    def pilih_metode_pembayaran(self, metode, nomor, total_harga):
        """Fungsi untuk menangani pemilihan metode pembayaran"""
        # Menampilkan pesan konfirmasi pembayaran
        messagebox.showinfo("Konfirmasi Pembayaran", f"Pembayaran Anda sebesar Rp {total_harga} telah diproses menggunakan {metode}.")
        
        # Kembali ke halaman login setelah konfirmasi pembayaran
        self.kembali_ke_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPemesananPempek(root)
    root.mainloop()
