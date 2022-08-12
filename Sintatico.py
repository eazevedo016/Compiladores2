def is_PROGRAMA(token):
    global pilha
    if(token=='program'):
        pilha = pilha.replace('PROGRAMA','program ident CORPO .',1)
    else:
        raise Exception('Erro sintático.')

def is_CORPO(token):
    global pilha
    if(token=='real' or token=='integer'):
        pilha = pilha.replace('CORPO','DC begin COMANDOS end',1)
    else:
        raise Exception('Erro sintático.')

def is_DC(token):
    global pilha
    if(token=='begin'):
        pilha = pilha.replace('DC','',1)
        pilha = pilha.lstrip()
    elif(token=='real' or token=='integer'):
        pilha = pilha.replace('DC','DC_V MAIS_DC',1)
    else:
        raise Exception('Erro sintático.')

def is_DCV(token):
    global pilha
    if(token=='real' or token=='integer'):
        pilha = pilha.replace('DC_V','TIPO_VAR : VARIAVEIS',1)
    else:
        raise Exception('Erro sintático.')

def is_MAISDC(token):
    global pilha
    if(token==';'):
        pilha = pilha.replace('MAIS_DC','; DC',1)
    elif(token=='begin'):
        pilha = pilha.replace('MAIS_DC','',1)
        pilha = pilha.lstrip()
    else:
        raise Exception('Erro sintático.')


def is_TIPOVAR(token):
    global pilha
    if(token=='real'):
        pilha = pilha.replace('TIPO_VAR','real',1)
    elif(token=='integer'):
        pilha = pilha.replace('TIPO_VAR','integer',1)
    else:
        raise Exception('Erro sintático.')


def is_VARIAVEIS(token):
    global pilha
    if(token=='ident'):
        pilha = pilha.replace('VARIAVEIS','ident MAIS_VAR',1)
    elif(token=='integer'):
        pilha = pilha.replace('VARIAVEIS','integer',1)
    else:
        raise Exception('Erro sintático.')



def is_MAISVAR(token):
    global pilha
    if(token==';' or token=='begin'):
        pilha = pilha.replace('MAIS_VAR','ident MAIS_VAR',1)
    elif(token==','):
        pilha = pilha.replace('MAIS_VAR',', VARIAVEIS',1)
    else:
        raise Exception('Erro sintático.')


def is_COMANDOS(token):
    global pilha
    if(token=='ident' or token=='write' or token=='read'):
        pilha = pilha.replace('COMANDOS','COMANDO MAIS_COMANDOS',1)
    else:
        raise Exception('Erro sintático.')


def is_COMANDO(token):
    global pilha
    if(token=='ident'):
        pilha = pilha.replace('COMANDO','ident := EXPRESSAO',1)
    elif(token=='write'):
        pilha = pilha.replace('COMANDO','write ( ident )',1)
    elif(token=='read'):
        pilha = pilha.replace('COMANDO','read ( ident )',1)
    else:
        raise Exception('Erro sintático.')


def is_MAISCOMANDOS(token):
    global pilha
    if(token==';'):
        pilha = pilha.replace('MAISCOMANDOS','; COMANDOS',1)
    elif(token=='end'):
        pilha = pilha.replace('MAISCOMANDOS','',1)
        pilha = pilha.lstrip()
    else:
        raise Exception('Erro sintático.')


def is_EXPRESSAO(token):
    global pilha
    if(token=='-' or token=='(' or token=='ident' or token=='numero_int' or token=='numero_real'):
        pilha = pilha.replace('EXPRESSAO','TERMO OUTROS_TERMOS',1)
    else:
        raise Exception('Erro sintático.')


def is_TERMO(token):
    global pilha
    if(token=='-'):
        pilha = pilha.replace('TERMO','OP_UN FATOR MAIS_FATORES',1)
    else:
        raise Exception('Erro sintático.')


def is_OUTROSTERMOS(token):
    global pilha
    if(token=='+' or token=='-'):
        pilha = pilha.replace('OUTROSTERMOS','OP_AD TERMO OUTROS_TERMOS',1)
    elif(token==';' or token==')' or token=='end'):
        pilha = pilha.replace('OUTROSTERMOS','',1)
        pilha = pilha.lstrip()
    else:
        raise Exception('Erro sintático.')


def is_OPUN(token):
    global pilha
    if(token=='-'):
        pilha = pilha.replace('OPUN','-',1)
    elif(token=='(' or token==')' or token=='ident' or token=='numero_int' or token==')' or token=='numero_real'):
        pilha = pilha.replace('OPUN','',1)
        pilha = pilha.lstrip()
    else:
        raise Exception('Erro sintático.')


def is_OPAD(token):
    global pilha
    if(token=='-'):
        pilha = pilha.replace('OPUN','-',1)
    elif(token=='+'):
        pilha = pilha.replace('OPUN','+',1)
    else:
        raise Exception('Erro sintático.')

def is_OPMUL(token):
    global pilha
    if(token=='/'):
        pilha = pilha.replace('OPMUL','/',1)
    elif(token=='*'):
        pilha = pilha.replace('OPMUL','*',1)
    else:
        raise Exception('Erro sintático.')



def is_FATOR(token):
    global pilha
    if(token=='('):
        pilha = pilha.replace('FATOR','( EXPRESSAO )',1)
    elif(token=='ident'):
        pilha = pilha.replace('FATOR','ident',1)
    elif(token=='numero_int'):
        pilha = pilha.replace('FATOR','numero_int',1)
    elif(token=='numero_real'):
        pilha = pilha.replace('FATOR','numero_real',1)
    else:
        raise Exception('Erro sintático.')

def is_MAISFATORES(token):
    global pilha
    if(token=='+' or token=='-' or token==';' or token==')' or token=='end'):
        pilha = pilha.replace('MAISFATORES','',1)
        pilha = pilha.lstrip()
    elif(token=='/' or token=='*'):
        pilha = pilha.replace('MAISFATORES','OP_MUL FATOR MAIS_FATORES',1)
    else:
        raise Exception('Erro sintático.')

# -------------------------FIM VERIFICAÇÕES-------------------------





def Sintatico(tokens):

    global pilha 
    global cadeia

    pilha = 'PROGRAMA$'
    cadeia = ''

    for token in tokens:
        if ((pilha == '$') and (token == '$')):
            break
        tokens.append("$")
        while not((pilha == '$') and (token == '$')):

            # PILHA COM INICIAL NÃO TERMINAL
            if (pilha.startswith('PROGRAMA')):
                is_PROGRAMA(token)
            elif (pilha.startswith('CORPO')):
                is_CORPO(token)
            elif (pilha.startswith('DC') and pilha[2] != "_"):
                is_DC(token)
            elif (pilha.startswith('DC_V')):
                is_DCV(token)
            elif (pilha.startswith('MAIS_DC')):
                is_MAISDC(token)
            elif(pilha.startswith('TIPO_VAR')):
                is_TIPOVAR(token)
            elif(pilha.startswith('VARIAVEIS')):
                is_VARIAVEIS(token)
            elif(pilha.startswith('MAIS_VAR')):
                is_MAISVAR(token)
            elif(pilha.startswith('COMANDO') and pilha[8] != "S"):
                is_COMANDO(token)
            elif(pilha.startswith('COMANDOS')):
                is_COMANDOS(token)
            elif(pilha.startswith('MAIS_COMANDOS')):
                is_MAISCOMANDOS(token)
            elif(pilha.startswith('EXPRESSAO')):
                is_EXPRESSAO(token)
            elif(pilha.startswith('TERMO')):
                is_TERMO(token)
            elif(pilha.startswith('OUTROS_TERMOS')):
                is_OUTROSTERMOS(token)
            elif(pilha.startswith('OP_UN')):
                is_OPUN(token)
            elif(pilha.startswith('OP_AD')):
                is_OPAD(token)
            elif(pilha.startswith('OP_MUL')):
                is_OPMUL(token)
            elif(pilha.startswith('FATOR')):
                is_FATOR(token)
            elif(pilha.startswith('MAIS_FATORES')):
                is_MAISFATORES(token)
            

            # PILHA COM INICIAL TERMINAL

            elif(pilha.startswith('+')):
                pilha = pilha.replace('+','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '+'
                break
            elif(pilha.startswith('-')):
                pilha = pilha.replace('-','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '-'
                break
            elif(pilha.startswith('/')):
                pilha = pilha.replace('/','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '/'
                break
            elif(pilha.startswith('*')):
                pilha = pilha.replace('*','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '*'
                break
            elif(pilha.startswith('.')):
                pilha = pilha.replace('.','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '.'
                break
            elif(pilha.startswith(':')):
                pilha = pilha.replace(':','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + ':'
                break
            elif(pilha.startswith(';')):
                pilha = pilha.replace(';','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + ';'
                break
            elif(pilha.startswith(',')):
                pilha = pilha.replace(',','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + ','
                break
            elif(pilha.startswith(':=')):
                pilha = pilha.replace(':=','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + ':='
                break
            elif(pilha.startswith('(')):
                pilha = pilha.replace('(','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '('
                break
            elif(pilha.startswith(')')):
                pilha = pilha.replace(')','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + ')'
                break
            elif(pilha.startswith('begin')):
                pilha = pilha.replace('begin','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'begin'
                break
            elif(pilha.startswith('end')):
                pilha = pilha.replace('end','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'end'
                break
            elif(pilha.startswith('real')):
                pilha = pilha.replace('real','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'real'
                break
            elif(pilha.startswith('integer')):
                pilha = pilha.replace('integer','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'integer'
                break
            elif(pilha.startswith('ident')):
                pilha = pilha.replace('ident','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'ident'
                break
            elif(pilha.startswith('write')):
                pilha = pilha.replace('write','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'write'
                break
            elif(pilha.startswith('read')):
                pilha = pilha.replace('read','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'read'
                break
            elif(pilha.startswith('numero_int')):
                pilha = pilha.replace('numero_int','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'numero_int'
                break
            elif(pilha.startswith('numero_real')):
                pilha = pilha.replace('numero_real','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'numero_real'
                break
            elif(pilha.startswith('program')):
                pilha = pilha.replace('program','', 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + 'program'
                break
            elif(pilha.startswith("$")):
                pilha = pilha.replace("$","", 1)
                pilha = pilha.lstrip()
                cadeia = cadeia + '$'
                break 
            
            







def main():

    tokens = ['program','teste', 'real', ':', 'a',',','b',';', 'begin', 'read', '(', 'a', ')', ';', '1.5', 'b', ':=', 'a', '*', 'a', ';','write','(','b',')',';','end']
    Sintatico(tokens)
    print("Cadeia aceita")


main()