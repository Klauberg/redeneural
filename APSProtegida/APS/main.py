from sigmoid import *#line:1
from dados import *#line:2
class Sigmoid :#line:4
    def sigmoid (OO0OOOOOO0O000O00 ,OO00OO0000OOO00O0 ):#line:5
        try :#line:7
            float (OO00OO0000OOO00O0 )#line:8
            O0O0O00OOO0OO0OO0 =Calculo ()#line:9
            OOO00OO0OO0O0O0OO =O0O0O00OOO0OO0OO0 .sigmoid (float (OO00OO0000OOO00O0 ))#line:10
            OO0OOO00OO0OO0O00 =Salva ()#line:11
            OO0OOO00OO0OO0O00 .salva_dados (OOO00OO0OO0O0O0OO )#line:12
            print (OOO00OO0OO0O0O0OO )#line:13
        except :#line:14
            print ("Valor Incorreto")#line:15
    def limpa_txt (OOO0O00OOO00OO0OO ):#line:17
        O0OO0OOO0OO0O000O =Reseta ()#line:18
        O0OO0OOO0OO0O000O .reseta_dados ()#line:19
    def entrada_notas (O00O000OO0000O0OO ):#line:21
        O00O0000O00O0OOO0 =Leitura ()#line:22
        O000000O0O0OO0OOO =(O00O0000O00O0OOO0 .ler_dados ())#line:23
        for OO0OOO0OO0000O000 in O000000O0O0OO0OOO :#line:24
            O00O000OO0000O0OO .sigmoid (OO0OOO0OO0000O000 )#line:25
sig =Sigmoid ()#line:29
sig .entrada_notas ()#line:30
