# importing required modules
import PyPDF2
import tabula
import pandas as pd

def CorrigirLinha(context):
	context = context.replace('Produto,Investido em,Vencimento,Taxa,Valor Investido,Valor Bruto,Valor Líquido,Indexador','Produto\tInvestido em\tVencimento\tTaxa\tValor Investido\tValor Bruto\tValor Líquido\tIndexador\tGanho\t%\tTempo (MÊs)\t% Mensal')
	context = context.replace("I,", "I\t")
	context = context.replace("E,", "E\t")
	context = context.replace("/2022,", "/2022\t")
	context = context.replace(',"', '\t"')
	context = context.replace('",', '"\t')
	context = context.replace("R$ ", "")

	return context


tabula.convert_into("PosicaoInvestimento_2023-04-01.pdf", "output.csv", output_format="csv", pages='all')


f = open("output.csv", "r")
linhas = f.readlines()

linha = 1


for line in linhas:
	if 'Total' in line:
		break

	line = line.replace('\n', '')

	if linha > 1:
		line = line + f'\t=G{linha}-E{linha}'
		line = line + f'\t=ROUND((G{linha}/E{linha})*100-100;2)'
		line = line + f'\t=ROUND(DATEDIF(B{linha};TODAY();"D") / 30;0)'
		line = line + f'\t=ROUND(J{linha}/IF(K{linha} = 0;1;K{linha});2)'

	
	print(CorrigirLinha(line))
	linha = linha + 1

f.close()



#fw = open("DadosDoPDF.csv", "w")
#fw.write(context)
#fw.close()





