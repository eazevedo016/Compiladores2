from PosFixa import PosFixa
class MaquinaHipotetica():
    
    def __init__(self,pilhaCodigo):
        self.pilhaCodigo = pilhaCodigo
        self.pilhaDados = []


    def Executor(self):
        for token in self.pilhaCodigo:
            funcao = token[0]
            valor = token[1]

            if funcao == 'INPP':
                pass
            
            elif funcao == 'MULT':
                valor1 = self.pilhaDados.pop(-2)
                valor2 = self.pilhaDados.pop()
                self.pilhaDados.append(valor1 * valor2)

            elif funcao == 'SOMA':
                valor1 = self.pilhaDados.pop(-2)
                valor2 = self.pilhaDados.pop()
                self.pilhaDados.append(valor1 + valor2)

            elif funcao == 'INVE':
                valor = self.pilhaDados.pop()
                self.pilhaDados.append(-1 * valor)

            elif funcao == 'DIVI':
                valor1 = self.pilhaDados.pop(-2)
                valor2 = self.pilhaDados.pop()
                self.pilhaDados.append(valor1 / valor2)


            elif funcao == 'SUBT':
                valor1 = self.pilhaDados.pop(-2)
                valor2 = self.pilhaDados.pop()
                self.pilhaDados.append(valor1 - valor2)

            elif funcao == 'ARMZ':
                valor1 = self.pilhaDados.pop()
                self.pilhaDados[valor] = valor1


            elif funcao == 'LEIT':
                inputVar = float(input("input: "))
                self.pilhaDados.append(inputVar)
            
            elif funcao == 'ALME':
                self.pilhaDados.append(0)

            elif funcao == "CRCT":
                self.pilhaDados.append(float(valor))

            elif funcao == "CRVL":
                self.pilhaDados.append(float(self.pilhaDados[valor]))

            elif funcao == 'PARA':
                 print("Fim")

            elif funcao == 'IMPR':
                 valor = str(self.pilhaDados.pop())
                 print(f"output: {valor}")


                


