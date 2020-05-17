import matplotlib.pyplot as plt; plt.rcdefaults();
import numpy as np
import squarify

def funcCriarGraficoDeBarras():

	consoles = ('Nintendo Switch', 'PS4', 'XboxOne', 'Outros', 'Nintendo 3ds')
	indice = np.arange(len(consoles))
	numeroDeVendas = [19278308,10054837,4969579,4251188,1259144]

	plt.bar(indice, numeroDeVendas, color=["red","blue","green","gray","purple"], edgecolor='black')
	plt.xticks(indice, consoles)
	plt.ylabel('Numero de Vendas(em milhoes)')
	plt.title('Numero de vendas de consoles em 2019')

	plt.show()

def funcCriarTreeMap():

	squarify.plot(sizes=[19278308,10054837,4969579,4251188,1259144], 
		label=["Nintendo Switch(48,4%)","PS4(25,2%)","XboxOne(12,5%)","Outros(10,7%)","Nintendo 3ds(3,2%)"],
		color=["red","blue","green","gray","purple"]
		)
	plt.title("Numero de vendas de consoles em 2019",fontsize=18,fontweight="bold")
	plt.axis('off')
	plt.show()

def funcCriarGraficoTemporal():
	

	meses = [1,2,3,4,5,6,7,8,9,10,11,12]
	vendas_ns = np.array([1140, 970, 1160, 780, 890, 890, 880, 960, 1550, 1170, 3800, 5000])
	vendas_ps4 = np.array([1110, 1000, 1250, 820, 1000, 890, 760, 910, 890, 790, 2660, 2120])
	vendas_xboxOne = np.array([280, 290, 330, 190, 220, 250, 180, 180, 230, 210, 1290, 1280])
	vendas_3ds = np.array([180, 140, 160, 100, 110, 75, 74, 79, 49, 51, 108, 118])

	plt.plot(meses, vendas_ns, color="red", label ='Nintendo Switch')
	plt.plot(meses, vendas_ps4, color="blue", label ='PS4')
	plt.plot(meses, vendas_xboxOne, color="green", label ='XboxOne')
	plt.plot(meses, vendas_3ds, color="purple", label ='3ds')

	plt.xlabel('Meses')
	plt.ylabel('Numero de Vendas(vezes 10^3)')
	plt.title('Numero de vendas de consoles em 2019')
	plt.legend()
	plt.show()

funcCriarTreeMap()
funcCriarGraficoDeBarras()
funcCriarGraficoTemporal()





