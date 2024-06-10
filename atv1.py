class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.statusCadastro = statusCadastro

    def atualizar_status(self, novo_status):
        self.statusCadastro = novo_status
        print("Status de cadastro atualizado para:", novo_status)


cadastro1 = Cadastro("sinthya", 16, 3000, "Ativo")
print("Nome:", cadastro1.nome)
print("Idade:", cadastro1.idade)
print("Saldo:", cadastro1.saldo)
print("Status do Cadastro:", cadastro1.statusCadastro)

cadastro1.atualizar_status("Inativo")
print("Novo status do Cadastro:", cadastro1.statusCadastro)
