
#resposta 3

import pandas as pd
import missingno  as msno
%matplotlib inline
data = pd.read_csv("goodreads_books.csv")

#avaliando base - 10 linhas x 31 colunas
# print(data.head(10)) 

# print (data.describe()) #52199 rows x 31 columns

# print(data.dtypes) # Verificando tipo de todas as colunas

print (data.isnull().sum())
# df_titulo = data[(data["original_title"].isnull())]
# df_titulo = df_titulo[['title','original_title']]

msno.matrix(data) 







