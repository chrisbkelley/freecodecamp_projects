import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
#divides weight given in kg by the square of height that has converted from cm to m  
overweight_formula = df['weight']/(df['height']*.01)**2

#set binary values in overweight col based on results of formula
df.loc[overweight_formula > 25, 'overweight'] = 1
df.loc[overweight_formula < 26, 'overweight'] = 0

#the formula returns a float but it should be an integer datatype
df['overweight'] = df['overweight'].astype(int)

#normalize the cholesterol and gluc features
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1

    # Draw the catplot with 'sns.catplot()'
    fig = plt.figure()
    sns.catplot(x="variable", y="total", col="cardio", data=df_cat, kind="bar", hue="value", estimator=sum)

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df_heat = df[(df['ap_lo'] <= df['ap_hi']) & \
            (df['height'] >= df['height'].quantile(0.025)) &\
            (df['height'] <= df['height'].quantile(0.975)) &\
            (df['weight'] >= df['weight'].quantile(0.025)) &\
            (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr().round(decimals=1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_heat.corr(), dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,6))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask, annot=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
