import streamlit as st
import numpy as np
import matplotlib.pyplot as plt 

N_LIMIT = 1000

x = np.arange(N_LIMIT,dtype=np.uint16)
y = np.arange(N_LIMIT,dtype=np.uint16)

xx, yy = np.meshgrid(x,y)

int_and = np.bitwise_and(xx,yy)
int_or  = np.bitwise_or(xx,yy)
int_xor = np.bitwise_xor(xx,yy)

names = ["AND", "OR", "XOR"]

"## Linear scale"
fig, axs = plt.subplots(1, 4, 
    gridspec_kw={'width_ratios':[2,2,2,0.1]},
    figsize=[14,4])

for ax,name,data in zip(axs,names,[int_and,int_or,int_xor]):
    mapable = ax.imshow(data, origin='lower')
    ax.set_title(name)
    
plt.colorbar(mapable,cax=axs[-1])
st.pyplot(fig, dpi=300)

"## Log-scale"
fig, axs = plt.subplots(1, 4, 
    gridspec_kw={'width_ratios':[2,2,2,0.1]},
    figsize=[14,4])

for ax,name,data in zip(axs,names,[int_and,int_or,int_xor]):
    mapable = ax.imshow(np.log10(data), origin='lower', vmin=0,vmax=3)
    ax.set_title(name)
    
plt.colorbar(mapable,cax=axs[-1])
st.pyplot(fig, dpi=300)
