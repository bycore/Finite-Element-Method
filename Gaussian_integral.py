import math

GauThree={-0.7745966692:0.555555556,0.7745966692:0.555555556,0:0.8888888889}


def funtest1(x):
    return x
def funtest2(x):
    return x

def Gau_3(fun,a=-1.0,b=1.0):
    GauSum=0.0
    sng=1 if a<=b else -1
    for key,value in GauThree.items():
        GauSum+=fun(((b-a)*key+a+b)/2)*value
    GauSum=GauSum*(b-a)/2
    return GauSum*sng


if __name__ == '__main__':
    Gau_3()
    