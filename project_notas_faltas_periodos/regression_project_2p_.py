import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


n = np.array([7.6 , 7.7 , 7.7 , 7.5 , 7.7])
f = np.array([0 , 6 , 6 , 8 , 24])

#embora faltar mais de 16 leva a reprovação, o professor fez o acordo no início do período que não reprovaria
#ningúem por falta, o número de faltas que consta o sigaa é 16, mas na realidade foram 24 faltas

def resul_cor():
    corr_martrix = np.corrcoef(f,n)
    corr = corr_martrix[0,1]
    if corr==0:
        print('Não há correlação nenhuma entre notas e faltas')
    elif corr <0.05:
        print('praticamente não há relação entre notas e faltas',corr)
    elif corr<0.20:
        print('relação muito fraca entre notas e faltas', corr)
    elif corr<0.40:
        print('relação fraca entre notas e faltas', corr)
    elif corr<0.70:
        print('relação forte entre notas e faltas' , corr)
    elif corr<0.99:
        print('relação muito forte entre notas e faltas' , corr)
    elif corr==1:
        print('Correlação perfeita positiva entre notas e faltas' , corr)
    elif corr ==-1:
        print('Correlação negativa perfeita entre notas e faltas', corr)

resul_cor()



f=f.reshape(5,1)

modelo = LinearRegression()
modelo.fit(f,n)

c_ang = modelo.coef_
intercp = modelo.intercept_

plt.scatter(f,n)
xreg = np.arange(0,24,1)
plt.plot(xreg, c_ang*xreg + intercp )

plt.show()
