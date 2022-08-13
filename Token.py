from enum import Enum
from tokenize import String


class TipoToken(Enum):

    # numeros inteiros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numeroInteiro = 0

    # numero real
    numeroReal = 1

    # operacoes = [+,-,*,/]
    operador = 2

    # precedencia = [(,)]
    precedencia = 3

    # espacos = [\n, \t, ]
    espacos = 4

    # palavras_reservadas = [program , ident , begin , end , real , integer  , read , write]
    palavras_reservadas = 5

     # espacos = [:=]
    relacional = 6

    # outros = [, ;]
    outros = 7

    variaveis = 8





class Token():
    tipo: TipoToken
    valor: str

    

    def toString(self):
        if(self.valor=='\n'):
            return "Token[" + str(self.tipo) + ", " + "\\" + "n" + "]"
        elif(self.valor=='\t'):
            return "Token[" + str(self.tipo) + ", " + "\\" + "t" + "]"
        return "Token[" + str(self.tipo) + ", " + str(self.valor) + "]"



