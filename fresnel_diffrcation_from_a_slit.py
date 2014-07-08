# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 11:45:42 2014

Fresnel Diffraction From A Slit

@author: Stephen James, Cranfield University
"""
import scipy
import numpy as np
from scipy.special import fresnel
import matplotlib
import matplotlib.pyplot as plt




d = 0.75             # slitwidth mm
lam = 2.66e-4       # wavelength mm
x = np.linspace(-1.5*d,1.5*d,5000) # distance in x direction mm
z = np.linspace(0,3,1000) # log10 of the distance to the screen mm

I1 = np.zeros((len(x),len(z))) # set up array to receive the intensity data

# fix slitwidth, vary screen location
for i in range (0,len(z)-1):
    alpha_1 = (x+d/2)*(np.sqrt(2/(lam*10**z[i])))
    alpha_2 = (x-d/2)*(np.sqrt(2/(lam*10**z[i])))
    s1, c1 = fresnel(alpha_1) #Fresnel integrals
    s2, c2 = fresnel(alpha_2) #Fresnel integrals
    Intensity = 0.5*((c2-c1)**2+(s2-s1)**2)
    I1[:,i]= Intensity


zplot = 310 # distance at which you would  like to plot the intesity pattern mm

plt.figure(1)
plt.plot(x,I1[:,np.where(10**z>zplot-1)[0][0]])
plt.xlabel("x (mm)")
plt.ylabel("Intensity (au)")
plt.title("Intensity profile " +  str(int(10**z[np.where(10**z>zplot-1)[0][0]])) + "mm behind a slit of width " + str(d) + "mm")


# plot limts
x_min = np.min(x)
x_max = np.max(x)
z_min = np.min(z)
z_max = np.max(z)

plt.figure(2)
plt.imshow(I1, cmap=matplotlib.cm.gray, interpolation='nearest', aspect='auto', origin='lower', extent = [ 10**(z_min), 10**(z_max), x_min, x_max,] )
plt.xscale('log')
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')


# fix screen position, vary slit width

d = np.linspace(0.2,1,1000) # slitwidth  mm
x = np.linspace(-1*np.max(d),1*np.max(d),5000) # distance in x direction mm
z = 300 # distance to screen mm

I2 = np.zeros((len(x),len(d))) # set up array to receive the intensity data

for i in range (0,len(d)-1):
    alpha_1 = (x+d[i]/2)*(np.sqrt(2/(lam*z)))
    alpha_2 = (x-d[i]/2)*(np.sqrt(2/(lam*z)))
    s1, c1 = fresnel(alpha_1) #Fresnel integrals
    s2, c2 = fresnel(alpha_2) #Fresnel integrals
    Intensity = 0.5*((c2-c1)**2+(s2-s1)**2)
    I2[:,i]= Intensity

# plot limits
x_min = np.min(x)
x_max = np.max(x)
d_min = np.min(d)
d_max = np.max(d)

plt.figure(3)
plt.imshow(I2, cmap=matplotlib.cm.gray, interpolation='nearest', aspect='auto', origin='lower', extent = [ d_min, d_max, x_min, x_max,] )
plt.xlabel('Slitwidth (mm)')
plt.ylabel('x (mm)')
plt.title("Intensity as function of slitwidth" + "\n" + "assuming wavelength 266 nm and viewing distance " +  str(z) + "mm")


plt.show()