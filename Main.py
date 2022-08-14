from Sintatico import Sintatico
from MaquinaHipotetica import MaquinaHipotetica

def main():

    sintatico = Sintatico()
    
    sintatico.avaliaSintaxe('entrada.txt')
    print("\n***************************************************************************************\n")
    print("Entrada sintaticamente correta.")
    print("\n***************************************************************************************")
    print("Codigo objeto gerado: \n")
    i= 0
    for token in sintatico.pilhaGeraCodigo.pilhaPosFixa:
        print(f"{i:3}\t{token}")
        i += 1
    
    print("\n***************************************************************************************")
    maquinaHipotetica = MaquinaHipotetica(sintatico.pilhaGeraCodigo.pilhaPosFixa)
    maquinaHipotetica.Executor()
    

main()