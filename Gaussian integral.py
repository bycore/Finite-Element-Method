import math
def fun(x):
    return x*x
 
GauThree={0.7745966692:0.555555556,0:0.8888888889}
GauFive={0.9061798459:0.2369268851,0.5384693101:0.4786286705,0:0.5688888889}
GauSum=0.0
for key,value in GauThree.items():
    if(key>0):
        GauSum+=fun(key)*value
        GauSum+=fun(-key)*value
    else:
        GauSum+=fun(key)*value
print ("GauThree Method:",GauSum)
GauSum=0.0
for key,value in GauFive.items():
    if(key>0):
        GauSum+=fun(key)*value
        GauSum+=fun(-key)*value
    else:
        GauSum+=fun(key)*value
print ("GauFive Method:",GauSum)