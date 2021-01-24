import math

GauThree={0.7745966692:0.555555556,0:0.8888888889}
GauFive={0.9061798459:0.2369268851,0.5384693101:0.4786286705,0:0.5688888889}


def funtest(x):
    if x>=-1.0 and x<=1.0:
        return x*x
    else:
        raise ValueError("unknow")
def fun_diff(fun,x,h=1.0e-5):
    try :
        return (fun(x+h)-fun(x))/h
    except:
        return (fun(x)-fun(x-h))/h
def Gau_3(fun):
    GauSum=0.0
    for key,value in GauThree.items():
        if key>0:
            GauSum+=fun_diff(fun,key)*value
            GauSum+=fun_diff(fun,-key)*value
        else:
            GauSum+=fun_diff(fun,key)*value
    return GauSum
def Gau_5(fun):
    GauSum=0.0
    for key,value in GauFive.items():
        if key!=0 :
            GauSum+=fun(key)*value
            GauSum+=fun(-key)*value
        else:
            GauSum+=fun(key)*value
    return GauSum

if __name__ == '__main__':
    print(Gau_3(funtest))
    print(Gau_5(funtest))