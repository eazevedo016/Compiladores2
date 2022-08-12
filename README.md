# Autômato
![image](https://user-images.githubusercontent.com/75282286/183781215-6047fa4d-a427-46da-a9d7-7e227313ae0f.png)


# Alfabeto
Terminais:
- :=  , ; , : , ( , ) , program , ident , begin , end , real , integer  , read , write , numero_int , numero_real 

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





