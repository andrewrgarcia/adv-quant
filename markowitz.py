'''#Andrew Garcia, 2015'''
import numpy as np

def EV(X1=0.25,X2=0.3):

    'Probability beliefs (static)'
    #Covariances
    s11=2.6;     s12=5.5;     s13=7.2
    s21=3.4;     s22=6.5;     s23=7.0
    s31=7.5;     s32=2.3;     s33=3.2
    
    #s11=12.6;     s12=15.5;     s13=17.2
    #s21=5.4;     s22=16.5;     s23=17.0
    #s31=6.5;     s32=12.3;     s33=13.2
    sigma=np.array([[s11,s12,s13],[s21,s22,s23],[s31,s32,s33]])
    
    #Expected Values
    m1=10
    m2=13
    m3=20
    mu=np.array([m1,m2,m3])
    
    #Percentages of Assets Invested:
    X1==X1
    X2==X2
    X3=1-X1-X2
    X=([X1,X2,X3])
    
    V=0
    #for i in range(3):
    #    for j in range(3):
    #        V=+X[i]*X[j]*sigma[i,j]
    for i in range(3):
        V+=X[0]*X[i]*sigma[0,i]
        V+=X[1]*X[i]*sigma[1,i]
        V+=X[2]*X[i]*sigma[2,i]
        
    E=0
    for i in range(3):
        E=+X[i]*mu[i]
        
    return V,E
