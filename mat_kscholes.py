'''#Andrew Garcia, 2016'''
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.integrate as integrate


def init(S=80,K=100,r=0.12,T=1,t=0.8,sigma=0.10):
    
    d1=(np.log10(S/K) + (r+0.5*sigma**2)*(T-t) )* ( sigma*np.sqrt(T-t) )**-1
    d2=(np.log10(S/K) + (r-0.5*sigma**2)*(T-t) )* ( sigma*np.sqrt(T-t) )**-1
    
    
    phi1 = integrate.quad(lambda y: (1*(np.sqrt(2*np.pi))**-1)*np.exp(-(y**2)*0.5), -np.inf, d1)[0]
    phi2 = integrate.quad(lambda y: (1*(np.sqrt(2*np.pi))**-1)*np.exp(-(y**2)*0.5), -np.inf, d2)[0]
    
    Vc=S*phi1-K*phi2*np.exp(-r*(T-t))
    
    return Vc
    
def matrix(N=20):
    
    SV=np.linspace(70,130,N)
    tV=np.linspace(0.1,0.9,N)
    volV=np.linspace(0.10,0.20,N)
    
    Mdim=(len(SV),len(tV),len(volV))
    M=np.zeros(Mdim)
                
    for i in range(len(SV)):
        for j in range(len(tV)):
            for k in range(len(volV)):
                M[i][j][k]= init(S=SV[i],K=100,r=0.12,T=1,t=tV[j],sigma=volV[k])
    
    ax = plt.axes(projection='3d')    
    cmap = mpl.cm.cool
    for i2 in range(len(SV)):
        for j2 in range(len(tV)):
            ax.plot(SV,tV,M[i2][j2],color=cmap((i2+2) / float(15)))
            
matrix()