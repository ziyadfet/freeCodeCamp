import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df.Year,df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    xvals1 = np.arange(171)
    reg1 = linregress(x=np.arange(len(df)),y=df["CSIRO Adjusted Sea Level"])
    bestfit1 = [(x*reg1.slope + reg1.intercept) for x in xvals1]
    plt.plot([x+1880 for x in xvals1],bestfit1,color='b')
  
    # Create second line of best fit
    reg2 = linregress(x=np.arange(14),y=df["CSIRO Adjusted Sea Level"][df.Year>1999])
    xvals2 = np.arange(51)
    bestfit2 = [(x*reg2.slope + reg2.intercept) for x in xvals2]
  
    # Add second line of best fit to plot
    plt.plot([(x+2000) for x in xvals2],bestfit2,color='r')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

draw_plot()