##Uma série em pandas funciona como um dicionário contendo índice para cada valor, no entando são passíveis de modificação
import pandas as pd
lista = ['1', '2', '5', '6']
lista_S = pd.Series(lista)
print(lista_S)