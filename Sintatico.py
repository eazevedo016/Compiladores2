from Lexico import Lexico
from Token import Token,TipoToken
from PosFixa import PosFixa


class TabelaVariaveis():
    tabelaVariaveis = []
    inserirNatabelaVariaveis = False
    entrouBegin = False
    #variaveis de controle
    def inserir(self, novaVariavel):
        if self.inserirNatabelaVariaveis:
            if novaVariavel in self.tabelaVariaveis:
                raise Exception(f"Erro semântico: '{novaVariavel}' já foi declarado(a).")
            else:
                self.tabelaVariaveis.append(novaVariavel)
        else:
            pass
    
    def posicaoVariavel(self,variavel):
        if variavel in self.tabelaVariaveis:
            return self.tabelaVariaveis.index(variavel)
        else:
            raise Exception(f"Erro semântico: '{variavel}' não foi declarado(a).")


class Sintatico():
    listaSubCadeias = []
    pilha = ""
    linha = 0
    geraCodigo = []
    tabelaVariaveis = TabelaVariaveis()
    pilhaGeraCodigo = PosFixa()

    #variaveis de controle
    mudarParaARMZ = False
    

    # ---------------------------------------MÉTODOS DE CONSULTA NA TABELA M---------------------------------------

    

    def is_PROGRAMA(self, token):
        
        if(token.valor=='program'):
            self.pilha = self.pilha.replace('PROGRAMA','program ident CORPO .',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

    def is_CORPO(self, token):
        
        if(token.valor=='real' or token.valor=='integer'):
            self.pilha = self.pilha.replace('CORPO','DC begin COMANDOS end',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

    def is_DC(self, token):
        
        if(token.valor=='begin' or token.valor=='$'):
            self.pilha = self.pilha.replace('DC','',1)
            self.pilha = self.pilha.lstrip()
        elif(token.valor=='real' or token.valor=='integer'):
            self.pilha = self.pilha.replace('DC','DC_V MAIS_DC',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

    def is_DCV(self, token):
        
        if(token.valor=='real' or token.valor=='integer'):
            self.pilha = self.pilha.replace('DC_V','TIPO_VAR : VARIAVEIS',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

    def is_MAISDC(self, token):
        
        if(token.valor==';'):
            self.pilha = self.pilha.replace('MAIS_DC','; DC',1)
        elif(token.valor=='begin' or token=='$'):
            self.pilha = self.pilha.replace('MAIS_DC','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_TIPOVAR(self, token):
        
        if(token.valor=='real'):
            self.pilha = self.pilha.replace('TIPO_VAR','real',1)
        elif(token.valor=='integer'):
            self.pilha = self.pilha.replace('TIPO_VAR','integer',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_VARIAVEIS(self, token):
        
        if(token.valor=='ident'): 
            self.tabelaVariaveis.inserirNatabelaVariaveis = True;  
            self.pilha = self.pilha.replace('VARIAVEIS','ident MAIS_VAR',1)
        elif(token.valor=='integer'):
            self.pilha = self.pilha.replace('VARIAVEIS','integer',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")



    def is_MAISVAR(self, token):
        
        if(token.valor==','):
            self.pilha = self.pilha.replace('MAIS_VAR',', VARIAVEIS',1)
        elif(token.valor=='$' or token.valor=='begin' or token.valor==';'):
            self.pilha = self.pilha.replace('MAIS_VAR','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_COMANDOS(self, token):
        
        if(token.valor=='ident' or token.valor=='write' or token.valor=='read'):
            self.pilha = self.pilha.replace('COMANDOS','COMANDO MAIS_COMANDOS',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_COMANDO(self, token):
        
        if(token.valor=='ident'):
            self.mudarParaARMZ = True
            self.pilha = self.pilha.replace('COMANDO','ident := EXPRESSAO',1)
        elif(token.valor=='write'):
            self.pilha = self.pilha.replace('COMANDO','write ( ident )',1)
        elif(token.valor=='read'):
            self.mudarParaARMZ = True
            self.pilha = self.pilha.replace('COMANDO','read ( ident )',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_MAISCOMANDOS(self, token):
        
        if(token.valor==';'):
            self.pilha = self.pilha.replace('MAIS_COMANDOS','; COMANDOS',1)
        elif(token.valor=='end' or token.valor=='$'):
            self.pilha = self.pilha.replace('MAIS_COMANDOS','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_EXPRESSAO(self, token):
        
        if(token.valor=='-' or token.valor=='(' or token.valor=='ident' or token.valor=='numero_inteiro' or token.valor=='numero_real' or token.valor==';' or token.valor==')' or token.valor=='end'):
            self.pilha = self.pilha.replace('EXPRESSAO','TERMO OUTROS_TERMOS',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_TERMO(self, token):
        
        if(token.valor=='-' or token.valor=='ident' or token.valor=='end' or token.valor==';' or token.valor=='(' or token.valor==')' or token.valor=='numero_inteiro' or token.valor=='numero_real' or token.valor=='+'):
            self.pilha = self.pilha.replace('TERMO','OP_UN FATOR MAIS_FATORES',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_OUTROSTERMOS(self, token):
        
        if(token.valor=='+' or token.valor=='-'):
            self.pilha = self.pilha.replace('OUTROS_TERMOS','OP_AD TERMO OUTROS_TERMOS',1)
        elif(token.valor==';' or token.valor==')' or token.valor=='end' or token.valor=='$'):
            self.pilha = self.pilha.replace('OUTROS_TERMOS','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_OPUN(self, token):
        
        if(token=='-'):
            self.pilhaGeraCodigo.ajustarPilhas(["INVE",""])
            self.pilha = self.pilha.replace('OP_UN','-',1)
        elif(token.valor=='(' or token.valor==')' or token.valor=='$' or token.valor=='ident' or token.valor=='numero_inteiro' or token.valor=='numero_real'):
            self.pilha = self.pilha.replace('OP_UN','',1)
            self.pilha = self.pilha.lstrip()
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")


    def is_OPAD(self, token):
        
        if(token.valor=='-'):
            self.pilha = self.pilha.replace('OP_AD','-',1)
        elif(token.valor=='+'):
            self.pilha = self.pilha.replace('OP_AD','+',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

    def is_OPMUL(self, token):
        
        if(token.valor=='/'):
            self.pilha = self.pilha.replace('OP_MUL','/',1)
        elif(token.valor=='*'):
            self.pilha = self.pilha.replace('OP_MUL','*',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")



    def is_FATOR(self, token):
        
        if(token.valor=='('):
            self.pilha = self.pilha.replace('FATOR','( EXPRESSAO )',1)
        elif(token.valor=='ident'):
            self.pilha = self.pilha.replace('FATOR','ident',1)
        elif(token.valor=='numero_inteiro'):
            self.pilha = self.pilha.replace('FATOR','numero_inteiro',1)
        elif(token.valor=='numero_real'):
            self.pilha = self.pilha.replace('FATOR','numero_real',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

    def is_MAISFATORES(self, token):
        
        if(token.valor=='+' or token.valor=='-' or token.valor==';' or token.valor==')' or token.valor=='end' or token.valor=='$'):
            self.pilha = self.pilha.replace('MAIS_FATORES','',1)
            self.pilha = self.pilha.lstrip()
        elif(token.valor=='/' or token.valor=='*'):
            self.pilha = self.pilha.replace('MAIS_FATORES','OP_MUL FATOR MAIS_FATORES',1)
        else:
            raise Exception(f"Erro sintático.\nToken: {token.valor}\nLinha: {self.linha}")

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
                lista.append(token)

        if len(lista) > 0:
            self.listaSubCadeias.append(lista)
        # Até aqui é feita a separação dos tokens em subcadeias (linha por linha salva em uma lista)




        # Aqui se inicia a leitura de cada token das subcadeias salvas

        self.pilha = 'PROGRAMA$'
        self.cadeia = ''
        for listaSubCadeia in self.listaSubCadeias:
            self.geraCodigo.append(['$',''])
            self.linha += 1
            #print("lista entrada: " + str(listaSubCadeia))
            for token in listaSubCadeia:
                #print(token)
                if (token.tipo.value==1):
                    literal = token.valor
                    token.valor = 'numero_real'
                if (token.tipo.value==0):
                    literal = token.valor
                    token.valor = 'numero_inteiro'
                if ((self.pilha == '$') and (token.valor == '$')):
                    break

                while not((self.pilha == '$') and (token.valor == '$')):

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
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_VARIAVEIS(token)
                        if (token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('MAIS_VAR')):
                        self.is_MAISVAR(token)

                    elif(self.pilha.startswith('COMANDO') and self.pilha[7] != "S"):
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_COMANDO(token)
                        if (token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('COMANDOS')):
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_COMANDOS(token)
                        if(token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('MAIS_COMANDOS')):
                        self.is_MAISCOMANDOS(token)

                    elif(self.pilha.startswith('EXPRESSAO')):
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_EXPRESSAO(token)
                        if (token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('TERMO')):
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_TERMO(token)
                        if (token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('OUTROS_TERMOS')):
                        self.is_OUTROSTERMOS(token)

                    elif(self.pilha.startswith('OP_UN')):
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_OPUN(token)
                        if (token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('OP_AD')):
                        self.is_OPAD(token)

                    elif(self.pilha.startswith('OP_MUL')):
                        self.is_OPMUL(token)

                    elif(self.pilha.startswith('FATOR')):
                        
                        if(token.tipo.value==8):
                            literal = token.valor
                            token.valor = 'ident'
                        self.is_FATOR(token)
                        if (token.tipo.value==8):
                            token.valor = literal

                    elif(self.pilha.startswith('MAIS_FATORES')):
                        self.is_MAISFATORES(token)
                    

                    # PILHA COM INICIAL TERMINAL

                    elif(self.pilha.startswith('+')):
                        self.pilhaGeraCodigo.ajustarPilhas(['SOMA', ''])
                        self.pilha = self.pilha.replace('+','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '+'
                        break
                    elif(self.pilha.startswith('-')):
                        self.pilhaGeraCodigo.ajustarPilhas(['SUBT', ''])
                        self.pilha = self.pilha.replace('-','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '-'
                        break
                    elif(self.pilha.startswith('/')):
                        self.pilhaGeraCodigo.ajustarPilhas(['DIVI', ''])
                        self.pilha = self.pilha.replace('/','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '/'
                        break
                    elif(self.pilha.startswith('*')):
                        self.pilhaGeraCodigo.ajustarPilhas(['MULT', ''])
                        self.pilha = self.pilha.replace('*','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '*'
                        break
                    elif(self.pilha.startswith('.')):
                        self.pilha = self.pilha.replace('.','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '.'
                        break
                    elif(self.pilha.startswith(':') and self.pilha[1] != "="):
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
                        self.pilhaGeraCodigo.inserirPilha(['(',''])
                        self.pilha = self.pilha.replace('(','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  '('
                        break
                    elif(self.pilha.startswith(')')):
                        self.pilhaGeraCodigo.desempilharParenteses()
                        self.pilha = self.pilha.replace(')','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  ')'
                        break
                    elif(self.pilha.startswith('begin')):
                        self.pilha = self.pilha.replace('begin','', 1)
                        self.tabelaVariaveis.inserirNatabelaVariaveis = False 
                        self.tabelaVariaveis.entrouBegin = True 
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'begin'
                        break
                    elif(self.pilha.startswith('end')):
                        self.pilhaGeraCodigo.inserirPosfixa(['PARA', 0])
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
                        if(self.tabelaVariaveis.inserirNatabelaVariaveis):
                            self.tabelaVariaveis.inserir(token.valor)
                            self.pilhaGeraCodigo.inserirPosfixa(['ALME', 0]) #ALME
                        elif self.tabelaVariaveis.entrouBegin:
                            if self.mudarParaARMZ:
                                self.pilhaGeraCodigo.ajustarPilhas(['ARMZ', self.tabelaVariaveis.posicaoVariavel(token.valor)]) #CRLV
                                self.mudarParaARMZ = False
                            else:
                                self.pilhaGeraCodigo.inserirPosfixa(['CRVL', self.tabelaVariaveis.posicaoVariavel(token.valor)]) #CRLV
                        self.pilha = self.pilha.replace('ident','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  token.valor
                        break
                    elif(self.pilha.startswith('write')):
                        self.pilhaGeraCodigo.ajustarPilhas(['IMPR', ''])
                        self.pilha = self.pilha.replace('write','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'write'
                        break
                    elif(self.pilha.startswith('read')):
                        self.pilhaGeraCodigo.inserirPosfixa(['LEIT', ''])
                        self.pilha = self.pilha.replace('read','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  'read'
                        break
                    elif(self.pilha.startswith('numero_inteiro')):
                        self.pilhaGeraCodigo.inserirPosfixa(['CRCT', literal])
                        self.pilha = self.pilha.replace('numero_inteiro','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  literal
                        break
                    elif(self.pilha.startswith('numero_real')):
                        self.pilhaGeraCodigo.inserirPosfixa(['CRCT', literal])
                        self.pilha = self.pilha.replace('numero_real','', 1)
                        self.pilha = self.pilha.lstrip()
                        self.cadeia = self.cadeia + ' ' +  literal
                        break
                    elif(self.pilha.startswith('program')):
                        self.pilhaGeraCodigo.inserirPosfixa(["INPP",""]) #INPP
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
            self.pilhaGeraCodigo.desempilharTudo()            
