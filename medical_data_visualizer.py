import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
# Clean data


# Add 'overweight' column
df['overweight'] = 0
BMI = df['weight']/(0.01*df['height'])**2
df.loc[BMI > 25, 'overweight']=1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    cat_df=df.melt(id_vars=['cardio'], value_vars=[
    'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'
]
       )
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'

    sns.catplot(x='variable', hue='value', data=cat_df, col='cardio', kind='count')
    
    # Get the figure for the output
    fig = sns.catplot(x='variable', hue='value', data=cat_df, col='cardio', kind='count')
    fig.set(ylabel='total')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data

    df_heat = df.drop(df[df['ap_lo'] > df['ap_hi']].index)
    df_heat = df_heat.drop(df_heat[df_heat['height'] < df['height'].quantile(0.025)].index)
    df_heat = df_heat.drop(df_heat[df_heat['height'] > df['height'].quantile(0.975)].index)
    df_heat = df_heat.drop(df_heat[df_heat['weight'] < df['weight'].quantile(0.025)].index)
    df_heat = df_heat.drop(df_heat[df_heat['weight'] > df['weight'].quantile(0.975)].index)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    corr = df_heat.corr()
    mask=np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    
    fig, ax = plt.subplots()
    ax=sns.heatmap(corr,mask=mask, annot=True, fmt='.1f')
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
