import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic-data-6.csv')

titanic.head()


def limpa(coluna,valor):
    titanic[coluna].fillna(valor,inplace=True)
    return titanic.head(6)
    
    
def remove(colunas):
    for i in range(0, len(colunas)):
        titanic.drop([colunas[i]],axis = 1, inplace = True)
    return titanic.head()

colunas = ['Pclass','Fare','Ticket','Cabin','PassengerId','SibSp']
remove(colunas)


titanic_idade = titanic.copy()
titanic_idade.drop(titanic[titanic['Age'].isnull() == True].index ,inplace=True)

titanic['Not Survived'] = titanic['Survived'].map({0:1,1:0})

print('Sobreviventes     :', titanic['Survived'].value_counts()[1])
print('Não Sobreviventes :', titanic['Survived'].value_counts()[0])


titanic['Survived'].value_counts().plot.pie(colors=('tab:red', 'tab:blue'), 
                                       title='Qual a porcentagem dos passageiros sobreviventes?', 
                                       fontsize=13, shadow=True, startangle=90,autopct='%1.1f%%',
                                       labels=('Não sobreviventes','Sobreviventes'),
                                       figsize=(5,5)).set_ylabel('')

plt.figure();
titanic_idade.hist(column='Age', color=('blue'), alpha=0.8, bins=10, figsize=(10,4))
plt.title('Faixa Etária dos Passageiros')
plt.xlabel('Idade')
plt.ylabel('Frequência')


titanic_idade['Crianca_Adulto'] = 0
titanic_idade.loc[titanic_idade[titanic_idade['Age'] < 18].index, 'Crianca_Adulto'] = 'Crianças'
titanic_idade.loc[titanic_idade[titanic_idade['Age'] >= 18].index, 'Crianca_Adulto'] = 'Adulto'
titanic_idade.groupby('Crianca_Adulto')[['Survived']].mean()

titanic_idade.groupby('Crianca_Adulto')['Survived'].mean().plot.barh(title='4.3. Média de Sobrevivência', figsize=(10,2.5),
                                                                color=('tab:green','tab:blue')).set_ylabel(''),plt.xlabel('')

                                                                