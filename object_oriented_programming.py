
# Aqui temos uma classe Pessoa, que é uma abstração criada com atributos name e age e metodos run e sleep
class Pessoa:
    # def é a palavra chave utilizada para definir uma função
    # __init__ é  o método especial chamado quando uma nova instância da classe é criada. Ele inicializa os atributos da classe.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} está correndo!")

    def sleep(self):
        print(f"{self.name} está dormindo.")


# Criando instância da classe Pessoa
pessoa1 = Pessoa("Manoel", 28)

# Acessando atributos
print(f"Nome: {pessoa1.name}, Idade: {pessoa1.age}")

# Chamando métodos
pessoa1.run()
pessoa1.sleep()
