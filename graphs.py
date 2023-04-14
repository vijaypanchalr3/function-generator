import matplotlib.pyplot as plt
import numpy as np




def low():
    t = 1
    w = np.arange(0,t,.01)
    w0 = t/100
    A = np.zeros(len(w))
    for i in range(len(A)):
        A[i]=1/(1+np.exp((i-75/2)/5))

    plt.plot(w,A, label="low pass filter", color="#006169")
    plt.xlabel("$w/w_o$")
    plt.ylabel("$V_o/V_i$")
    plt.legend()
    plt.savefig('imgs/low.png')
def high():
    t = 1
    w = np.arange(0,t,.01)
    w0 = t/100
    A = np.zeros(len(w))
    for i in range(len(A)):
        A[i]=1/(1+np.exp(-(i-75/2)/5))

    plt.plot(w,A, label="high pass filter", color="#F76D03")
    plt.xlabel("$w/w_o$")
    plt.ylabel("$V_o/V_i$")
    plt.legend()
    plt.savefig('imgs/high.png')
def highlow():
    t = 1
    w = np.arange(0,t,.01)
    w0 = t/100
    A1 = np.zeros(len(w))
    A2 = np.zeros(len(w))
    for i in range(len(w)):
        A1[i]=1/(1+np.exp(-(i-75/2)/5))
        A2[i]=1/(1+np.exp((i-75/2)/5))
        
    fig, ax = plt.subplots()
    ax.plot(w,A1, label="high pass filter" ,color="#F76D03")
    ax.plot(w,A2, label="low pass filter", color="#006169")
    
    plt.xlabel("$w/w_o$")
    plt.ylabel("$V_o/V_i$")
    plt.legend()
    plt.savefig('imgs/highlow.png')
    plt.show()
def fourierana1():
    t = 1/40
    w = np.linspace(0,t,200)
    A = np.zeros(len(w))
    for i in range(len(A)):
        A[i]=(10*np.sin(50*i))+(0.004*np.sin(100*i))+(0.004*np.cos(100*i))+(0.02*np.cos(1000*i))+(0.002*np.cos(2000*i))+(0.2*np.cos(103*i))+(0.2*np.cos(10000*i))

    plt.plot(w,A)
    # plt.xlabel("$w/w_o$")
    # plt.ylabel("$V_o/V_i$")
    # plt.legend()
    # plt.savefig('imgs/high.png')
    plt.show()
fourierana1()
