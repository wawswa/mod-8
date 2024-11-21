import tkinter as tk
from tkinter import messagebox
import math

class VolumeTabung:
    def __init__(self, root):
        self.root = root
        self.root.title("hitung volume tabung")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')

        self.is_logged_in = False

        self.frame_login = tk.Frame(root, bg='#f0f0f0')
        self.frame_login.pack(expand=True, fill='both')

        self.label_judul_login = tk.Label(
            self.frame_login, 
            text="Login ", 
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0'
        )
        self.label_judul_login.pack(pady=20)

        self.label_username = tk.Label(
            self.frame_login, 
            text="Username", 
            bg='#f0f0f0'
        )
        self.label_username.pack()

        self.entry_username = tk.Entry(
            self.frame_login, 
            width=30
        )
        self.entry_username.pack(pady=10)

        self.tombol_login = tk.Button(
            self.frame_login, 
            text="Masuk", 
            command=self.validasi_login,
            bg='#4CAF50',
            fg='white'
        )
        self.tombol_login.pack(pady=10)

        self.frame_input = tk.Frame(root, bg='#f0f0f0')

        self.label_judul_input = tk.Label(
            self.frame_input, 
            text="Hitung Volume Tabung", 
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0'
        )
        self.label_judul_input.pack(pady=20)

        self.label_jari_jari = tk.Label(
            self.frame_input, 
            text="Jari-jari (cm)", 
            bg='#f0f0f0'
        )
        self.label_jari_jari.pack()

        self.entry_jari_jari = tk.Entry(
            self.frame_input, 
            width=30
        )
        self.entry_jari_jari.pack(pady=10)

        self.label_tinggi = tk.Label(
            self.frame_input, 
            text="Tinggi (cm)", 
            bg='#f0f0f0'
        )
        self.label_tinggi.pack()

        self.entry_tinggi = tk.Entry(
            self.frame_input, 
            width=30
        )
        self.entry_tinggi.pack(pady=10)

        self.tombol_hitung = tk.Button(
            self.frame_input, 
            text="Hitung Volume", 
            command=self.hitung_volume,
            bg='#2196F3',
            fg='white'
        )
        self.tombol_hitung.pack(pady=10)

        self.frame_hasil = tk.Frame(root, bg='#f0f0f0')


        self.label_hasil_volume = tk.Label(
            self.frame_hasil, 
            text="Hasil Perhitungan Volume", 
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0'
        )
        self.label_hasil_volume.pack(pady=20)

        self.label_detail_volume = tk.Label(
            self.frame_hasil, 
            text="", 
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        self.label_detail_volume.pack(pady=10)

        self.tombol_kembali = tk.Button(
            self.frame_hasil, 
            text="Hitung Ulang", 
            command=self.kembali_input,
            bg='#FF9800',
            fg='white'
        )
        self.tombol_kembali.pack(pady=10)

    def validasi_login(self):
        username = self.entry_username.get()
        if username == "admin":
            self.is_logged_in = True
            self.frame_login.pack_forget()
            self.frame_input.pack(expand=True, fill='both')
        else:
            messagebox.showerror("login salah", "Username salah")

    def hitung_volume(self):
        try:
            jari_jari = float(self.entry_jari_jari.get())
            tinggi = float(self.entry_tinggi.get())

            volume = math.pi * (jari_jari ** 2) * tinggi

            self.frame_input.pack_forget()
            self.frame_hasil.pack(expand=True, fill='both')

            hasil_teks = (
                f"Jari-jari: {jari_jari} cm\n"
                f"Tinggi: {tinggi} cm\n"
                f"Volume Tabung: {volume:.2f} cm³"
            )
            self.label_detail_volume.config(text=hasil_teks)

        except ValueError:
            messagebox.showerror("salah input", "Masukkan angka yang valid")

    def kembali_input(self):
        self.frame_hasil.pack_forget()
        self.frame_input.pack(expand=True, fill='both')

        self.entry_jari_jari.delete(0, tk.END)
        self.entry_tinggi.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = VolumeTabung(root)
    root.mainloop()

if __name__ == "__main__":
    main()