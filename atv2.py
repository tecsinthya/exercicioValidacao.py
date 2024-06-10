class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self.validar_nome(nome)
        self.validar_idade(idade)
        self.validar_saldo(saldo)
        self.validar_status(statusCadastro)
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.statusCadastro = statusCadastro

    def validar_nome(self, nome):
        if nome is None or nome.strip() == "":
            raise ValueError("O nome não pode ser vazio.")
    
    def validar_idade(self, idade):
        if idade < 18:
            raise ValueError("A idade precisa ser maior ou igual a 18 anos.")
    
    def validar_saldo(self, saldo):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
    
    def validar_status(self, status):
        if not status:
            raise ValueError("O status do cadastro precisa ser verdadeiro.")

    def atualizar_status(self, novo_status):
        self.validar_status(novo_status)
        self.statusCadastro = novo_status
        print("Status de cadastro atualizado para:", novo_status)


try:
    cadastro1 = Cadastro("sinthya", 18, 3000, True)
    print("Nome:", cadastro1.nome)
    print("Idade:", cadastro1.idade)
    print("Saldo:", cadastro1.saldo)
    print("Status do Cadastro:", cadastro1.statusCadastro)
except ValueError as e:
    print("Erro ao criar cadastro:", e)

try:
    cadastro2 = Cadastro("", 15, -500, False)
except ValueError as e:
    print("Erro ao criar cadastro:", e)
