import tkinter as tk
from tkinter import simpledialog, font, messagebox
from tkinter import ttk
import random

# ============================
# OOP (Object-Oriented Programming)
# ============================

class FoodRandomizer:
    """Class untuk mengelola data makanan dan pencarian"""
    
    def __init__(self):
        # ============================
        # Variable & Tipe Data
        # ============================
        # Dictionary: menyimpan kategori makanan dengan list of dictionaries
        self.food_categories = {
            'Breakfast': [
                {'nama': 'Soto Babe', 'harga': 8000, 'kalori': 350},
                {'nama': 'Bubur Ayam', 'harga': 12000, 'kalori': 300},
                {'nama': 'Gulai Babe', 'harga': 8000, 'kalori': 200},
                {'nama': 'Roti Bakar', 'harga': 8000, 'kalori': 250},
                {'nama': 'Mie Goreng', 'harga': 18000, 'kalori': 400}
            ],
            'Lunch': [
                {'nama': 'Nasi Padang', 'harga': 25000, 'kalori': 500},
                {'nama': 'Nasi Ayam Bali Crispy', 'harga': 15000, 'kalori': 350},
                {'nama': 'Gado-gado', 'harga': 15000, 'kalori': 300},
                {'nama': 'Nasi Ayam Geprek Petir', 'harga': 13000, 'kalori': 400},
                {'nama': 'Mie Ayam', 'harga': 22000, 'kalori': 450}
            ],
            'Dinner': [
                {'nama': 'Indomie Double', 'harga': 13000, 'kalori': 400},
                {'nama': 'Nasi Ayam Gongso', 'harga': 25000, 'kalori': 450},
                {'nama': 'Peyetan Gondang', 'harga': 20000, 'kalori': 500},
                {'nama': 'Ayam Balap SS', 'harga': 40000, 'kalori': 550},
                {'nama': 'Seafood Bakar', 'harga': 75000, 'kalori': 600}
            ],
            'Snack': [
                {'nama': 'Pisang Tandiuk Goreng', 'harga': 18000, 'kalori': 150},
                {'nama': 'Risoles', 'harga': 8000, 'kalori': 200},
                {'nama': 'Tahu Gejrot', 'harga': 8000, 'kalori': 300},
                {'nama': 'Takoyaki', 'harga': 12000, 'kalori': 250},
                {'nama': 'Martabak', 'harga': 20000, 'kalori': 400}
            ]
        }

    # ============================
    # Function and Method
    # ============================
    def cari_makanan_by_kategori(self, kategori, max_harga):
        """Cari makanan berdasarkan kategori dan harga maksimum"""
        # Variable lokal: list untuk menyimpan hasil
        hasil = []
        
        # ============================
        # Pengkondisian (Conditional)
        # ============================
        if kategori in self.food_categories:
            # ============================
            # Perulangan (Looping)
            # ============================
            # Loop untuk iterasi setiap makanan dalam kategori
            for makanan in self.food_categories[kategori]:
                # Pengkondisian: filter berdasarkan harga maksimum
                if makanan['harga'] <= max_harga:
                    hasil.append(makanan)
        return hasil


# ============================
# GUI Programming dengan Tkinter
# ============================

class FoodRandomizerGUI:
    """Class untuk GUI aplikasi Food Randomizer"""
    
    def __init__(self, master):
        # ============================
        # Variable Instance (Attribute)
        # ============================
        self.master = master
        self.randomizer = FoodRandomizer()  # Object dari class FoodRandomizer
        
        # ============================
        # Queue (History sebagai Queue/FIFO)
        # ============================
        # List sebagai queue untuk menyimpan history pencarian
        self.search_history = []
        
        # Variable untuk konfigurasi warna (String)
        self.bg_color = '#F0F4F8'  # Soft Blue Background
        self.primary_color = '#3498db'  # Modern Blue
        self.secondary_color = '#2ecc71'  # Vibrant Green
        self.accent_color = '#e74c3c'  # Vibrant Red
        self.history_color = '#9b59b6'  # Purple for history
        
        # Konfigurasi window utama
        master.title("Food Randomizer Tembalang")
        master.geometry("1100x750")
        master.configure(bg=self.bg_color)

        # Custom Fonts
        self.title_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.text_font = font.Font(family="Consolas", size=11)

        # ============================
        # GUI Components (Widgets)
        # ============================
        
        # Main Container with Subtle Shadow
        main_frame = tk.Frame(master, 
                               bg='white', 
                               bd=1, 
                               relief=tk.RAISED,
                               highlightthickness=0)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Gradient Background Canvas
        self.canvas = tk.Canvas(main_frame, 
                                bg=self.bg_color, 
                                highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create Gradient Background
        self.create_gradient_background()
        
        # Dictionary untuk menyimpan window items (untuk repositioning)
        self.window_items = {}

        # Title with Modern Design
        self.title_label = tk.Label(self.canvas, 
                               text="Food Randomizer Tembalang", 
                               font=self.title_font, 
                               bg=self.bg_color, 
                               fg=self.primary_color,
                               padx=20,
                               pady=10)
        self.window_items['title'] = self.canvas.create_window(0, 50, window=self.title_label, anchor='n')

        # Styled Category Buttons
        self.kategori_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.window_items['kategori'] = self.canvas.create_window(0, 120, window=self.kategori_frame, anchor='n')

        # Variable untuk max harga (Integer)
        self.max_harga = 1000000  # Default max price
        
        # List kategori makanan
        kategori = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
        
        # ============================
        # Perulangan untuk membuat button kategori
        # ============================
        for kat in kategori:
            btn = tk.Button(self.kategori_frame, 
                            text=f"🍽️ {kat}", 
                            command=lambda k=kat: self.cari_makanan_kategori(k),
                            font=self.button_font,
                            bg=self.primary_color, 
                            fg='white',
                            activebackground=self.secondary_color,
                            relief=tk.FLAT,
                            borderwidth=0,
                            padx=15, 
                            pady=8,
                            width=10)
            btn.pack(side=tk.LEFT, padx=10)
            btn.bind("<Enter>", lambda e, btn=btn: self.hover_effect(btn, True))
            btn.bind("<Leave>", lambda e, btn=btn: self.hover_effect(btn, False))

        # Frame untuk tombol-tombol aksi
        self.action_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.window_items['action'] = self.canvas.create_window(0, 200, window=self.action_frame, anchor='n')

        # Price Input Button with Modern Style
        harga_button = tk.Button(self.action_frame, 
                                 text="💰 Set Max Price", 
                                 command=self.set_max_harga,
                                 font=self.button_font,
                                 bg=self.accent_color, 
                                 fg='white',
                                 relief=tk.FLAT,
                                 padx=15, 
                                 pady=8)
        harga_button.pack(side=tk.LEFT, padx=10)
        
        # History Button
        history_button = tk.Button(self.action_frame, 
                                   text="📋 Show History", 
                                   command=self.show_history,
                                   font=self.button_font,
                                   bg=self.history_color, 
                                   fg='white',
                                   relief=tk.FLAT,
                                   padx=15, 
                                   pady=8)
        history_button.pack(side=tk.LEFT, padx=10)
        
        # Clear History Button
        clear_button = tk.Button(self.action_frame, 
                                text="🗑️ Clear History", 
                                command=self.clear_history,
                                font=self.button_font,
                                bg='#95a5a6', 
                                fg='white',
                                relief=tk.FLAT,
                                padx=15, 
                                pady=8)
        clear_button.pack(side=tk.LEFT, padx=10)

        # Price Warning Label
        self.peringatan_label = tk.Label(self.canvas, 
                                         text=f"⚠️ Current Max Price: Rp {self.format_price(self.max_harga)}", 
                                         fg=self.primary_color,
                                         bg=self.bg_color,
                                         font=self.text_font)
        self.window_items['label'] = self.canvas.create_window(0, 260, window=self.peringatan_label, anchor='n')
        
        # Styled Result Text with Scrollbar
        self.result_frame = tk.Frame(self.canvas, bg='white', bd=1, relief=tk.SUNKEN)
        self.window_items['result'] = self.canvas.create_window(0, 310, window=self.result_frame, width=850, height=350, anchor='n')

        self.result_text = tk.Text(self.result_frame, 
                                   font=self.text_font,
                                   bg='white', 
                                   fg='black',
                                   borderwidth=0,
                                   relief=tk.FLAT,
                                   wrap=tk.WORD)
        
        scrollbar = tk.Scrollbar(self.result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bind canvas resize event
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Initial positioning
        self.canvas.update_idletasks()
        self.center_all_items()

    # ============================
    # Function and Method untuk GUI
    # ============================
    
    def create_gradient_background(self):
        """Create a subtle gradient background"""
        width = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 1100
        
        # Perulangan untuk membuat gradient effect
        for i in range(100):
            r = int(240 - (i * 0.5))
            g = int(244 - (i * 0.8))
            b = int(248 - (i * 1))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, width, i, fill=color, tags='gradient')
    
    def format_price(self, harga):
        """Format price with thousand separators (titik)"""
        # String formatting dengan pemisah ribuan
        return f"{harga:,}".replace(',', '.')
    
    def center_all_items(self):
        """Center all window items on canvas"""
        canvas_width = self.canvas.winfo_width()
        center_x = canvas_width / 2
        
        # Perulangan untuk reposisi semua item ke tengah
        for item_id in self.window_items.values():
            bbox = self.canvas.bbox(item_id)
            if bbox:
                current_y = self.canvas.coords(item_id)[1]
                self.canvas.coords(item_id, center_x, current_y)
    
    def on_canvas_configure(self, event):
        """Reposisi elemen saat canvas di-resize"""
        canvas_width = event.width
        center_x = canvas_width / 2
        
        # Update posisi semua window items ke center
        for item_id in self.window_items.values():
            coords = self.canvas.coords(item_id)
            if coords:
                self.canvas.coords(item_id, center_x, coords[1])
        
        # Redraw gradient background
        self.canvas.delete('gradient')
        for i in range(100):
            r = int(240 - (i * 0.5))
            g = int(244 - (i * 0.8))
            b = int(248 - (i * 1))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, canvas_width, i, fill=color, tags='gradient')
        self.canvas.tag_lower('gradient')

    def hover_effect(self, btn, is_hover):
        """Create hover effect for buttons"""
        # Pengkondisian untuk efek hover
        if is_hover:
            btn.config(bg=self.secondary_color)
        else:
            btn.config(bg=self.primary_color)
    
    def set_max_harga(self):
        """Update maximum price based on user input"""
        try:
            # GUI: Input dialog untuk user
            input_str = simpledialog.askstring("Max Price", 
                                              "Enter maximum price (Rp 10.000 - 1.000.000):\n(You can use dots as thousand separators)")
            
            # ============================
            # Pengkondisian untuk validasi input
            # ============================
            if input_str:
                # Hapus semua karakter selain angka
                clean_input = ''.join(filter(str.isdigit, input_str))
                
                if clean_input:
                    input_harga = int(clean_input)
                    
                    # Validasi range dengan pengkondisian
                    if input_harga < 10000:
                        # Pop-up error message
                        messagebox.showerror("Error", "Minimum price is Rp 10.000")
                    elif input_harga > 1000000:
                        # Pop-up error message
                        messagebox.showerror("Error", "Maximum price is Rp 1.000.000")
                    else:
                        self.max_harga = input_harga
                        self.peringatan_label.config(
                            text=f"⚠️ Current Max Price: Rp {self.format_price(self.max_harga)}")
                        # Pop-up success message
                        messagebox.showinfo("Success", f"Max price updated to Rp {self.format_price(self.max_harga)}")
                else:
                    # Pop-up error message
                    messagebox.showerror("Error", "Please enter a valid number")
        except Exception as e:
            # Pop-up error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def cari_makanan_kategori(self, kategori):
        """Search for food by category and max price"""
        # Memanggil method dari object FoodRandomizer
        hasil = self.randomizer.cari_makanan_by_kategori(kategori, self.max_harga)
        
        # Clear text area
        self.result_text.delete(1.0, tk.END)
        self.result_text.tag_configure('title', foreground=self.primary_color, font=self.title_font)
        self.result_text.tag_configure('subtitle', foreground=self.accent_color, font=self.button_font)
        
        self.result_text.insert(tk.END, f"🍽️ {kategori} Category ", 'title')
        self.result_text.insert(tk.END, f"(Max Price Rp {self.format_price(self.max_harga)})\n\n", 'subtitle')
        
        # ============================
        # Pengkondisian untuk menampilkan hasil
        # ============================
        if hasil:
            random.shuffle(hasil)  # Randomize food order
            
            # ============================
            # Queue: Menambahkan entry baru ke history (FIFO)
            # ============================
            from datetime import datetime
            # Dictionary untuk menyimpan informasi history
            history_entry = {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'kategori': kategori,
                'max_harga': self.max_harga,
                'jumlah_hasil': len(hasil),
                'hasil': hasil.copy()
            }
            # Append ke queue (list)
            self.search_history.append(history_entry)
            
            # Batasi history maksimal 20 entri (Queue behavior - FIFO)
            if len(self.search_history) > 20:
                self.search_history.pop(0)  # Remove oldest entry (FIFO)
            
            # Perulangan untuk menampilkan hasil pencarian
            for makanan in hasil:
                self.result_text.insert(tk.END, 
                    f"• {makanan['nama']}\n"
                    f"  💰 Rp {self.format_price(makanan['harga'])}\n"
                    f"  🔥 {makanan['kalori']} kkal\n\n", 'item')
        else:
            self.result_text.insert(tk.END, 
                "🚫 No food found within your budget.\n"
                "Try increasing your maximum price.", 'subtitle')
    
    def show_history(self):
        """Display search history (Queue)"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.tag_configure('title', foreground=self.history_color, font=self.title_font)
        self.result_text.tag_configure('subtitle', foreground=self.primary_color, font=self.button_font)
        self.result_text.tag_configure('item', foreground='#34495e', font=self.text_font)
        
        self.result_text.insert(tk.END, "📋 Search History (Queue)\n\n", 'title')
        
        # ============================
        # Pengkondisian: Cek apakah history kosong
        # ============================
        if not self.search_history:
            self.result_text.insert(tk.END, "🚫 No search history yet.", 'item')
            return
        
        # ============================
        # Perulangan: Tampilkan history dari yang terbaru (reversed)
        # ============================
        for idx, entry in enumerate(reversed(self.search_history), 1):
            self.result_text.insert(tk.END, 
                f"[{idx}] {entry['timestamp']} - {entry['kategori']} "
                f"(Max: Rp {self.format_price(entry['max_harga'])}, "
                f"Found: {entry['jumlah_hasil']} items)\n", 'subtitle')
            
            # Nested loop untuk menampilkan detail makanan
            for makanan in entry['hasil']:
                self.result_text.insert(tk.END, 
                    f"    • {makanan['nama']} "
                    f"| Rp {self.format_price(makanan['harga'])} "
                    f"| {makanan['kalori']} kkal\n", 'item')
            
            self.result_text.insert(tk.END, "\n")
    
    def clear_history(self):
        """Clear search history (Queue)"""
        # Clear semua data di queue
        self.search_history = []
        self.result_text.delete(1.0, tk.END)
        self.result_text.tag_configure('title', foreground=self.secondary_color, font=self.title_font)
        self.result_text.insert(tk.END, "✅ History cleared successfully!", 'title')


# ============================
# Main Function
# ============================
def main():
    """Main function untuk menjalankan aplikasi"""
    root = tk.Tk()  # Membuat window utama
    app = FoodRandomizerGUI(root)  # Membuat object dari class FoodRandomizerGUI
    root.mainloop()  # Menjalankan event loop GUI


# ============================
# Program Entry Point
# ============================
if __name__ == "__main__":
    main()