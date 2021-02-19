import Gaussian_integral
import numpy as np
import sympy
import math

def hat_function(i,j,x,Pb,Tb):# 第i个基函数，第j个有限元
    h=Pb[1]-Pb[0]
    if i==j:
        return 1.0/h*(Pb[Tb[1][j]]-x)
    elif i==j+1:
        return 1.0/h*(x-Pb[Tb[0][j]])
    else :
        return 0*x

if __name__== '__main__':
    N=4
    a,b=1,5
    x=sympy.symbols("x")
    P=np.linspace(a,b,N+1)
    temp=np.linspace(0,N,N+1,dtype=int)
    T=np.vstack([temp[:-1],temp[1:]])

    ans=Gaussian_integral.Gau_sym_3(hat_function(0,0,x,P,T),1,2)
    print(ans)
