import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("mymoviedb.csv" , lineterminator='\n')
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())

df.head()
df.info()

df.duplicated().sum()
df['Genre'].head()
df.describe()

df['Release_Date']= pd.to_datetime(df['Release_Date'],
                                   errors='coerce')
print(df['Release_Date'].dtypes)
df['Release_Date']= df['Release_Date'].dt.year
df['Release_Date'].dtypes

#data cleaning 
cols = ['Overview', 'Original_Language', 'Poster_Url']
df.drop(cols, axis=1, inplace=True)

#categrozing vote average column
df['Vote_Average'] = pd.to_numeric(df['Vote_Average'],
                                   errors='coerce')

def categroize_col(df,col,labels):

    edges=[
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']

    ]
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates = 'drop')
    return df
labels= ['not_popular', 'below_average', 'average', 'popular']
 
categroize_col(df, 'Vote_Average', labels )
df['Vote_Average'].unique()
df.head()
df['Vote_Average'].value_counts()
df.dropna(inplace=True)
df.isna().sum()
#split genre 
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)
#casting column into category 
df['Genre']= df['Genre'].astype('category')
df['Genre'].dtypes
df.info()
df.nunique()

#Data Visualization
sns.set_style('whitegrid')
#what is the most frequent genre of movies released on netflix
df['Genre'].describe()
sns.catplot(y = 'Genre', data = df, kind = 'count',
            order= df['Genre'].value_counts().index,
            color = '#4287f5')
plt.title('Genre Column Distribution ')
plt.show()

#which has highest votes in vote column
sns.catplot( y= 'Vote_Average', data= df, kind='count',
             order= df['Genre'].value_counts().index,
            color = '#4287f5')
plt.title('Vote Distribution')
plt.show()

#which movie got the highest popularity ? what is its genre ?
df[df['Popularity'] == df['Popularity'].max()]

#which movie got the lowest popularity ? what is its genre?
df[df['Popularity'] == df['Popularity'].min()]

#which year has the most filmmed movies ?
df['Release_Date'].hist()
plt.title("Release Date Coulmn Distribution")
plt.show()
print(df.columns)
print(df['Vote_Average'].dtype)



 

 