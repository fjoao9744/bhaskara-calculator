import customtkinter as ctk
from math import sqrt, trunc

class App(ctk.CTk):
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Bhaskara")
        
        abc_label = ctk.CTkLabel(self, text="Determine:", font=("Arial", 25))
        abc_label.pack(pady=(40, 10))
        
        abc_frame = ctk.CTkFrame(self)
        abc_frame.pack()
        
        self.a_button = ctk.CTkEntry(abc_frame, placeholder_text="A")
        self.a_button.pack(side="left", padx=10)
        self.a_button.bind("<KeyRelease>", self.calcular)
        
        self.b_button = ctk.CTkEntry(abc_frame, placeholder_text="B")
        self.b_button.pack(side="left", padx=10)
        self.b_button.bind("<KeyRelease>", self.calcular)
        
        self.c_button = ctk.CTkEntry(abc_frame, placeholder_text="C")
        self.c_button.pack(side="left", padx=10)
        self.c_button.bind("<KeyRelease>", self.calcular)
        
        x_frame = ctk.CTkFrame(self)
        x_frame.pack(anchor="center", pady=50)
        
        self.x1 = ctk.CTkLabel(x_frame, text=f"x1 = ?", font=("Arial", 40))
        self.x1.pack(padx=50, side="left", anchor="center")
        
        self.x2 = ctk.CTkLabel(x_frame, text=f"x2 = ?", font=("Arial", 40))
        self.x2.pack(padx=(0, 50), side="left", anchor="center")
        
        copy = ctk.CTkLabel(self, text="©João F.", font=("Arial", 15))
        copy.pack(side="bottom")
        
    def calcular(self, event=None):
        a = self.a_button.get()
        b = self.b_button.get()
        c = self.c_button.get()
        if a == "" or b == "" or c == "": 
            return
        
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            
            delta = (b ** 2) - (4 * (a * c))
            
            delta_raiz = sqrt(delta)
            
            _x1 = ((b * -1) + delta_raiz) / (2 * a)
            _x2 = ((b * -1) - delta_raiz) / (2 * a)
            
            self.x1.configure(text= f"x1 = {trunc(_x1)}")
            self.x2.configure(text= f"x2 = {trunc(_x2)}")
        
        except ValueError:
            self.x1.configure(text= f"x1 = ?")
            self.x2.configure(text= f"x2 = ?")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()