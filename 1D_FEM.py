import Gaussian_integral
import numpy as np
import math

def fun_f(x):
    return math.exp(x)

def fun_g(x):
    return -math.exp(x)*(math.cos(x)-2*math.sin(x)-x*math.cos(x)-x*math.sin(x))

N=8
a,b=0.0,1.0
h=(b-a)/N
base_der=np.eye(N+1,N,dtype=float)*(-1/h)+np.eye(N+1,N,k=-1,dtype=float)*1/h
P=np.linspace(a,b,N+1)
temp=np.linspace(0,N,N+1,dtype=int)
T=np.vstack([temp[:-1],temp[1:]])

A=np.zeros((N+1,N+1))

for n in range(N):
    for i in range(N+1):
        for j in range(N+1):
            A[i][j]=A[i][j]+base_der[j][n]*base_der[i][n]*Gaussian_integral.Gau_3(fun_f,P[T[0][n]],P[T[1][n]])
# print(A)

b=np.zeros((N+1,1))
for n in range(N):
    for i in range(N+1):
        b[i]=Gaussian_integral.Gau_3(fun_g,P[T[0][n]],P[T[1][n]])
# print(b)

A[0,:]=0
A[0][0]=1
A[-1,:]=0
A[-1][-1]=1
b[0]=0
b[-1]=math.cos(1)

anx = np.linalg.solve(A,b)
print(anx)




