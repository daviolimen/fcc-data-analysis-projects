import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/home/daviolimen/repos/fcc-data-analysis-projects/Project_4/fcc-forum-pageviews.csv', index_col='date', parse_dates=True)


# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df, color='red')
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('/home/daviolimen/repos/fcc-data-analysis-projects/Project_4/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(['year', 'month'], sort=False)['value'].mean())
    df_bar = df_bar.unstack('month')
    df_bar.columns.names = ['value', 'Months']
    df_bar = df_bar.droplevel('value', axis=1)
    df_bar = pd.concat([df_bar.iloc[:, 8:], df_bar.iloc[:, :8]], axis=1)

    # Draw bar plot
    ax = df_bar.plot.bar(figsize=(8, 8))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    fig = ax.figure
    # Save image and return fig (don't change this part)
    fig.savefig('/home/daviolimen/repos/fcc-data-analysis-projects/Project_4/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    order_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(20, 5))
    ax1, ax2 = axs
    sns.boxplot(df_box, x='year', y='value', ax=ax1)
    sns.boxplot(df_box, x='month', y='value', ax=ax2, order=order_of_months)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax1.set_xlabel('Year')
    ax2.set_xlabel('Month')
    ax1.set_ylabel('Page Views')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('/home/daviolimen/repos/fcc-data-analysis-projects/Project_4/box_plot.png')
    return fig
