from xml.etree.ElementTree import tostring
from Token import Token,TipoToken

class Lexico():

    def __init__(self, caminhoArquivo):
        with open(caminhoArquivo,'r') as arquivo:
            self.conteudo = arquivo.read()
            self.pos = 0
    linha = 1

    # token = Token()
    # token.valor = 'a'
    # token.tipo = TipoToken.variaveis
    # print(token.tipo.value)
    

    def nextToken(self):
        
        valor = ''
        token = None
        estado = 0
        listaPalavrasReservadas = ['program' , 'ident' , 'begin' , 'end' , 'real' , 'integer'  , 'read' , 'write']
        # if(not self.pos == 0):
        #     self.backChar()
        
        while(True):

            
           
            if(self.isEOF()):
                self.pos = len(self.conteudo)+1
                #return None
           
            c = self.nextChar()

            # ESTADO 0 
            if (estado == 0):
                if(self.isNumero(c)):
                    estado = 1
                    valor = valor + c
                elif (self.isOperador(c)):
                    estado = 5
                    valor += c
                elif (self.isPreced(c)):
                    estado = 6
                    valor += c
                elif (self.isEspaco(c)):
                    estado = 12
                    # continue
                    valor += c
                elif (self.isLetraMinuscula(c)):
                    estado = 7
                    valor += c
                elif (self.isOperadorAtribuicao1(c)):
                    estado = 9
                    valor += c
                elif (self.isOutros(c)):
                    estado = 13
                    valor += c
                elif (c == "$$"):
                    break
                else:
                    raise Exception(f"Token não reconhecido. Linha: {self.linha} Posição: {self.pos - 1} Token: {valor}")
                continue


            # ESTADO 1
            if(estado == 1):
                if(self.isNumero(c)):
                    estado = 1
                    valor += c
                    continue
                elif(self.isPonto(c)):
                    estado = 2
                    valor += c
                    continue
                else:
                    estado = 3
            
            # ESTADO 2
            if(estado == 2):
                if(self.isNumero(c)):
                    estado = 2
                    valor += c
                else:
                    estado = 4
        
            
            # ESTADO 3
            if(estado == 3):
                token = Token()

                # atribui o valor e tipo de token
                token.tipo = TipoToken.numeroInteiro
                token.valor = valor
                self.backChar()

                return token

            # ESTADO 4
            if(estado == 4):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.numeroReal
                token.valor = valor
                self.backChar()

                return token

            # ESTADO 5
            if(estado == 5):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.operador
                token.valor = valor
                self.backChar()

                return token

            # ESTADO 6
            if(estado == 6):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.precedencia
                token.valor = str(valor)
                self.backChar()

                return token

            # ESTADO 7
            if(estado == 7):
                if(self.isLetraMinuscula(c)):
                    estado = 7
                    valor += c
                    continue
                elif(self.isUnderline(c)):
                    estado = 14
                    valor += c
                    continue
                else:
                    estado = 8

                

            # ESTADO 8
            if(estado == 8):
                token = Token()
                
                # atribui o valor e tipo de token
                if valor in listaPalavrasReservadas:
                    token.tipo = TipoToken.palavras_reservadas
                else:
                    token.tipo = TipoToken.variaveis

                token.valor = valor
                self.backChar()

                return token
                

            # ESTADO 9
            if(estado == 9):
                if(self.isOperadorAtribuicao2(c)):
                    estado = 10
                    valor += c
                    continue
                else:
                    estado = 11

            # ESTADO 10
            if(estado == 10):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.relacional
                token.valor = valor
                self.backChar()

                return token


            # ESTADO 11
            if(estado == 11):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.relacional
                token.valor = valor
                self.backChar()

                return token
            
            # ESTADO 12
            if(estado == 12):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.espacos
                token.valor = valor
                self.backChar()

                return token
            
            # ESTADO 13
            if(estado == 13):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.outros
                token.valor = valor
                self.backChar()

                return token
            
            # ESTADO 14
            if(estado == 14):
                if(self.isLetraMinuscula(c)):
                    estado = 7
                    valor += c
                    continue
                else:
                    estado = 15

            # ESTADO 15
            if(estado == 15):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.variaveis
                token.valor = valor
                self.backChar()

                return token
        

        

    # POSSIBILIDADES QUE LEVAM A UM ESTADO X
    def isNumero(self,c):
        return (c>= '0' and c <='9')

    def isOperador(self, c):
        return (c == '+' or c == '-' or c == '*' or c == '/')

    def isPreced(self,c):
        return (c == '(' or c == ')')

    def isPonto(self, c):
        return (c == '.')
    
    def isEspaco(self,c):
        if (c == '\n'):
            self.linha+=1
        return (c == '\n' or c == '\t' or c == ' ')

    def isLetraMinuscula(self,c):
        return (c >= 'a' and c <= 'z') 
    
    def isOperadorAtribuicao1(self,c):
        return (c == ':')
    
    def isOperadorAtribuicao2(self,c):
        return (c == '=')

    def isOutros(self,c):
        return (c == ';' or c == ',')

    def isUnderline(self,c):
        return (c == '_')



    
    # verificar se chegou ao fim da fita
    def isEOF(self):
        return self.pos >= len(self.conteudo) 

    # anda na fita
    def nextChar(self):
        if(self.isEOF()):
            return '$$'
        aux = self.pos
        self.pos += 1
        return self.conteudo[aux]
    
    # volta na fita
    def backChar(self):
        self.pos -= 1
        # if(not self.isEOF()):
        #     self.pos -= 1
    





    
def main():
    token = Lexico('entrada.txt')
    while not(token.isEOF()):
        print(token.nextToken())

    # while not(token.isEOF()):
    #     valor = token.nextToken()
    #     if valor != None:
    #         if valor.valor not in  ["\n"," ","\t"]:
    #             print(valor.valor)
        
    

# main()
    

