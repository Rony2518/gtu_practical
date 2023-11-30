import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data = {'Name':['ronak','rony','da'],
        'marks':[10,30,40]}
df = pd.DataFrame(data)

Name = df['Name']
Marks = df['marks']

plt.bar(Name,Marks,label=Name,color=['red','green','yellow'],width=0.5)
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend()
plt.show()