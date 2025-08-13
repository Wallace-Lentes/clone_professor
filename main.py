import tkinter as tk
from tkinter import messagebox
from livro import livro
from leitor import usuario
from biblioteca import Biblioteca

biblioteca = Biblioteca()

def atualizar_status():
    total_disponiveis = sum(l.quantidade for l in biblioteca.livros)
    total_emprestados = sum((l.quantidade_inicial - l.quantidade) for l in biblioteca.livros)
    status_label.config(text=f"Disponíveis: {total_disponiveis} | Emprestados: {total_emprestados}")

biblioteca.atualizar_status_callback = atualizar_status

def cadastrar_livro():
    titulo = entrada_titulo.get().strip()
    autor = entrada_autor.get().strip()
    ano = entrada_ano.get().strip()
    qtd = entrada_qtd.get().strip()

    if not titulo or not autor or not ano or not qtd:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    if not ano.isdigit():
        messagebox.showerror("Erro", "Ano deve conter apenas números.")
        return
    if not qtd.isdigit():
        messagebox.showerror("Erro", "Quantidade deve conter apenas números.")
        return

    biblioteca.cadastrar_livro(livro(titulo, autor, int(ano), int(qtd)))
    messagebox.showinfo("Sucesso", f"Livro '{titulo}' cadastrado!")

def cadastrar_usuario():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    id_usuario = entrada_id.get().strip()

    if not nome or not email or not id_usuario:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    if not id_usuario.isdigit():
        messagebox.showerror("Erro", "ID deve conter apenas números.")
        return
    if not ("@" in email and (email.endswith(".com") or email.endswith(".com.br"))):
        messagebox.showerror("Erro", "Digite um e-mail válido.")
        return

    biblioteca.cadastrar_usuario(usuario(nome, email, int(id_usuario)))
    messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado!")

def listar_livros():
    livros = biblioteca.listar_livros()
    messagebox.showinfo("Lista de Livros", "\n".join(livros) if livros else "Nenhum livro cadastrado.")

def listar_usuarios():
    usuarios = biblioteca.listar_usuarios()
    messagebox.showinfo("Lista de Usuários", "\n".join(usuarios) if usuarios else "Nenhum usuário cadastrado.")

root = tk.Tk()
root.title("Biblioteca APP")

tk.Label(root, text='Título').grid(row=0, column=0)
entrada_titulo = tk.Entry(root)
entrada_titulo.grid(row=0, column=1)

tk.Label(root, text='Autor').grid(row=1, column=0)
entrada_autor = tk.Entry(root)
entrada_autor.grid(row=1, column=1)

tk.Label(root, text='Ano').grid(row=2, column=0)
entrada_ano = tk.Entry(root)
entrada_ano.grid(row=2, column=1)

tk.Label(root, text='Quantidade').grid(row=3, column=0)
entrada_qtd = tk.Entry(root)
entrada_qtd.grid(row=3, column=1)

tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro).grid(row=4, column=1)

tk.Label(root, text='Nome').grid(row=5, column=0)
entrada_nome = tk.Entry(root)
entrada_nome.grid(row=5, column=1)

tk.Label(root, text='E-mail').grid(row=6, column=0)
entrada_email = tk.Entry(root)
entrada_email.grid(row=6, column=1)

tk.Label(root, text='ID').grid(row=7, column=0)
entrada_id = tk.Entry(root)
entrada_id.grid(row=7, column=1)

tk.Button(root, text="Cadastrar Usuário", command=cadastrar_usuario).grid(row=8, column=1)

tk.Button(root, text="Listar Livros", command=listar_livros).grid(row=9, column=1)
tk.Button(root, text="Listar Usuários", command=listar_usuarios).grid(row=10, column=1)

status_label = tk.Label(root, text="Disponíveis: 0 | Emprestados: 0", anchor="w")
status_label.grid(row=11, column=0, columnspan=2, sticky="we")

atualizar_status()

root.mainloop()
