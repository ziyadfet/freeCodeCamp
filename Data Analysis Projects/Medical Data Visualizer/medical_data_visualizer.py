import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')
#Cleaning
overweight = []
for h,w in zip(df.height,df.weight):
    if (w/((h/100)**2)) > 25:
        overweight.append(1)
    else: 
        overweight.append(0)
df['overweight'] = overweight
df.cholesterol = df.cholesterol.replace(1,0)
df.cholesterol = df.cholesterol.replace([2,3],1)
df.gluc = df.gluc.replace(1,0)
df.gluc = df.gluc.replace([2,3],1)

def draw_cat_plot():
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    df_cat = df_cat.reset_index().groupby(['variable','cardio','value']).agg('count').rename(columns={"index":"total"}).reset_index()
    sns.catplot(data=df_cat,x="variable",y="total",hue="value",kind="bar",col="cardio")
    fig = sns.catplot(data=df_cat,x="variable",y="total",hue="value",kind="bar",col="cardio").fig
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():    
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))& (df['height'] <= df['height'].quantile(0.975))& (df['weight'] >= df['weight'].quantile(0.025))& (df['weight'] <= df['weight'].quantile(0.975))]
    corr = df_heat.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    fig = plt.figure(figsize=(12,6))
    sns.heatmap(corr, mask=mask,
                annot=True, fmt='.1f',
                center=0, vmin=-0.5, vmax=0.5)
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()