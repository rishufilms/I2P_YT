# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:09:36 2020

@author: RishuFilms
"""

"""
***************************************************************
******************  Import Required Modules  ******************
***************************************************************
"""

import numpy as np
import matplotlib.pyplot as plt

"""
***************************************************************
******************  Declaring Input Values  *******************
***************************************************************
"""

P=1000
percent=1/100
month=1
year=12*month
r=12*percent
rm=r/12

fig_sz=(6,5)
fz=12


"""
***************************************************************
***************  Loop for Different Durations *****************
***************************************************************
"""

for time in range(1,101):
    
    t=time*year
    EMI=P/np.sum(np.power((1/(1+rm)),range(1,t+1)))
    
    Intr=P*rm*np.ones(t)
    PP=EMI-Intr
    
    for ii in range(1,t):
        Intr[ii]=(P-sum(PP[0:ii]))*rm
        PP[ii]=EMI-Intr[ii]
    

    fig1=plt.figure(figsize=fig_sz)
    ax1=plt.axes([0.125,0.125,0.75,0.75])
    
    xt=np.ceil(0.1*t)
    yt=np.ceil(0.2*EMI)
    
    ax1.set_xlim([-0.05*t,1.15*t])
    ax1.set_xticks(np.arange(1,1.2*t,xt))
    ax1.set_ylim([0,1.1*EMI])
    ax1.set_yticks(np.arange(1,1.1*EMI,yt))

    """
    ***************************************************************
    *******************  Plotting the Results  ********************
    ***************************************************************
    """    
    
    plt.fill_between(range(1,t+2),EMI*np.ones(t+1),\
                     step="pre",color='g')
    
    Intr2=np.append(Intr,Intr[t-1])
    
    plt.fill_between(range(1,t+2),Intr2,\
                      step="post",color='r');
    
    plt.xlabel('EMI Count')
    plt.ylabel('Payment per EMI')
    
    str1='No. of Years = '+str(time)
    plt.text(0.3*t,1.05*EMI, str1, fontsize=fz)
    str2='EMI = '+str(round(EMI,2));
    plt.text(0.8*t,1.05*EMI, str2, fontsize=fz)
    
    plt.show()
