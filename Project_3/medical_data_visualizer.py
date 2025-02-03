import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('/home/daviolimen/repos/fcc-data-analysis-projects/Project_3/medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100)**2)) > 25

# 3
df['cholesterol'] = df['cholesterol'] > 1
df['gluc'] = df['gluc'] > 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=('cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'))

    # 6
    df_cat = df_cat.value_counts().to_frame()
    df_cat.columns = ['total']
    df_cat.sort_values(['cardio', 'value', 'variable'], inplace=True)
    
    # 7



    # 8
    fig = sns.catplot(df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').figure


    # 9
    fig.savefig('/home/daviolimen/repos/fcc-data-analysis-projects/Project_3/catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df.ap_lo <= df.ap_hi) & (df.height >= df.height.quantile(0.025)) & (df.height <= df.height.quantile(0.975)) & (df.weight >= df.weight.quantile(0.025)) & (df.weight <= df.weight.quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool), k=0)

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax)


    # 16
    fig.savefig('/home/daviolimen/repos/fcc-data-analysis-projects/Project_3/heatmap.png')
    return fig
