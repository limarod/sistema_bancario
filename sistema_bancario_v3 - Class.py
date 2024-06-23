from abc import ABC, abstractmethod, classmethod


class Cliente:
    def __init__(self, endereco ):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        
        if valor > saldo:
            print ("Você não tem saldo suficiente para sacar este valor.")
        
        elif valor <=0:
            print("Operação inválida, O valor informado é inválido")

        elif valor > 0:
            saldo -= valor 
            print("saque realizado com sucesso!") 
            return True
        
        return False

    def depositar(self, valor):
        saldo = self._saldo

        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso.")
            return True
        
        else:
            print("Operação não realizada, digite um valor válido.")
        
        return True


class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    

    def sacar(self, valor):
        numero_saques = 0

        for transacao in self.historico.transacoes:
            if transacao["tipo"] == "Saque":
                numero_saques +=1

        excedeu_limite_saque = valor > self.limite
        excedeu_limite_transacoes = numero_saques >= self.limite_saques

        if excedeu_limite_saque:
            print(f"valor de saque excedeu o limite de {self.limite}")
        elif excedeu_limite_transacoes:
            print(f"você excedeu o limite de {self.limite_saques} saques diários.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
            Agência: {self.agencia} 
            C/C: {self.numero} 
            Titular: {self.cliente.nome}
        """
    
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacoes(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor) :
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor) :
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)