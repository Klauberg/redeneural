from sigmoid import *
from dados import *

class Sigmoid:
    def sigmoid(self,x):

        try:
            float(x)
            sig = Calculo()
            calculo= sig.sigmoid(float(x))
            salva = Salva()
            salva.salva_dados(calculo)
            print(calculo)
        except:
            print("Valor Incorreto")

    def limpa_txt(self):
        limpa = Reseta()
        limpa.reseta_dados()

    def entrada_notas(self):
        nota = Leitura()
        dados=(nota.ler_dados())
        for i in dados:
            self.sigmoid(i)



sig = Sigmoid()
sig.sigmoid(0.5)
