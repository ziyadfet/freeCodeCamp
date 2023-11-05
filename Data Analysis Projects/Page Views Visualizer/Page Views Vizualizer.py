import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv")
df.date = pd.to_datetime(df.date)
df.set_index(df.date, inplace=True)

# Filtering outliers
upper_outliers = df.value.quantile(1-0.025)
lower_outliers = df.value.quantile(0.025)

df = df[df.value < upper_outliers]
df = df[df.value > lower_outliers]




def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5-2016-12/2019")
    ax.plot(df.date, df.value, color='red')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    df_bar.index = pd.to_datetime(df_bar.index)
    df_bar["month"] = df_bar.index.month
    df_bar["year"] = df_bar.index.year
    df_bar = df_bar.groupby(["month","year"]).mean()
    
    # Draw bar plot
    ax = df_bar.unstack(0).value.plot(kind='bar')
    fig = ax.get_figure()
    dpi = 200
    width_inches = 1514 / dpi
    height_inches = 1330 / dpi
    fig.set_dpi(dpi)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax.legend(labels=months,title="Months")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    fig.set_size_inches(width_inches, height_inches)
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(28.8/2,10.8/2),dpi=200)
    sns.boxplot(data=df_box, x = df_box.year,y=df_box.value, ax=ax[0])
    ax[0].set_xlabel("Years")
    ax[0].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box, x = df_box.month,y=df_box.value,ax=ax[1])
    ax[1].set_xlabel("Months")
    ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[1].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()
draw_box_plot()
draw_line_plot()