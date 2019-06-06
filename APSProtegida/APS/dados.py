from data import Converte #line:1
class Leitura :#line:4
    def __init__ (OO0O00000OOO0O0OO ):#line:6
        pass #line:7
    def ler_dados (OOO000O00O0OOOO0O ):#line:9
        O0O0O0OOO00O00O00 =open ("DadosEntrada.txt","r")#line:10
        O0OOO0O000O0OO000 =[]#line:11
        for OO00OOOO0OO000O00 in O0O0O0OOO00O00O00 :#line:12
            O0OOO0O000O0OO000 .append (float (OO00OOOO0OO000O00 .rstrip ('\n')))#line:13
        return O0OOO0O000O0OO000 #line:14
class Salva :#line:18
    def __init__ (O0O0OOOOOO0OO000O ):#line:20
        pass #line:21
    def salva_dados (OOOO000O0O0000O00 ,OOOO0OOO000O0OO00 ):#line:23
        O00000OOOOOOO0OOO =Converte ()#line:25
        O0000O0O0O000O00O =O00000OOOOOOO0OOO .converte_data ()#line:26
        O000O00OO0O0000O0 =open ("dados "+O0000O0O0O000O00O +".txt","a")#line:29
        O000O00OO0O0000O0 .write (str (OOOO0OOO000O0OO00 )+"\n")#line:30
class Reseta :#line:32
    def __init__ (O0OO00OOO000O0OOO ):#line:34
        pass #line:35
    def reseta_dados (OO0O0OO0O00OO0O0O ):#line:37
        OO00O0O0OO000000O =Converte ()#line:38
        O0OO0000O0OO0OOO0 =OO00O0O0OO000000O .converte_data ()#line:39
        O0O0O00O0OOOOO0O0 =open ("dados "+O0OO0000O0OO0OOO0 +".txt","w")#line:40
        O0O0O00O0OOOOO0O0 .write ("")