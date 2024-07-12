import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


x = np.array([2, 4, 0, 2,0])
y = np.array([ 5.4, 9.5, 8.1, 6.8, 7.2 ])

def resul_cor():
    corr_martrix = np.corrcoef(x,y)
    corr = corr_martrix[0,1]
    if corr==0:
        print('Não há correlação nenhuma entre x e y', corr)
    elif corr <0.05:
        print('praticamente não há relação entre x e y',corr)
    elif corr<0.20:
        print('relação muito fraca entre x e y', corr)
    elif corr<0.40:
        print('relação fraca entre x e y', corr)
    elif corr<0.70:
        print('relação forte entre x e y' , corr)
    elif corr<0.99:
        print('relação muito forte entre x e y' , corr)
    elif corr==1:
        print('Correlação perfeita positiva entre x e y' , corr)
    elif corr ==-1:
        print('Correlação negativa perfeita entre x e y', corr)

resul_cor()



x=x.reshape(5,1)

modelo = LinearRegression()
modelo.fit(x,y)

c_ang = modelo.coef_
intercp = modelo.intercept_

plt.scatter(x,y)
xreg = np.arange(0,16,1)
plt.plot(xreg, c_ang*xreg + intercp )

plt.show()