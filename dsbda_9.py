import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())
titanic = titanic.dropna(subset=['age'])
plt.figure(figsize=(10, 6))

sns.boxplot(
    x='sex',       
    y='age',        
    hue='survived',
    data=titanic
)

plt.title('Age Distribution by Gender and Survival (Titanic Dataset)')
plt.xlabel('Gender')
plt.ylabel('Age')

plt.legend(title='Survived', labels=['No', 'Yes'])

plt.show()