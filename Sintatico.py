from Lexico import Lexico


class Sintatico():
    listaSubCadeias = []
    pilha = ""



    # ---------------------------------------MÉTODOS DE CONSULTA NA TABELA M---------------------------------------

    def is_PROGRAMA(self, token):
        global pilha
        if(token=='program'):
            self.pilha = self.pilha.replace('PROGRAMA','program ident CORPO .',1)
        else:
            raise Exception('Erro sintático.')

    def is_CORPO(self, token):
        global pilha
        if(token=='real' or token=='integer'):
            self.pilha = self.pilha.replace('CORPO','DC begin COMANDOS end',1)
        else:
            raise Exception('Erro sintático.')

    def is_DC(self, token):
        global pilha
        if(token=='begin'):
            self.pilha = self.pilha.replace('DC','',1)
            self.pilha = self.pilha.lstrip()
        elif(token=='real' or token=='integer'):
            self.pilha = self.pilha.replace('DC','DC_V MAIS_DC',1)
        else:
            raise Exception('Erro sintático.')

    def is_DCV(self, token):
        global pilha
        if(token=='real' or token=='integer'):
            self.pilha = self.pilha.replace('DC_V','TIPO_VAR : VARIAVEIS',1)
        else:
            raise Exception('Erro sintático.')

    def is_MAISDC(self, token):
        global pilha
        if(token==';'):
            self.pilha = self.pilha.replace('MAIS_DC','; DC',1)
        elif(token=='begin'):
            self.pilha = self.pilha.replace('MAIS_DC','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception('Erro sintático.')


    def is_TIPOVAR(self, token):
        global pilha
        if(token=='real'):
            self.pilha = self.pilha.replace('TIPO_VAR','real',1)
        elif(token=='integer'):
            self.pilha = self.pilha.replace('TIPO_VAR','integer',1)
        else:
            raise Exception('Erro sintático.')


    def is_VARIAVEIS(self, token):
        global pilha
        if(token=='ident'):
            self.pilha = self.pilha.replace('VARIAVEIS','ident MAIS_VAR',1)
        elif(token=='integer'):
            self.pilha = self.pilha.replace('VARIAVEIS','integer',1)
        else:
            raise Exception('Erro sintático.')



    def is_MAISVAR(self, token):
        global pilha
        if(token==';' or token=='begin'):
            self.pilha = self.pilha.replace('MAIS_VAR','ident MAIS_VAR',1)
        elif(token==','):
            self.pilha = self.pilha.replace('MAIS_VAR',', VARIAVEIS',1)
        else:
            raise Exception('Erro sintático.')


    def is_COMANDOS(self, token):
        global pilha
        if(token=='ident' or token=='write' or token=='read'):
            self.pilha = self.pilha.replace('COMANDOS','COMANDO MAIS_COMANDOS',1)
        else:
            raise Exception('Erro sintático.')


    def is_COMANDO(self, token):
        global pilha
        if(token=='ident'):
            self.pilha = self.pilha.replace('COMANDO','ident := EXPRESSAO',1)
        elif(token=='write'):
            self.pilha = self.pilha.replace('COMANDO','write ( ident )',1)
        elif(token=='read'):
            self.pilha = self.pilha.replace('COMANDO','read ( ident )',1)
        else:
            raise Exception('Erro sintático.')


    def is_MAISCOMANDOS(self, token):
        global pilha
        if(token==';'):
            self.pilha = self.pilha.replace('MAISCOMANDOS','; COMANDOS',1)
        elif(token=='end'):
            self.pilha = self.pilha.replace('MAISCOMANDOS','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception('Erro sintático.')


    def is_EXPRESSAO(self, token):
        global pilha
        if(token=='-' or token=='(' or token=='ident' or token=='numero_int' or token=='numero_real'):
            self.pilha = self.pilha.replace('EXPRESSAO','TERMO OUTROS_TERMOS',1)
        else:
            raise Exception('Erro sintático.')


    def is_TERMO(self, token):
        global pilha
        if(token=='-'):
            self.pilha = self.pilha.replace('TERMO','OP_UN FATOR MAIS_FATORES',1)
        else:
            raise Exception('Erro sintático.')


    def is_OUTROSTERMOS(self, token):
        global pilha
        if(token=='+' or token=='-'):
            self.pilha = self.pilha.replace('OUTROSTERMOS','OP_AD TERMO OUTROS_TERMOS',1)
        elif(token==';' or token==')' or token=='end'):
            self.pilha = self.pilha.replace('OUTROSTERMOS','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception('Erro sintático.')


    def is_OPUN(self, token):
        global pilha
        if(token=='-'):
            self.pilha = self.pilha.replace('OPUN','-',1)
        elif(token=='(' or token==')' or token=='ident' or token=='numero_int' or token==')' or token=='numero_real'):
            self.pilha = self.pilha.replace('OPUN','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception('Erro sintático.')


    def is_OPAD(self, token):
        global pilha
        if(token=='-'):
            self.pilha = self.pilha.replace('OPUN','-',1)
        elif(token=='+'):
            self.pilha = self.pilha.replace('OPUN','+',1)
        else:
            raise Exception('Erro sintático.')

    def is_OPMUL(self, token):
        global pilha
        if(token=='/'):
            self.pilha = self.pilha.replace('OPMUL','/',1)
        elif(token=='*'):
            self.pilha = self.pilha.replace('OPMUL','*',1)
        else:
            raise Exception('Erro sintático.')



    def is_FATOR(self, token):
        global pilha
        if(token=='('):
            self.pilha = self.pilha.replace('FATOR','( EXPRESSAO )',1)
        elif(token=='ident'):
            self.pilha = self.pilha.replace('FATOR','ident',1)
        elif(token=='numero_int'):
            self.pilha = self.pilha.replace('FATOR','numero_int',1)
        elif(token=='numero_real'):
            self.pilha = self.pilha.replace('FATOR','numero_real',1)
        else:
            raise Exception('Erro sintático.')

    def is_MAISFATORES(self, token):
        global pilha
        if(token=='+' or token=='-' or token==';' or token==')' or token=='end'):
            self.pilha = self.pilha.replace('MAISFATORES','',1)
            self.pilha = self.pilha.lstrip()
        elif(token=='/' or token=='*'):
            self.pilha = self.pilha.replace('MAISFATORES','OP_MUL FATOR MAIS_FATORES',1)
        else:
            raise Exception('Erro sintático.')

    #---------------------------------------FIM---------------------------------------




    #---------------------------------------INÍCIO DO MÉTODO PARA AVALIAR SINTAXE---------------------------------------
    
    def avaliaSintaxe(self,path):
        lexico = Lexico(path)

        lista = []
        while not(lexico.isEOF()):
            token = lexico.nextToken()
            #print(token.valor)
            if token.valor == "\n" and len(lista)>0:
                self.listaSubCadeias.append(lista)
                lista = []
            elif token.valor not in  ['\n',' ','\t']:
                lista.append(token.valor)

        if len(lista) > 0:
            self.listaSubCadeias.append(lista)
        # Até aqui é feita a separação dos tokens em subcadeias (linha por linha salva em uma lista)




        # Aqui se inicia a leitura de cada token das subcadeias salvas

        self.pilha = 'PROGRAMA$'
        self.cadeia = ''
        for listaSubCadeia in self.listaSubCadeias:
            #print("lista entrada: " + str(listaSubCadeia))
            for token in listaSubCadeia:
                #print(token)
                if (str(token).isnumeric() and '.' in token):
                    literal = token
                    token = 'numero_real'
                if (str(token).isnumeric() and '.' not in token):
                    literal = token
                    token = 'numero_inteiro'
                if ((self.pilha == '$') and (token == '$')):
                    break

                while not((self.pilha == '$') and (token == '$')):

                    # PILHA COM INICIAL NÃO TERMINAL
                    if (self.pilha.startswith('PROGRAMA')):
                        self.is_PROGRAMA(token)
                    elif (self.pilha.startswith('CORPO')):
                        self.is_CORPO(token)
                    elif (self.pilha.startswith('DC') and self.pilha[2] != "_"):
                        self.is_DC(token)
                    elif (self.pilha.startswith('DC_V')):
                        self.is_DCV(token)
                    elif (self.pilha.startswith('MAIS_DC')):
                        self.is_MAISDC(token)
                    elif(self.pilha.startswith('TIPO_VAR')):
                        self.is_TIPOVAR(token)
                    elif(self.pilha.startswith('VARIAVEIS')):
                        self.is_VARIAVEIS(token)
                    elif(self.pilha.startswith('MAIS_VAR')):
                        self.is_MAISVAR(token)
                    elif(self.pilha.startswith('COMANDO') and self.pilha[8] != "S"):
                        self.is_COMANDO(token)
                    elif(self.pilha.startswith('COMANDOS')):
                        self.is_COMANDOS(token)
                    elif(self.pilha.startswith('MAIS_COMANDOS')):
                        self.is_MAISCOMANDOS(token)
                    elif(self.pilha.startswith('EXPRESSAO')):
                        self.is_EXPRESSAO(token)
                    elif(self.pilha.startswith('TERMO')):
                        self.is_TERMO(token)
                    elif(self.pilha.startswith('OUTROS_TERMOS')):
                        self.is_OUTROSTERMOS(token)
                    elif(self.pilha.startswith('OP_UN')):
                        self.is_OPUN(token)
                    elif(self.pilha.startswith('OP_AD')):
                        self.is_OPAD(token)
                    elif(self.pilha.startswith('OP_MUL')):
                        self.is_OPMUL(token)
                    elif(self.pilha.startswith('FATOR')):
                        self.is_FATOR(token)
                    elif(self.pilha.startswith('MAIS_FATORES')):
                        self.is_MAISFATORES(token)
                    

                    # PILHA COM INICIAL TERMINAL

                    elif(self.pilha.startswith('+')):
                        self.pilha = self.pilha.replace('+','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '+'
                        break
                    elif(self.pilha.startswith('-')):
                        self.pilha = self.pilha.replace('-','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '-'
                        break
                    elif(self.pilha.startswith('/')):
                        self.pilha = self.pilha.replace('/','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '/'
                        break
                    elif(self.pilha.startswith('*')):
                        self.pilha = self.pilha.replace('*','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '*'
                        break
                    elif(self.pilha.startswith('.')):
                        self.pilha = self.pilha.replace('.','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '.'
                        break
                    elif(self.pilha.startswith(':')):
                        self.pilha = self.pilha.replace(':','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  ':'
                        break
                    elif(self.pilha.startswith(';')):
                        self.pilha = self.pilha.replace(';','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  ';'
                        break
                    elif(self.pilha.startswith(',')):
                        self.pilha = self.pilha.replace(',','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  ','
                        break
                    elif(self.pilha.startswith(':=')):
                        self.pilha = self.pilha.replace(':=','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  ':='
                        break
                    elif(self.pilha.startswith('(')):
                        self.pilha = self.pilha.replace('(','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '('
                        break
                    elif(self.pilha.startswith(')')):
                        self.pilha = self.pilha.replace(')','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  ')'
                        break
                    elif(self.pilha.startswith('begin')):
                        self.pilha = self.pilha.replace('begin','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'begin'
                        break
                    elif(self.pilha.startswith('end')):
                        self.pilha = self.pilha.replace('end','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'end'
                        break
                    elif(self.pilha.startswith('real')):
                        self.pilha = self.pilha.replace('real','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'real'
                        break
                    elif(self.pilha.startswith('integer')):
                        self.pilha = self.pilha.replace('integer','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'integer'
                        break
                    elif(self.pilha.startswith('ident')):
                        self.pilha = self.pilha.replace('ident','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  token
                        break
                    elif(self.pilha.startswith('write')):
                        self.pilha = self.pilha.replace('write','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'write'
                        break
                    elif(self.pilha.startswith('read')):
                        self.pilha = self.pilha.replace('read','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'read'
                        break
                    elif(self.pilha.startswith('numero_int')):
                        self.pilha = self.pilha.replace('numero_int','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'numero_int'
                        break
                    elif(self.pilha.startswith('numero_real')):
                        self.pilha = self.pilha.replace('numero_real','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'numero_real'
                        break
                    elif(self.pilha.startswith('program')):
                        self.pilha = self.pilha.replace('program','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'program'
                        self.cadeia = self.cadeia.lstrip()
                        break
                    elif(self.pilha.startswith("$")):
                        self.pilha = self.pilha.replace("$","", 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '$'
                        break 
                
            







def main():

    sintatico = Sintatico()
    sintatico.avaliaSintaxe('entrada.txt')

    # tokens = ['program','teste', 'real', ':', 'a',',','b',';', 'begin', 'read', '(', 'a', ')', ';', '1.5', 'b', ':=', 'a', '*', 'a', ';','write','(','b',')',';','end']
    # Sintatico(tokens)
    # print("Cadeia aceita")


main()