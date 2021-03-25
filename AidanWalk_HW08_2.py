#Aidan Walk
#ASTR 260-001
#Homework 08 Problem 2
#24 March 2021, 17:00

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

def f(x, y):
    '''f(x,y) = 5 * exp( -1*(x-1)**2 - 2*(y-3)**2 ) + 3 * exp( -2*(x-4)**2 - (y-1)**2
    takes in values of x and y
    returns f(x,y)'''
    firstTerm = 5 * np.exp( -1*(x-1)**2 - 2*(y-3)**2 )
    secondTerm = 3 * np.exp( -2*(x-4)**2 - (y-1)**2 )
    
    return firstTerm+secondTerm
    
def dfDx(x,y):
    '''returns the df/dx parital derivative'''
    return (f(x+h/2, y) - f(x-h/2, y))/h
    
def dfDy(x,y):
    '''returns the df/dy parital derivative'''
    return (f(x, y+h/2) - f(x, y-h/2))/h
    
def visualize(data):
    '''plots data in a countourf plot and saves it as a .png'''
    #plot Z in contour plot
    print('Plotting Z over domain {[0,5), [0,5)}...')
    plt.contourf(data)
    #save plot
    plotName = 'AidanWalk_HW08_2_contourPlot.png'
    xLabel = 'X/' + str(h)
    plt.xlabel(xLabel)
    plt.savefig(plotName)
    print('\n','PLOT SAVED TO:', plotName)
    
def gradientDescent(f=None, gamma=None, maxIterations=None, startingPt=None):
    '''computes the max of a function of two variables'''
    #I DID NOT FINISH THIS
    xmax = startingPt[0]
    ymax = startingPt[1]
    for dx in range(maxIterations):
        for dy in range(maxIterations):
            xmax = xmax - gamma*dfDx(dx, dy)
            ymax = ymax - gamma*dfDy(dx, dy)
    max = f(xmax, ymax)
    return max
    
    

if __name__ == '__main__':
    h = 0.01
    xs = ys = np.arange(0,5,h)
    X, Y = np.meshgrid(xs, ys)
    
    #calculate Z
    print('Calculating Z as a function of X,Y...')
    Z = f(X,Y)
    
    visualize(Z) #plot Z
    
    #Find the global max (min of -f'n)
    #minimize(lambda r,j: -f(r,j), [1,1]) 
    #I Cannot get this to work (namely the lambda with 2 variables). 
    
    print('Calculating global max of function via gradient descent...\nThis is incorrect')
    globalMax = gradientDescent(f=f, gamma=.1, maxIterations=100, startingPt=[2,4])
    print(globalMax)
    #^I know this is wrong. not enough time to diagnose problem b/c I have to turn in now. 




