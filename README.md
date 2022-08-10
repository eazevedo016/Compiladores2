# Autômato
![image](https://user-images.githubusercontent.com/75282286/183781215-6047fa4d-a427-46da-a9d7-7e227313ae0f.png)


# Alfabeto
Terminais:
- :=  , ; , : , ( , ) , program , ident , begin , end , real , integer  , read , write , numero_int , numero_real 

# First e Follow

## First
- First (programa) 		  = { program }
- First (corpo) 		      = {	}										U First (dc) 			  = { λ , real , integer }
- First (dc) 			      = { λ }										U First (dc_v)		  = { λ , real , integer }
- First (mais_dc) 		  = { ; , λ }
- First (dc_v) 			  = {  }   									    U First (tipo_var)	  = { real , integer }
- First (tipo_var) 		  = { real , integer }
- First (variaveis) 	      = { ident }
- First (mais_var) 		  = { , λ }
- First (comandos) 		  = {  }										U First (comando)		  = { read , write , ident }
- First (mais_comandos)     = { ; , λ }
- First (comando) 		  = { read , write , ident }
- First (expressao) 	      = {  }										U First (termo)		  = { - , λ }
- First (termo) 		      = {  }										U First (op_un)		  = { - , λ }
- First (op_un) 		      = { - , λ }
- First (fator) 		      = { ident , numero_int , numero_real , ( }
- First (outros_termos)     = { λ }										U First (op_ad)		  = { λ , + , - }
- First (op_ad) 		      = { + , - }
- First (mais_fatores) 	  = { λ }										U First (op_mul)		  = { λ , * , / }
- First (op_mul) 		      = { * , / }

-sintetizando:

- First (programa) 		  = { program }
- First (corpo) 		      = { λ , real , integer }
- First (dc) 			      = { λ , real , integer }
- First (mais_dc) 		  = { ; , λ }
- First (dc_v) 			  = { real , integer }
- First (tipo_var) 		  = { real , integer }
- First (variaveis) 	      = { ident }
- First (mais_var) 		  = { , λ }
- First (comandos) 		  = { read , write , ident }
- First (mais_comandos)     = { ; , λ }
- First (comando) 		  = { read , write , ident }
- First (expressao) 	      = { - , λ }
- First (termo) 		      = { - , λ }
- First (op_un) 		      = { - , λ }
- First (fator) 		      = { ident , numero_int , numero_real , ( }
- First (outros_termos)     = { λ , + , - }
- First (op_ad) 		      = { + , - }
- First (mais_fatores) 	  = { λ , * , / }
- First (op_mul) 		      = { * , / }


