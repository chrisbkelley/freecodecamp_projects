import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col="date")

# Clean data
df = df = df[(df['value'] >= df['value'].quantile(.025)) &\
       (df['value'] <= df['value'].quantile(.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(24,12))
    df['value'].plot(ax=ax)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # list of months names to be mapped as categorical data
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']

    # create separate columns for years/months 
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = pd.Categorical(df_bar.index.month_name(),categories=months,ordered=True)

    #remove the index and then delete entire column.  It is not needed for the bar chart
    df_bar.reset_index(inplace=True)
    df_bar.drop(columns=['date'], inplace=True)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,6))
    df_bar.pivot_table(values='value',index='year',columns='month',aggfunc=np.mean).plot(kind='bar', ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # needed to map month to sort month names in order staring with Jan. 
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df_box2 = df_box.copy()
    df_box2['month'] = pd.Categorical(df_box2['month'],categories=months,ordered=True)
    # Draw box plots (using Seaborn)

    #create figure and subplots 
    fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2,figsize=(36,15))

    #settings for year wise box plot
    ax1 = sns.boxplot(x="year",y="value", data=df_box, ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_ylabel("Page Views")
    ax1.set_xlabel("Year")

    #settings for month wise box plot
    ax2 = sns.boxplot(x="month",y="value", data=df_box2, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_ylabel("Page Views")
    ax2.set_xlabel("Month")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
