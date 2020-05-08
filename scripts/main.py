#%% Import 

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

#%% Bounds

def bV(c1s,c2s,f2):
    return np.array([1-f2,f2])@np.array([c1s,c2s])

def bR(c1s,c2s,f2):
    return 1/(np.array([1-f2,f2])@np.array([1/c1s,1/c2s]))

#%% Plot

def plot(c1s,c2s,orientation='v'):
    f2s = np.linspace(0,1,20)
    
    p = np.array([[f(c1s,c2s,f2) for f2 in f2s] for f in [bV,bR]])
    
    if orientation=='h':
        fig,ax = plt.subplots(1,2,figsize=(10,4))
    else:
        fig,ax = plt.subplots(2,1,figsize=(5,8))
    
    y_labels = ['$c^*_1 = 3K^*$','$c^*_2 = 2G^*$']
    for i in [0,1]:
        ax[i].plot(f2s,p[0,:,i],label='Voigt')
        ax[i].plot(f2s,p[1,:,i],label='Reuss')
        ax[i].set_ylim([0,10])
        ax[i].set_xlabel('$f^{(2)}$')
        ax[i].set_ylabel(y_labels[i])
        ax[i].legend()
    plt.show()
    
#%% Static plot

c1s = np.array([1,10])
c2s = np.array([8,3])

print('Static plot')
plot(c1s,c2s)

#%% Interactive plot

# Variables
c11 = widgets.IntSlider(1,min=1,max=10,description='$c^{(1)}_1 = 3K^{(1)}$')
c12 = widgets.IntSlider(1,min=1,max=10,description='$c^{(1)}_2 = 2G^{(1)}$')
c21 = widgets.IntSlider(10,min=1,max=10,description='$c^{(2)}_1 = 3K^{(2)}$')
c22 = widgets.IntSlider(10,min=1,max=10,description='$c^{(2)}_2 = 2G^{(2)}$')

# Function
def plot2(c11,c12,c21,c22):
    plot(np.array([c11,c12]),np.array([c21,c22]))

# Bottom
bottom_manual = widgets.interactive(
    plot2
    ,{'manual':True}
    ,c11=c11,c12=c12,c21=c21,c22=c22
)
bottom_manual.children[-2].description = 'Run/Update'

def start(device='smartphone'):
    print('Starting interactive plots')
    if device=='smartphone':
        head = widgets.VBox([widgets.Label('Material 1'),c11,c12,widgets.Label('Material 2'),c21,c22])
        display(head)
    else: 
        head1 = widgets.HBox([widgets.Label('Material 1'),c11,c12])
        head2 = widgets.HBox([widgets.Label('Material 2'),c21,c22])
        display(head1)
        display(head2)
    display(bottom_manual.children[-2])
    display(bottom_manual.children[-1])