import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Load your clean dataset
df_all = pd.read_csv('merged_happiness_data.csv')

## 1. Year-over-year boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_all, x='year', y='happiness_score')
plt.title('Year-over-Year Happiness Score Distribution')
plt.savefig('boxplot_yearly_distribution.png', dpi=300)
plt.close()

## 2. Top 10 happiest countries bar chart (latest year)
latest_year = df_all['year'].max()
top10 = df_all[df_all['year'] == latest_year].nlargest(10, 'happiness_score')
plt.figure(figsize=(8, 6))
sns.barplot(data=top10, x='happiness_score', y='country', palette='viridis')
plt.title(f'Top 10 Happiest Countries ({latest_year})')
plt.savefig('top10_happiest_countries.png', dpi=300)
plt.close()

## 3. Correlation heatmap
corr = df_all[['happiness_score', 'economy_gdp_per_capita', 'family',
               'health_life_expectancy', 'freedom', 
               'trust_government_corruption', 'generosity']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png', dpi=300)
plt.close()

## 4. Residual distribution for model evaluation
features = ['economy_gdp_per_capita', 'family', 'health_life_expectancy',
            'freedom', 'trust_government_corruption', 'generosity']
df_clean = df_all.dropna(subset=features + ['happiness_score'])
X = df_clean[features]
y = df_clean['happiness_score']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
residuals = y - y_pred
plt.figure(figsize=(8, 6))
sns.histplot(residuals, bins=30, kde=True, color='skyblue')
plt.title('Residual Distribution (Predicted - Actual)')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.savefig('residual_distribution.png', dpi=300)
plt.close()

print("✅ Visuals generated and saved for PowerPoint use.")
