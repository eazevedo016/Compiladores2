# Autômato
![image](https://user-images.githubusercontent.com/75282286/184503154-23dc5e00-8bd6-43fb-816d-9406d7c15770.png)



# Gramática 
 
- PROGRAMA -> program ident CORPO .
- CORPO -> DC begin COMANDOS end
- DC -> DC_V MAIS_DC  
- DC -> 
- MAIS_DC -> ; DC 
- MAIS_DC -> 
- DC_V ->  TIPO_VAR : VARIAVEIS
- TIPO_VAR -> real 
- TIPO_VAR -> integer
- VARIAVEIS -> ident MAIS_VAR
- MAIS_VAR -> , VARIAVEIS 
- MAIS_VAR -> 
- COMANDOS -> COMANDO MAIS_COMANDOS
- MAIS_COMANDOS -> ; COMANDOS 
- MAIS_COMANDOS -> 
- COMANDO -> read ( ident ) 
- COMANDO -> write ( ident )
- COMANDO -> ident := EXPRESSAO						
- EXPRESSAO -> TERMO OUTROS_TERMOS
- TERMO -> OP_UN FATOR MAIS_FATORES
- OP_UN -> - 
- OP_UN -> 
- FATOR -> ident 
- FATOR -> numero_int 
- FATOR -> numero_real 
- FATOR -> ( EXPRESSAO )
- OUTROS_TERMOS -> OP_AD TERMO OUTROS_TERMOS 
- OUTROS_TERMOS -> 
- OP_AD -> + 
- OP_AD -> -
- MAIS_FATORES -> OP_MUL FATOR MAIS_FATORES 
- MAIS_FATORES -> 
- OP_MUL -> *
- OP_MUL -> /



# Alfabeto
Terminais:
- :=  ; : ( ) program ident begin end real integer read write numero_int numero_real 

Não terminais
- PROGRAMA CORPO DC COMANDOS DC_V MAIS_DC TIPO_VAR VARIAVEIS MAIS_VAR COMANDO MAIS_COMANDOS EXPRESSAO TERMO OUTROS_TERMOS OP_UN FATOR MAIS_FATORES OP_AD OP_MUL

# First e Follow

## First

- FIRST(PROGRAMA) -> { program }
- FIRST(CORPO) -> { begin integer real }
- FIRST(DC) -> { integer real λ }
- FIRST(COMANDOS) -> { ident read write  }
- FIRST(DC_V) -> { integer real }
- FIRST(MAIS_DC) -> { ; λ }
- FIRST(TIPO_VAR) -> { integer real }
- FIRST(VARIAVEIS) -> { ident }
- FIRST(MAIS_VAR) -> { , λ }
- FIRST(COMANDO) -> { ident read write }
- FIRST(MAIS_COMANDOS) -> { ; λ }
- FIRST(EXPRESSAO) -> { ident ( - numero_int numero_real }
- FIRST(TERMO) -> { ident ( - numero_int numero_real }
- FIRST(OUTROS_TERMOS) -> { - + λ }
- FIRST(OP_UN) -> { - λ }
- FIRST(FATOR) -> { ident ( numero_int numero_real }
- FIRST(MAIS_FATORES) -> { / * λ }
- FIRST(OP_AD) -> { - + }
- FIRST(OP_MUL) -> { / * }


## Follow

- FOLLOW(PROGRAMA) -> {  }
- FOLLOW(CORPO) -> { . }
- FOLLOW(DC) -> { begin }
- FOLLOW(COMANDOS) -> { end }
- FOLLOW(DC_V) -> { begin ; }
- FOLLOW(MAIS_DC) -> { begin }
- FOLLOW(TIPO_VAR) -> { : }
- FOLLOW(VARIAVEIS) -> { begin ; }
- FOLLOW(MAIS_VAR) -> { begin ; }
- FOLLOW(COMANDO) -> { end ; }
- FOLLOW(MAIS_COMANDOS) -> { end }
- FOLLOW(EXPRESSAO) -> { end ; ) }
- FOLLOW(TERMO) -> { end ; ) - + }
- FOLLOW(OUTROS_TERMOS) -> { end ; ) }
- FOLLOW(OP_UN) -> { ident ( numero_int numero_real }
- FOLLOW(FATOR) -> { end ; ) - + / * }
- FOLLOW(MAIS_FATORES) -> { end ; ) - + }
- FOLLOW(OP_AD) -> { ident ( - numero_int numero_real }
- FOLLOW(OP_MUL) -> { ident ( numero_int numero_real }


# Analisador Semântico

- Não se pode usar uma variável que não tenha sido previamente declarada;
- Não se pode declarar uma mesma variável mais de uma vez;
- O padrão de nome para declaração de variável consiste no uso de letras minúsculas sem acentuação podendo se usar o underline(_).

# Código objeto

Foram utilizados os seguintes códigos de instrução para execução da máquian hipotética:
- INPP   inicia programa
- MULT   multiplica elemento do topo pelo antecessor
- SOMA   soma topo da pilha com seu antecessor
- INVE   inverte sinal do topo
- DIVI   divide elemento do antecessor pelo do topo
- SUBT   subtrai o elemento do topo do antecessor
- ARMZ   armazena o topo da pilha no endereço n
- LEIT   lê um dado do arquivo de entrada
- ALME   reserva m posições na pilha
- CRCT   carrega constante k na pilha
- CRVL   carrega valor de endereço n na pilha
- PARA   termina a execução do programa
- IMPR   imprime valor inteiro








