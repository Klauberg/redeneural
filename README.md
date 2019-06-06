README;

	Esta API tem como objetivo calcular uma função de ativação de redes 
neurais artificiais chamada 'SIGMOID'. A função de ativação sigmoid é 
comumente utilizada por redes neurais com propagação positiva (Feedforward) 
que precisam ter como saída apenas números positivos, em redes neurais 
multicamadas e em outras redes com sinais contínuos. Sua fórmula é:


			1 / (1 + exp^(-x))


	O Programa tem duas formas de entrada e saída de dados, 
será possível inserir dados através do console do próprio Python que
aceita um valor apenas para calcular, ou através de um txt que está 
nomeado como "DadosEntrada.txt" podendo inserir uma lista de n valores 
que serão calulados um por um, sendo assim retornando os valores calculados 
no console e também pelo txt, que será criado após a execução do código com 
a data atual que foi gerado os dados. 
	O projeto possui 4 pastas .py, são elas; main.py, sigmod.py, 
dados.py e data.py.

	*Abaixo está a explicação do que cada .py está fazendo quando 
é executado o algoritmo, e as propriedade envolvidas para o bom uso da API.

	-main.py: Possui import's que estão chamando as outras classe do 
algoritmo;
Possui uma classe que chama os métodos das classes importadas e guarda em 
variáveis;

os métodos são:
sigmod: que envia os dados para serem calculados.
limpa_txt: limpa os dados do arquivo txt.
entrada_notas: recebe os dados do aquivo txt.
	
	-sigmod.py: Possui um import da biblioteca 'math', para auxiliar no 
cálculo do método;
Possui um método que calcula a fórmula de sigmod de Redes Neuráis.

	-dados.py: Possui métodos para a leitura dos dados pelo arquivo txt,
para salvar os dados e para resetar os dados.
	
	-data.py: Possui um método para adicionar a data atual ao nome do txt 
gerado com os resultados dos dados.

	*Abaixo segue o exeplo de chamada de metodos para a execução do código:

recebe um valor apenas
	sig.sigmod(val)

recebe a lista de valores do arquivo DadosEntrada.txt
	sig.entradanotas()

limpa txt
	sig.limpa_txt()



End :)