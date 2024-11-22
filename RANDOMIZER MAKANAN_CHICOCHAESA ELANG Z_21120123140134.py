import tkinter as tk
from tkinter import simpledialog, font
from tkinter import ttk
import random

class FoodRandomizer:
    def __init__(self):
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

    def cari_makanan_by_kategori(self, kategori, max_harga):
        """Cari makanan berdasarkan kategori dan harga maksimum"""
        hasil = []
        if kategori in self.food_categories:
            for makanan in self.food_categories[kategori]:
                if makanan['harga'] <= max_harga:
                    hasil.append(makanan)
        return hasil


class FoodRandomizerGUI:
    def __init__(self, master):
        self.master = master
        self.randomizer = FoodRandomizer()
        
        # Konfigurasi Warna Modern
        self.bg_color = '#F0F4F8'  # Soft Blue Background
        self.primary_color = '#3498db'  # Modern Blue
        self.secondary_color = '#2ecc71'  # Vibrant Green
        self.accent_color = '#e74c3c'  # Vibrant Red
        
        master.title("Food Randomizer Tembalang")
        master.geometry("900x750")
        master.configure(bg=self.bg_color)

        # Custom Fonts
        self.title_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.text_font = font.Font(family="Consolas", size=11)

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

        # Title with Modern Design
        title_label = tk.Label(self.canvas, 
                               text="Food Randomizer Tembalang", 
                               font=self.title_font, 
                               bg=self.bg_color, 
                               fg=self.primary_color,
                               padx=20,
                               pady=10)
        self.canvas.create_window(450, 50, window=title_label)

        # Styled Category Buttons
        kategori_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window(450, 120, window=kategori_frame)

        self.max_harga = 100000  # Default max price
        kategori = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
        for kat in kategori:
            btn = tk.Button(kategori_frame, 
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

        # Price Input Button with Modern Style
        harga_button = tk.Button(self.canvas, 
                                 text="💰 Set Max Price", 
                                 command=self.set_max_harga,
                                 font=self.button_font,
                                 bg=self.accent_color, 
                                 fg='white',
                                 relief=tk.FLAT,
                                 padx=15, 
                                 pady=8)
        self.canvas.create_window(450, 200, window=harga_button)

        # Price Warning Label
        self.peringatan_label = tk.Label(self.canvas, 
                                         text=f"⚠️ Current Max Price: Rp {self.max_harga}", 
                                         fg=self.primary_color,
                                         bg=self.bg_color,
                                         font=self.text_font)
        self.canvas.create_window(450, 250, window=self.peringatan_label)

        # Styled Result Text with Scrollbar
        result_frame = tk.Frame(self.canvas, bg='white', bd=1, relief=tk.SUNKEN)
        self.canvas.create_window(450, 475, window=result_frame, width=700, height=300)

        self.result_text = tk.Text(result_frame, 
                                   font=self.text_font,
                                   bg='white', 
                                   fg='black',
                                   borderwidth=0, 
                                   wrap=tk.WORD)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add Scrollbar
        scrollbar = tk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)

    def create_gradient_background(self):
        """Create a subtle gradient background"""
        for i in range(100):
            r = int(240 - (i * 0.5))
            g = int(244 - (i * 0.8))
            b = int(248 - (i * 1))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, 900, i, fill=color)

    def hover_effect(self, btn, is_hover):
        """Create hover effect for buttons"""
        if is_hover:
            btn.config(bg=self.secondary_color)
        else:
            btn.config(bg=self.primary_color)

    def set_max_harga(self):
        """Update maximum price based on user input"""
        try:
            input_harga = simpledialog.askinteger("Max Price", 
                                                  "Enter maximum price (Rp):",
                                                  minvalue=1, 
                                                  maxvalue=1000000)
            if input_harga:
                self.max_harga = input_harga
                self.peringatan_label.config(
                    text=f"⚠️ Current Max Price: Rp {self.max_harga}")
        except Exception as e:
            self.peringatan_label.config(text=f"⚠️ Error: {e}")

    def cari_makanan_kategori(self, kategori):
        """Search for food by category and max price"""
        hasil = self.randomizer.cari_makanan_by_kategori(kategori, self.max_harga)
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.tag_configure('title', foreground=self.primary_color, font=self.title_font)
        self.result_text.tag_configure('subtitle', foreground=self.accent_color, font=self.button_font)
        
        self.result_text.insert(tk.END, f"🍽️ {kategori} Category ", 'title')
        self.result_text.insert(tk.END, f"(Max Price Rp {self.max_harga})\n\n", 'subtitle')
        
        if hasil:
            random.shuffle(hasil)  # Randomize food order
            for makanan in hasil:
                self.result_text.insert(tk.END, 
                    f"• {makanan['nama']} "
                    f"| Price: Rp {makanan['harga']} "
                    f"| Calories: {makanan['kalori']} kkal\n")
        else:
            self.result_text.insert(tk.END, "🚫 No food matches the criteria.")


def main():
    root = tk.Tk()
    app = FoodRandomizerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()