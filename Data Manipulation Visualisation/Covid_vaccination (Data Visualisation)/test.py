import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('vaccination-data.csv')
# print(df.head(2))
# print(df.shape)
#df.isnull().sum()

df = df.dropna(subset=['COUNTRY','TOTAL_VACCINATIONS','PERSONS_VACCINATED_1PLUS_DOSE'])
df = df.drop_duplicates()
df['TOTAL_VACCINATIONS'] = pd.to_numeric(df['TOTAL_VACCINATIONS'],errors='coerce')
df['PERSONS_VACCINATED_1PLUS_DOSE'] = pd.to_numeric(df['PERSONS_VACCINATED_1PLUS_DOSE'],errors='coerce')
df['TOTAL_VACCINATIONS'] = df['TOTAL_VACCINATIONS'].fillna(df['TOTAL_VACCINATIONS'].median())
df['PERSONS_VACCINATED_1PLUS_DOSE'] = df['PERSONS_VACCINATED_1PLUS_DOSE'].fillna(df['PERSONS_VACCINATED_1PLUS_DOSE'].median())
print(df.head(3))
print(df.shape)


plt.figure(figsize=(10,5))
plt.hist(df['TOTAL_VACCINATIONS'],bins=15)
plt.title("Total Vaccination Distribution")
plt.xlabel('Total Vaccinations')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,5))
plt.scatter(df['TOTAL_VACCINATIONS'],df['PERSONS_VACCINATED_1PLUS_DOSE'])
plt.title("Total Vaccination v/s No. of Persons vaccinated with 1+ Dose")
plt.xlabel('Total Vaccinations')
plt.ylabel('No. of Persons vaccinated with 1+ Dose')
plt.show()



