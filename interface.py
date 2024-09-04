import tkinter as tk
from tkinter import ttk, messagebox
import os

# Função para salvar os dados em um arquivo de texto
def salvar_dados():
    cliente = entry_cliente.get()
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    dropdown_valor = combo_quantidade.get()

    # Define o caminho do arquivo
    pasta = 'dados'
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    caminho_arquivo = os.path.join(pasta, 'dados.txt')
    
    # Salva os dados no arquivo
    with open(caminho_arquivo, 'a') as file:
        file.write(f'Cliente: {cliente}\n')
        file.write(f'Produto: {produto}\n')
        file.write(f'Quantidade: {quantidade}\n')
        file.write(f'Dropdown Valor: {dropdown_valor}\n')
        file.write('-----------------------\n')

    # Mensagem de confirmação
    messagebox.showinfo('Informação', 'Dados salvos com sucesso!')

    entry_cliente.delete(0, tk.END)
    entry_produto.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    combo_quantidade.set('')

# Cria a janela principal
root = tk.Tk()
root.title('Sistema de Exemplo')

# Define o tamanho e a posição da janela
largura = 400
altura = 300
x = 100
y = 100
root.geometry(f'{largura}x{altura}+{x}+{y}')

# Layout da interface
tk.Label(root, text='Campo Cliente').grid(row=0, column=0, padx=10, pady=5)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text='Campo Produto').grid(row=1, column=0, padx=10, pady=5)
entry_produto = tk.Entry(root)
entry_produto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text='Campo Quantidade').grid(row=2, column=0, padx=10, pady=5)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text='Dropdown Lista Quantidade').grid(row=3, column=0, padx=10, pady=5)
combo_quantidade = ttk.Combobox(root, values=['Opção 1', 'Opção 2', 'Opção 3'])
combo_quantidade.grid(row=3, column=1, padx=10, pady=5)

btn_salvar = tk.Button(root, text='Salvar', command=salvar_dados)
btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
