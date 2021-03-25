#Aidan Walk 
#ASTR 260-001
#Homework 08 Problem 1
#24 March 2021, 17:00

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


def buckinghamPotential(r):
    '''Buckingham Potential: Potential energy interaction btwn atoms
    takes in r, a distance in Angstroms
    returns phi, a potential in eV'''
    
    A = B = C = 1
    #Pauli exclusion principle (first term on right)
    pauliExclPrinc = A * np.exp(-1*B*r) 
    #Van der Waals attraction (second term on right)
    vDWAttraction = C / r**6
    #potential in eV
    buckinghamPotential = pauliExclPrinc - vDWAttraction
    
    return buckinghamPotential
    
def visualize(x=None, y=None):
    '''Plots the Buckingham Potential and its global max
    takes in: x, r [Angstroms]
              y, phi [eV]'''
    #plot min point on graph
    plt.scatter(max[0], max[1], color='red', s=25, label='Maximum')
    #plot a line of the whole function
    plt.plot(x, y, color='black')
    #adjust viewing zoom on plot
    plt.xlim(0, 6)
    plt.ylim(-3, 1)
    
    plt.title('Buckingham Potential')
    plt.xlabel('r [Angstroms]')
    plt.ylabel('phi [eV]')
    plt.legend() #show the key
    
    plotName = 'AidanWalk_HW08_1_plot.png'
    plt.savefig(plotName) #save plot
    print('PLOT SAVED TO:', plotName)
    

if __name__=='__main__':
    #define bounds of r for calculation
    rBegin = 0.5
    rEnd = 10
    numSteps = 100000 #number of steps to compute
    
    #define a numpy array of r's to pass through function phi
    r = np.linspace(rBegin, rEnd, numSteps)
    
    print('\n', 'Calculating Buckingham Potential...')
    phi = buckinghamPotential(r)
    
    print('\n', 'Finding Max Value...')
    maxX = opt.fmin(lambda r: -buckinghamPotential(r), 1) #find the X value of the max (or min of -f(x))
    max = (maxX, buckinghamPotential(maxX)) #calculate Y max based on X max
    print('\n', 'Maximum value occurs at', \
                 max[0], 'Angstroms, and', \
                 max[1], 'eV')
    
    print('\n', 'Plotting Buckingham Potential...')
    visualize(x=r, y=phi)