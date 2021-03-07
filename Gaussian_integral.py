import math
import sympy


def funtest1(x):
    return x
def funtest2(x,y):
    return x*x+y
def funtest3(x,y,z):
    return x*x+y*y+z*z


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

def Gau_2D_9_standard(fun):
    gpt=math.sqrt(3.0/5)
    A=[25.0/81,25.0/81,25.0/81,25.0/81,40.0/81,40.0/81,40.0/81,40.0/81,64.0/81]
    x=[-gpt,gpt,gpt,-gpt,0,gpt,0,-gpt,0]
    y=[-gpt,-gpt,gpt,gpt,-gpt,0,gpt,0,0]
    GauSum=0.0
    for i in range(9):
        GauSum+=fun(x[i],y[i])*A[i]
    return GauSum

def Gau_2D_9(fun,a=-1.0,b=1.0,c=-1.0,d=1.0):
    gpt=math.sqrt(3.0/5)
    A=[25.0/81,25.0/81,25.0/81,25.0/81,40.0/81,40.0/81,40.0/81,40.0/81,64.0/81]
    x=[-gpt,gpt,gpt,-gpt,0,gpt,0,-gpt,0]
    y=[-gpt,-gpt,gpt,gpt,-gpt,0,gpt,0,0]
    GauSum=0.0
    for i in range(9):
        GauSum+=fun((b+a+(b-a)*x[i])/2,(d+c+(d-c)*y[i])/2)*A[i]*(b-a)*(d-c)/4
    return GauSum

def Gau_3D_14_standard(fun):
    B6=320.0/361
    C8=121.0/361
    b=math.sqrt(19.0/30)
    c=math.sqrt(19.0/33)
    A=[B6,B6,B6,B6,B6,B6,C8,C8,C8,C8,C8,C8,C8,C8]
    x=[-b,b,0,0,0,0,-c,c,c,-c,-c,c,-c,c]
    y=[0,0,-b,b,0,0,-c,c,-c,c,-c,c,c,-c]
    z=[0,0,0,0,-b,b,-c,c,-c,-c,c,-c,c,c]
    GauSum=0.0
    for i in range(14):
        GauSum+=fun(x[i],y[i],z[i])*A[i]
    return GauSum

def Gau_3D_14(fun,m=-1.0,n=1.0,s=-1.0,t=1.0,u=-1.0,v=1.0):
    B6=320.0/361
    C8=121.0/361
    b=math.sqrt(19.0/30)
    c=math.sqrt(19.0/33)
    A=[B6,B6,B6,B6,B6,B6,C8,C8,C8,C8,C8,C8,C8,C8]
    x=[-b,b,0,0,0,0,-c,c,c,-c,-c,c,-c,c]
    y=[0,0,-b,b,0,0,-c,c,-c,c,-c,c,c,-c]
    z=[0,0,0,0,-b,b,-c,c,-c,-c,c,-c,c,c]
    GauSum=0.0
    for i in range(14):
        GauSum+=fun((n+m+(n-m)*x[i])/2,(s+t+(t-s)*y[i])/2,(u+v+(v-u)*z[i])/2)*A[i]*(n-m)*(t-s)*(v-u)/8
    return GauSum

x=sympy.symbols("x")

if __name__== '__main__':
    x=sympy.symbols("x")
    y=sympy.symbols("y")
    z=sympy.symbols("z")
    init=float(sympy.integrate(x*x+y*y+z*z,(x,1,2),(y,1,2),(z,1,2)))
    init2=Gau_3D_14(funtest3,1,2,1,2,1,2)
    print(init-init2)