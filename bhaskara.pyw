import customtkinter as ctk

class App(ctk.CTk):
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    
        
if __name__ == "__main__":
    app = App()
    app.mainloop()