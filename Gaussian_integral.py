import math
import sympy


def funtest1(x):
    return x
def funtest2(x,y):
    return x*x+y


def Gau_3(fun,a=-1.0,b=1.0):
    GauThree={-0.7745966692:0.555555556,0.7745966692:0.555555556,0:0.8888888889}
    GauSum=0.0
    sng=1 if a<=b else -1
    for key,value in GauThree.items():
        GauSum+=fun(((b-a)*key+a+b)/2)*value
    GauSum=GauSum*(b-a)/2
    return GauSum*sng

def Gau_sym_3(fun,a=-1.0,b=1.0):
    GauThree={-0.7745966692:0.555555556,0.7745966692:0.555555556,0:0.8888888889}
    GauSum=0.0
    sng=1 if a<=b else -1
    for key,value in GauThree.items():
        GauSum+=fun.evalf(subs={x:(((b-a)*key+a+b)/2)})*value
    GauSum=GauSum*(b-a)/2
    return GauSum*sng

def Gau_2D_9(fun):
    gpt=math.sqrt(3.0/5)
    A=[25.0/81,25.0/81,25.0/81,25.0/81,40.0/81,40.0/81,40.0/81,40.0/81,64.0/81]
    x=[-gpt,gpt,gpt,-gpt,0,gpt,0,-gpt,0]
    y=[-gpt,-gpt,gpt,gpt,-gpt,0,gpt,0,0]
    GauSum=0.0
    for i in range(9):
        GauSum+=fun(x[i],y[i])*A[i]
    return GauSum

x=sympy.symbols("x")

if __name__== '__main__':
    init=Gau_2D_9(funtest2)
    print(init)