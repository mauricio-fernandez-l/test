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

#%% Eshelby's solution

def aSIP(cIs,cMs):
    a1 = (cMs[0]+2*cMs[1])/(cIs[0]+2*cMs[1])
    a2 = (5*cMs[1]*(cMs[0]+2*cMs[1]))/(
        2*cIs[1]*(cMs[0]+3*cMs[1])+cMs[1]*(3*cMs[0]+4*cMs[1])
        )
    return np.array([a1,a2])

#%% Approximations

def app(c1s,c2s,f2,a):
    return c1s + f2*(c2s-c1s)*a

def appDD1(c1s,c2s,f2):
    a = aSIP(cIs=c2s,cMs=c1s)
    return app(c1s,c2s,f2,a)

def appDD2(c1s,c2s,f2):
    aS = aSIP(cIs=c1s,cMs=c2s)
    a = (np.array([1,1])-(1-f2)*aS)
    return app(c1s,c2s,1,a)

#%% Plot

def plot(c1s,c2s,orientation='h'):
    f2s = np.linspace(0,1,20)
    
    p = np.array([
        [f(c1s,c2s,f2) for f2 in f2s] 
        for f in [bV,bR,appDD1,appDD2]
        ])
    
    if orientation=='h':
        fig,ax = plt.subplots(1,2,figsize=(10,4))
    else:
        fig,ax = plt.subplots(2,1,figsize=(5,8))
    
    y_labels = ['$c^*_1 = 3K^*$','$c^*_2 = 2G^*$']
    for i in [0,1]:
        ax[i].plot(f2s,p[0,:,i],label='Voigt')
        ax[i].plot(f2s,p[1,:,i],label='Reuss')
        ax[i].plot(f2s,p[2,:,i],label='DD1')
        ax[i].plot(f2s,p[3,:,i],label='DD2')
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

# Interactive variables
c11 = widgets.IntSlider(1,min=1,max=10,description='$c^{(1)}_1 = 3K^{(1)}$')
c12 = widgets.IntSlider(1,min=1,max=10,description='$c^{(1)}_2 = 2G^{(1)}$')
c21 = widgets.IntSlider(10,min=1,max=10,description='$c^{(2)}_1 = 3K^{(2)}$')
c22 = widgets.IntSlider(10,min=1,max=10,description='$c^{(2)}_2 = 2G^{(2)}$')

# Interactive devices
devices = widgets.Dropdown(
    options = [('',0),('computer',1),('smartphone',2)]
    ,description = 'Select device'
)

def plot_computer(c11,c12,c21,c22):
    plot(np.array([c11,c12]),np.array([c21,c22]))
    
def plot_smartphone(c11,c12,c21,c22):
    plot(np.array([c11,c12]),np.array([c21,c22]),orientation='v')

def check(device):
    if device==0:
        print('Please choose a device.')
    if device==1:
        print('You are using a computer')
        head1 = widgets.HBox([widgets.Label('Material 1'),c11,c12])
        head2 = widgets.HBox([widgets.Label('Material 2'),c21,c22])
        bottom = widgets.interactive(
            plot_computer
            ,{'manual':True}
            ,c11=c11,c12=c12,c21=c21,c22=c22
        )
        bottom.children[-2].description = 'Run/Update'
        display(head1)
        display(head2)
        display(bottom.children[-2])
        display(bottom.children[-1])
    if device==2:
        head = widgets.VBox([widgets.Label('Material 1'),c11,c12,widgets.Label('Material 2'),c21,c22])
        bottom = widgets.interactive(
            plot_smartphone
            ,{'manual':True}
            ,c11=c11,c12=c12,c21=c21,c22=c22
        )
        bottom.children[-2].description = 'Run/Update'
        display(head)
        display(bottom.children[-2])
        display(bottom.children[-1])
    
check_w = widgets.interactive(
    check
    ,device=devices
)
    
def start_interactive():
    display(check_w)