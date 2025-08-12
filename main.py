from livro import livro
from leitor import usuario
from biblioteca import Biblioteca

def main():  # alimentação da biblioteca
    biblioteca = Biblioteca()

    biblioteca.cadastrar_livro(livro("Introdução à Inteligência Artificial", "Ana Souza", 2021, 5))
    biblioteca.cadastrar_livro(livro("Algoritmos e Estruturas de Dados", "Carlos Pereira", 2019, 4))
    biblioteca.cadastrar_livro(livro("Desenvolvimento Web com Django", "Fernanda Lima", 2022, 3))
    biblioteca.cadastrar_livro(livro("Banco de Dados para Iniciantes", "Ricardo Alves", 2018, 6))



    biblioteca.cadastrar_usuario(usuario("João Silva", "joao.silva@email.com", 3))
    biblioteca.cadastrar_usuario(usuario("Mariana Costa", "mariana.costa@email.com", 4))
    biblioteca.cadastrar_usuario(usuario("Pedro Oliveira", "pedro.oliveira@email.com", 5))
    biblioteca.cadastrar_usuario(usuario("Beatriz Fernandes", "beatriz.fernandes@email.com", 6))


    # emprestar e devolver
    biblioteca.emprestar_livro(3, "Introdução à Inteligência Artificial")  
    biblioteca.emprestar_livro(4, "Desenvolvimento Web com Django")      
    biblioteca.devolver_livro(3, "Introdução à Inteligência Artificial")   


    biblioteca.listar_livros()
    biblioteca.listar_usuarios()

if __name__ == "__main__":
    main()
