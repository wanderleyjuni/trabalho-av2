# Importação das bibliotecas necessárias
import tkinter as tk  # Interface gráfica
from tkinter import filedialog, messagebox  # Para abrir janelas de diálogo
from PIL import Image, ImageTk  # Para manipulação de imagens (não usado diretamente aqui, mas útil para exibir imagens)
from rembg import remove  # Função para remover fundo da imagem
import os  # Para manipulação de caminhos de arquivos

# Classe principal da aplicação
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Removedor de Fundo")  # Título da janela
        self.root.geometry("400x300")  # Tamanho da janela

        # Label inicial orientando o usuário
        self.label = tk.Label(root, text="Selecione uma imagem para remover o fundo.")
        self.label.pack(pady=10)

        # Botão para selecionar imagem
        self.button_browse = tk.Button(root, text="Selecionar Imagem", command=self.browse_image)
        self.button_browse.pack(pady=5)

        # Botão para processar a imagem (inicialmente desativado)
        self.button_process = tk.Button(root, text="Remover Fundo", command=self.remove_background, state=tk.DISABLED)
        self.button_process.pack(pady=5)

        self.image_path = None  # Caminho da imagem selecionada (inicialmente None)

    # Função chamada ao clicar em "Selecionar Imagem"
    def browse_image(self):
        filetypes = (("Imagens", "*.png *.jpg *.jpeg"), ("Todos os arquivos", "*.*"))
        self.image_path = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=filetypes)

        if self.image_path:
            self.label.config(text=f"Imagem selecionada:\n{self.image_path}")
            self.button_process.config(state=tk.NORMAL)  # Ativa o botão de remover fundo

    # Função chamada ao clicar em "Remover Fundo"
    def remove_background(self):
        if not self.image_path:
            messagebox.showerror("Erro", "Nenhuma imagem selecionada.")  # Mostra erro se nenhuma imagem for selecionada
            return

        try:
            # Lê a imagem original em modo binário
            with open(self.image_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)  # Remove o fundo da imagem

            # Gera o caminho para a nova imagem com fundo removido
            output_path = os.path.splitext(self.image_path)[0] + "_sem_fundo.png"
            with open(output_path, 'wb') as output_file:
                output_file.write(output_data)  # Salva a imagem processada

            # Mostra mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Fundo removido!\nImagem salva em:\n{output_path}")
        except Exception as e:
            # Mostra mensagem de erro em caso de falha
            messagebox.showerror("Erro", f"Falha ao remover fundo: {e}")

# Ponto de entrada da aplicação
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = App(root)  # Instancia a aplicação
    root.mainloop()  # Executa o loop da interface
