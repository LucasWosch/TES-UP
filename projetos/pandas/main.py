import pandas as pd

base = pd.read_csv("forms2semestreup.csv")
print(base.head())

print(base.iloc[:20,:5])
print(base.dtypes)
print(base.shape) # SHAPE -> tamanho da base

print(base)

print(base.iloc[30:40, 3:6])