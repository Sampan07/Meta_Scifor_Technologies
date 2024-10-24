import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('catalog.csv')


df_clean = df.drop(['time', 'continent_code', 'storm_name', 'location_description', 'source_name', 'source_link'], axis=1)
df_clean['injuries'].fillna(df_clean['injuries'].median())
df_clean['fatalities'].fillna(df_clean['fatalities'].median())
df_clean['landslide_type'].fillna(df_clean['landslide_type'].mode()[0])
df_clean['landslide_size'].fillna(df_clean['landslide_size'].mode()[0])
df_clean['population'].fillna(df_clean['population'].median())
df_clean['distance'].fillna(df_clean['distance'].median())
df_clean['latitude'].fillna(df_clean['latitude'].median())
df_clean['longitude'].fillna(df_clean['longitude'].median())


sns.histplot(df_clean['fatalities'], bins=20, kde=True)
plt.show()

sns.heatmap(df_clean.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.show()


features = ['population', 'distance', 'latitude', 'longitude']
target = 'fatalities'
X = df_clean[features]
y = df_clean[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")
