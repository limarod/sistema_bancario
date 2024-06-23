# class Calculadora:
#     def __init__(self, num1, num2):
#         self._num1 = num1
#         self._num2 = num2
        
#     def Calcular_Soma(self):
#         return f"{self.__class__.__name__}: {self._num1 + self._num2}"
   
#     def Calcular_Subtracao(self):
#         return self._num1 - self._num2
    
#     def Calcular_Multiplicacao(self):
#         return self._num1 * self._num2
    
#     def Calcular_Divisao(self):
#         return self._num1 / self._num2
    


# calculo1 = Calculadora(2, 3)
# print(calculo1.Calcular_Soma())


# calculo2 = Calculadora(2, 3)

# print(f"{calculo2.Calcular_Divisao():.2f}")
# calculo3 = Calculadora(2,3)
# print(calculo3.Calcular_Multiplicacao())
# calculo4 = Calculadora(2, 3)
# print(calculo4.Calcular_Subtracao())

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# class Elevador:
#     def __init__(self) -> None:
#         self._andar = 0
        
#     def locomover(self, andar):
#         if (andar < 0 or andar > 15 ):
#             return self._mensagem_erro()
        
#         else:
#             self._andar = andar 
#             return self._mensagem_alteração_andar()
        

    
#     def _mensagem_erro(self):
#         return f'Andar incorreto! Elevador no {self._andar}º andar'
    
#     def _mensagem_alteração_andar(self):
#         return f'Elevador indo para {self._andar}º andar'
    
    
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# Módulo 're' que fornece operações com expressões regulares.
# import re


# tODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
# def validate_numero_telefone(phone_number):
   
#     # tODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
#    pattern = re.compile('^\(\d{2}\) 9\d{4}-\d{4}')
#     # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
#     # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
#     if re.match(pattern, phone_number):  
        
#         # tODO: Agora crie um return, para retornar que o número de telefone é válido:
#         return ("Número de telefone válido.")
        
    
       
#        # tODO: Crie um else e return, caso não o número de telefone seja inválido:
#     else:
#         return ("Número de telefone inválido.")

# # Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
# phone_number = input()  

# # tTODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
# result = validate_numero_telefone(phone_number)
# # Imprime o resultado:
# print(result)


class Casa:
    lista = []

    def __init__(self, qtdd_quartos, qtdd_banheiros, qtdd_vagas):
        self.qtdd_quartos = qtdd_quartos
        self.qtdd_banheiros = qtdd_banheiros
        self.qtdd_vagas = qtdd_vagas

        Casa.lista.append(self)

    def __str__ (self):
        result = ""
        for casa in self.lista:
            result +=  f"{casa.qtdd_quartos} e haha {casa.qtdd_banheiros}"
        return result
    

c1 = Casa(2,1,1)
c2 = Casa(5,5,5)
c3 = Casa(8,8,8)

# print(c1)
print(c2)

