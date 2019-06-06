README;

	Esta API tem como objetivo calcular uma fun��o de ativa��o de redes 
neurais artificiais chamada 'SIGMOID'. A fun��o de ativa��o sigmoid � 
comumente utilizada por redes neurais com propaga��o positiva (Feedforward) 
que precisam ter como sa�da apenas n�meros positivos, em redes neurais 
multicamadas e em outras redes com sinais cont�nuos. Sua f�rmula �:


			1 / (1 + exp^(-x))


	O Programa tem duas formas de entrada e sa�da de dados, 
ser� poss�vel inserir dados atrav�s do console do pr�prio Python que
aceita um valor apenas para calcular, ou atrav�s de um txt que est� 
nomeado como "DadosEntrada.txt" podendo inserir uma lista de n valores 
que ser�o calulados um por um, sendo assim retornando os valores calculados 
no console e tamb�m pelo txt, que ser� criado ap�s a execu��o do c�digo com 
a data atual que foi gerado os dados. 
	O projeto possui 4 pastas .py, s�o elas; main.py, sigmod.py, 
dados.py e data.py.

	*Abaixo est� a explica��o do que cada .py est� fazendo quando 
� executado o algoritmo, e as propriedade envolvidas para o bom uso da API.

	-main.py: Possui import's que est�o chamando as outras classe do 
algoritmo;
Possui uma classe que chama os m�todos das classes importadas e guarda em 
vari�veis;

os m�todos s�o:
sigmod: que envia os dados para serem calculados.
limpa_txt: limpa os dados do arquivo txt.
entrada_notas: recebe os dados do aquivo txt.
	
	-sigmod.py: Possui um import da biblioteca 'math', para auxiliar no 
c�lculo do m�todo;
Possui um m�todo que calcula a f�rmula de sigmod de Redes Neur�is.

	-dados.py: Possui m�todos para a leitura dos dados pelo arquivo txt,
para salvar os dados e para resetar os dados.
	
	-data.py: Possui um m�todo para adicionar a data atual ao nome do txt 
gerado com os resultados dos dados.

	*Abaixo segue o exeplo de chamada de metodos para a execu��o do c�digo:

recebe um valor apenas
	sig.sigmod(val)

recebe a lista de valores do arquivo DadosEntrada.txt
	sig.entradanotas()

limpa txt
	sig.limpa_txt()



End :)