import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/home/daviolimen/repos/fcc-data-analysis-projects/Project_5/epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter('Year', 'CSIRO Adjusted Sea Level', xlim=(1880, 2050))

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = [i for i in range(1880, 2051)]
    y = [i * result.slope + result.intercept for i in x]
    plt.plot(x, y)

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    result2 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x2 = [i for i in range(2000, 2051)]
    y2 = [i * result2.slope + result2.intercept for i in x2]
    plt.plot(x2, y2)

    # Add labels and title
    plt.xticks(list(range(1850, 2100, 25)))
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('/home/daviolimen/repos/fcc-data-analysis-projects/Project_5/sea_level_plot.png')
    return plt.gca()

draw_plot()