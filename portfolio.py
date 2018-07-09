'''#Andrew Garcia, 2015'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import markowitz as mvitz

def effV():
    cmap = mpl.cm.cool
    cmaph = mpl.cm.hot

    'INCREASING GRADIENT: CYAN TO PURPLE'
    for i in range(100):
        '''x1 changes FIRST from 0-i; x2 fixed at i(shows x1 values before a x2 limit);
        INCREASING X2 BOTTOM TO TOP, THEN TOP TO BOTTOM AFTER SADDLE POINT'''
        x1=np.linspace(0,i*0.01)
        Vx=mvitz.EV(X1=x1,X2=i*0.01)[0]
        #plt.plot(x1,Vx,'o')
        #plt.plot(x1,Vx,'-')
        plt.plot(x1,Vx,'o',color=cmap(i*5))
        plt.plot(x1,Vx,'-',color='gray')
    #
    for i in range(100):
        '''x1 changes FIRST from i-1; x2 fixed at i (shows x1 values beyond a x2 limit)
        INCREASING X2 BOTTOM TO TOP, THEN TOP TO BOTTOM AFTER SADDLE POINT'''
        x1=np.linspace(i*0.01,1)
        Vx=mvitz.EV(X1=x1,X2=i*0.01)[0]
        plt.plot(x1,Vx,color=cmap(i*5))


    #plt.axhline(y=0,color='red')
    plt.ylim([0, 8])
    plt.xlabel(r'$X_1$($X_2$)',size=13)
    plt.ylabel(r'Variance',size=13)
    #plt.title('Portfolio Selection: Variance("Risk") \n Andrew R Garcia, 2015')
    plt.title('Andrew R Garcia, 2015',size=13)
    plt.show()

def effE():
    #with plt.xkcd():
    cmap = mpl.cm.cool
    #cmap = mpl.cm.hot

    'INCREASING GRADIENT: CYAN TO PURPLE'
    for i in range(100):
        '''x1 changes FIRST from 0-i; x2 fixed at i(shows x1 values before a x2 limit);
        INCREASING X2 BOTTOM TO TOP, THEN TOP TO BOTTOM AFTER SADDLE POINT'''
        x1=np.linspace(0,i*0.01)
        Ex=mvitz.EV(X1=x1,X2=i*0.01)[1]
        #plt.plot(x1,Vx,'o')
        #plt.plot(x1,Vx,'-')
        plt.plot(x1,Ex,'o',color=cmap(i*5))
        plt.plot(x1,Ex,'-',color='gray')
    #
    for i in range(100):
        '''x1 changes FIRST from i-1; x2 fixed at i (shows x1 values beyond a x2 limit)
        INCREASING X2 BOTTOM TO TOP, THEN TOP TO BOTTOM AFTER SADDLE POINT'''
        x1=np.linspace(i*0.01,1)
        Ex=mvitz.EV(X1=x1,X2=i*0.01)[1]
        plt.plot(x1,Ex,color=cmap(i*5))


    #plt.axhline(y=0,color='red')
    plt.ylim([0, 20])
    plt.xlabel('$X_1$, $X_2$',size=13)
    plt.ylabel(r'Expected Return',size=13)
    #plt.title('Portfolio Selection: Expected Return \n Andrew R Garcia, 2015',size=13)
    plt.title('Andrew R Garcia, 2015',size=13)
    plt.show()

def retrisk():
    #with plt.xkcd():
    cmap = mpl.cm.cool
    cmaph = mpl.cm.hot

    'INCREASING GRADIENT: CYAN TO PURPLE'
    for i in range(100):
        '''x1 changes FIRST from 0-i; x2 fixed at i(shows x1 values before a x2 limit);
        INCREASING X2 BOTTOM TO TOP, THEN TOP TO BOTTOM AFTER SADDLE POINT'''
        x1=np.linspace(0,i*0.01)
        Vx=mvitz.EV(X1=x1,X2=i*0.01)[0]
        Ex=mvitz.EV(X1=x1,X2=i*0.01)[1]
        #plt.plot(x1,Vx,'o')
        #plt.plot(x1,Vx,'-')
        plt.plot(Vx,Ex,'o',color=cmap(i*5))
        plt.plot(Vx,Ex,'-',color='gray')
    #
    for i in range(100):
        '''x1 changes FIRST from i-1; x2 fixed at i (shows x1 values beyond a x2 limit)
        INCREASING X2 BOTTOM TO TOP, THEN TOP TO BOTTOM AFTER SADDLE POINT'''
        x1=np.linspace(i*0.01,1)
        Vx=mvitz.EV(X1=x1,X2=i*0.01)[0]
        Ex=mvitz.EV(X1=x1,X2=i*0.01)[1]
        plt.plot(Vx,Ex,color=cmap(i*5))


    #plt.axhline(y=0,color='red')
    plt.xlabel(r'Risk',size=13)
    plt.ylabel(r'Return',size=13)
    #plt.title(' Return v Risk Portfolio Surface \n Andrew R Garcia, 2015')
    plt.title('Andrew R Garcia, 2015',size=13)
    plt.show()

retrisk()

def plotv(v=15):
    X2=np.linspace(4,100)
    #X1r1=-0.48876404494382*X2 - 0.00561797752808989*np.sqrt(8993.0*X2**2 - 4118.0*X2 - 3560.0*v + 18281.0) + 0.466292134831461
    X1r2=-0.48876404494382*X2 + 0.00561797752808989*np.sqrt(8993.0*X2**2 - 4118.0*X2 - 3560.0*v + 18281.0) + 0.466292134831461

    #plt.plot(X2,X1r1)
    plt.plot(X2,X1r2)

    return X2,X1r2

def multplt():
    for i in range(25):
        X2,X1=plotv(v=i)
        plt.plot(X2,X1)

#multplt()
