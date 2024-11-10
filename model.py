class Filme:
    def __init__(self, id, descricao, completo=False):
        self.id = id
        self.descricao = descricao
        self.completo = completo

listaFilmes = []

usuarios = {
    "user": "1234",
    "admin": "5678"
}

def addFilme(descricao):
    id = len(listaFilmes) + 1  
    novo_filme = Filme(id, descricao)
    listaFilmes.append(novo_filme)

def getFilmes():
    return listaFilmes

def autenticar(user, senha):
    if user in usuarios:
        if usuarios[user] == senha:
            return user
    return None
class FilmeAlugar:
    def __init__(self, id, nome,imagem,preco):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.imagem=imagem
        

listFilmesAlugar = []
listFilmesAlugar.append(FilmeAlugar(1, "Gente Grande", 15.00, "gente_grande.jpg"))
listFilmesAlugar.append(FilmeAlugar(2, "Avengers-Ultimato", 35.00, "avengers.jpg"))
listFilmesAlugar.append(FilmeAlugar(3, "Enrolados", 10.00,"enrolados.jpg")),
listFilmesAlugar.append(FilmeAlugar(4, "Todos menos você", 40.00,"todos.jpg")),
listFilmesAlugar.append(FilmeAlugar(5, "Harry Potter4", 20.00,"harry.jpg")),
listFilmesAlugar.append(FilmeAlugar(6, "It-A coisa", 25.00,"it.jpg"))
