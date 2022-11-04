import pandas as pd
import numpy as np

data = {'NOMBRE':['María','José','David','Iván'],
        'CARRERA':['Auditoría','Informática','Derecho','Religión'],
        'CORREO':['mari02@gmail.com','jos353@gmail.com','david11@hotmail.com','ivog22@gmail.com']
        }
estudiantes = pd.DataFrame(data)
# print(estudiantes)
df = pd.DataFrame([['Saúl',17],['Ana',26],['Roger',34]],
                  columns=['NOMBRE','EDAD'])
# print(df)
# print('-.-.-.-.-.-.-.-.-.-.-.-\n')

# df2 = pd.DataFrame(np.random.randn(4,3), columns=['a','b','c'])
# print(df2)
df3 = pd.read_csv('ModalidadVirtual.csv')
#print(df3)
#print(df3.info()) #dtype, non-null
#print(df.describe()) #media, desv, cuart
print(df3.iloc[10:20])

# git config -h #variables de git BASH para trabajar
