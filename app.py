import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Removedor de Fundo")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Selecione uma imagem para remover o fundo.")
        self.label.pack(pady=10)

        self.button_browse = tk.Button(root, text="Selecionar Imagem", command=self.browse_image)
        self.button_browse.pack(pady=5)

        self.button_process = tk.Button(root, text="Remover Fundo", command=self.remove_background, state=tk.DISABLED)
        self.button_process.pack(pady=5)

        self.image_path = None

    def browse_image(self):
        filetypes = (("Imagens", "*.png *.jpg *.jpeg"), ("Todos os arquivos", "*.*"))
        self.image_path = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=filetypes)

        if self.image_path:
            self.label.config(text=f"Imagem selecionada:\n{self.image_path}")
            self.button_process.config(state=tk.NORMAL)

    def remove_background(self):
        if not self.image_path:
            messagebox.showerror("Erro", "Nenhuma imagem selecionada.")
            return

        try:
            with open(self.image_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)

            output_path = os.path.splitext(self.image_path)[0] + "_sem_fundo.png"
            with open(output_path, 'wb') as output_file:
                output_file.write(output_data)

            messagebox.showinfo("Sucesso", f"Fundo removido!\nImagem salva em:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao remover fundo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
