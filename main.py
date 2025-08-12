from livro import livro
from leitor import usuario
from biblioteca import Biblioteca

def main():  # alimentação da biblioteca
    biblioteca = Biblioteca()

    biblioteca.cadastrar_livro(livro("Python para Iniciantes", "wallace lentes", 2020, 3))
    biblioteca.cadastrar_livro(livro("POO em python", "Maria Fernanda", 2023, 2))

    biblioteca.cadastrar_usuario(usuario("cleiton", "cleiton@email.com", 1))
    biblioteca.cadastrar_usuario(usuario("Amanda", "amanda@email.com", 2))

    # emprestar e devolver
    biblioteca.emprestar_livro(1, "Python para Iniciantes")
    biblioteca.emprestar_livro(2, "POO em python")
    biblioteca.devolver_livro(1, "Python para Iniciantes")

    biblioteca.listar_livros()
    biblioteca.listar_usuarios()

if __name__ == "__main__":
    main()
