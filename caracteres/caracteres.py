import tkinter as tk
import pyperclip

class CharacterButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Copiar caracteres")
        self.root.configure(bg="#000000")
        
        # Leer los caracteres guardados del archivo
        try:
            from caracteres_guardados import character_list
            self.character_list = list(character_list)
        except ImportError:
            self.character_list = []

        self.text_entry = tk.Entry(self.root, width=10, bg="#000000", fg="#ffffff")
        self.text_entry.pack(pady=(4, 0))

        self.add_button = tk.Button(self.root, text="Agregar caracter", command=self.add_character, bg="#000000", fg="#ffffff")
        self.add_button.pack(pady=(4, 0))

        self.character_frame = tk.Frame(self.root, bg="#000000")
        self.character_frame.pack(pady=(4, 0))

        self.update_character_buttons()

    def copy_character(self, char):
        pyperclip.copy(char)

    def add_character(self):
        char = self.text_entry.get()
        if char:
            self.character_list.append(char)
            self.text_entry.delete(0, tk.END)
            self.update_character_buttons()
            self.save_character_list()

    def delete_character(self, char):
        self.character_list.remove(char)
        self.update_character_buttons()
        self.save_character_list()

    def update_character_buttons(self):
        for widget in self.character_frame.winfo_children():
            widget.destroy()

        row = 0
        col = 0

        for char in self.character_list:
            button = tk.Button(self.character_frame, text=char, width=3, height=2, bg="#000000", fg="#ffffff", command=lambda c=char: self.copy_character(c))
            button.bind("<Button-3>", lambda event, c=char: self.delete_character(c))
            button.grid(row=row, column=col, padx=4, pady=4)
            col += 1
            if col == 9:
                col = 0
                row += 1

    def save_character_list(self):
        with open("caracteres_guardados.py", "w") as file:
            file.write(f"character_list = \"{''.join(self.character_list)}\"")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterButtonApp(root)
    root.mainloop()
