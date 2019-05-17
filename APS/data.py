import datetime
class Converte:

    def __init__(self):
        pass
    #Separa a data para melhor modificações
    def converte_data(self):
        agora = (datetime.datetime.now())
        ano = str(agora)[0:4]
        mes = str(agora)[5:7]
        dia = str(agora)[8:10]
        data=ano+mes+dia
        return data


