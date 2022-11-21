import pandas
import seaborn
data = pandas.read_csv("new.csv", sep="\t")
seaborn.relplot(x='Доходность B, %', y='Доходность A, %', kind='scatter', data=data)
seaborn.relplot(x='Доходность B, %', y='Доходность C, %', kind='scatter', data=data)
seaborn.relplot(x='Доходность C, %', y='Доходность A, %', kind='scatter', data=data)