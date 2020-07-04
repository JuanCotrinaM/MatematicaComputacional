##Instalar sympy y matplotlib
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

   

def lagrange(pto,n):

    t = symbols('t')

    aux = [1,1,1,1]

    for i in range(n):
        for k in range(n):
            if(i != k):
                aux[i] = aux[i]*(t-k)/(i-k)
    
    alfa = np.array(aux)
    
    polinomio = np.zeros((2,1))
    
    
    polinomio =pto.dot(alfa)

    return polinomio

def ptos(valor,pto):
    resultado = []
    
    for i in valor:
        t = symbols('t')
        resultado.append(pto.subs(t,i))
    
    return resultado


def main():
    pto_control = np.array([[-3.0,0.0],[-1.0,4.0],[2.0,3.0],[4.0,1.0]])
    n,m = pto_control.shape

    polinomio =lagrange(pto_control.transpose(),n)

    t1 = np.arange(0.0, 3.0, 0.1)
    x = ptos(t1,polinomio[0])
    y = ptos(t1,polinomio[1])


    plt.plot(x,y, color='lightblue', linewidth=3)
    plt.scatter(pto_control[0][0],pto_control[0][1], label='P0', s=10)
    plt.scatter(pto_control[1][0],pto_control[1][1], label='P1', s=10)
    plt.scatter(pto_control[2][0],pto_control[2][1], label='P2', s=10)
    plt.scatter(pto_control[2][0],pto_control[3][1], label='P3', s=10)
    plt.show() 

main()
   
