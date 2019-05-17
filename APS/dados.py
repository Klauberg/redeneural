from data import Converte


class Leitura:

    def __init__(self):
        pass

    def ler_dados(self):
        arquivo = open("DadosEntrada.txt", "r")
        dado=[]
        for linha in arquivo:
            dado.append(float(linha.rstrip('\n')))
        return dado



class Salva:

    def __init__(self):
        pass

    def salva_dados(self,sigmoid):
        #Cria obj para pegar data atual
        converte = Converte()
        data=converte.converte_data()

        #Escreve calculo
        arquivo=open("dados "+data+".txt","a")
        arquivo.write(str(sigmoid)+"\n")

class Reseta:

    def __init__(self):
        pass

    def reseta_dados(self):
        converte = Converte()
        data = converte.converte_data()
        arquivo = open("dados " + data + ".txt", "w")
        arquivo.write("")