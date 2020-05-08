#%% Import 

import numpy as np
import matplotlib.pyplot as plt
import pywidgets.widgets as widgets

#%% Bounds

def bV(c1s,c2s,f2):
    return np.array([1-f2,f2])@np.array([c1s,c2s])

def bR(c1s,c2s,f2):
    return 1/(np.array([1-f2,f2])@np.array([1/c1s,1/c2s]))

#%% Plot

def plot(c1s,c2s):
    f2s = np.linspace(0,1,20)
    
    p = np.array([[f(c1s,c2s,f2) for f2 in f2s] for f in [bV,bR]])
    
    fig,ax = plt.subplots(1,2,figsize=(10,4))
    
    y_labels = ['$c^*_1 = 3K^*$','$c^*_2 = 2G^*$']
    for i in [0,1]:
        ax[i].plot(f2s,p[0,:,i],label='Voigt')
        ax[i].plot(f2s,p[1,:,i],label='Reuss')
        ax[i].set_ylim([0,10])
        ax[i].set_xlabel('$f^{(2)}$')
        ax[i].legend()
    plt.show()
    
#%% Static plot

c1s = np.array([1,10])
c2s = np.array([8,3])

plot(c1s,c2s)