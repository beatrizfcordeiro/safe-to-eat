import pandas as pd



## carregar dados
df = pd.read_csv("data/raw/restaurantes_curitiba_rmc.csv")

## mostrar nomes das colunas
print(df.columns)

## remover espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

## visualizar antes
print("ANTES DA LIMPEZA:")
print(df.head())

## remover espaços extras
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

## padronizar texto
df["seguro_celiaco"] = df["seguro_celiaco"].str.capitalize()

## preencher valores vazios
df["nivel_seguranca"] = df["nivel_seguranca"].fillna("Desconhecido")
df["observacoes"] = df["observacoes"].fillna("Sem informação")

## visualizar depois
print("\nDEPOIS DA LIMPEZA:")
print(df.head())


