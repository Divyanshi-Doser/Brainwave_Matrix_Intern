import pandas as pd

df = pd.read_csv('E:synthetic_online_retail_data.csv')
print(df)
df.info()

#Count Of Missing Values
df.isnull()
print(df.isnull().sum())

#Filling Missing Values Of Column Review_Score
mean_value = df['review_score'].mean()
df['review_score'] = df['review_score'].fillna(mean_value)

print(df.isnull().sum())

#Filling Missing Values Of Column Gender
mode_value = df['gender'].mode()[0]
df['gender'] = df['gender'].fillna(mode_value)

print(df.isnull().sum())

#Replacing Values In Column Gender
df['gender'] = df['gender'].replace({'F':'Female', 'M':'Male'})
print(df.head(10))

df.to_csv('online_retail_store_data.csv', index = False)

