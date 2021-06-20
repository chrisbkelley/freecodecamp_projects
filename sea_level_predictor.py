import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    
    # used to set bounds for figure 
    extend_start_year = x[0:].values[0]
    extend_end_year = x[-1:].values[0]+51
    
    # Create scatter plot
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # use slope and intercept to calculate predicted sea level rise to year 2050
    x_line1 = list(range(1880, 2051))
    y_line1 = []
    for year in x_line1:
        y_line1.append(intercept + slope*year)
    
    # regression model from year 2000 to 2050
    df_2000 = df[df["Year"] >= 2000]
    x2 = df_2000["Year"]
    y2 = df_2000["CSIRO Adjusted Sea Level"]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2,y2)

    x_line2 = list(range(2000,2051))
    y_line2 = []
    for year in x_line2:
        y_line2.append(intercept2 + slope2*year)
    
    #create plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax = plt.scatter(x,y)
    
    # set bounds of x and y plots
    #plt.xlim(extend_start_year, extend_end_year)
    #plt.ylim(-1,12)
    
    # Create first line of best fit
    plt.plot(x_line1, y_line1, 'r', label = 'Bests Fit Line 1')

    # Create second line of best fit
    plt.plot(x_line2, y_line2, 'r', label = 'Bests Fit Line 2')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
       
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
