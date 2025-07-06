# ---------------------------------------------------------------
# 🔹 Step 18: Streamlit Dashboard for Global Happiness Project
# ---------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('merged_happiness_data.csv')

# Sidebar - year selection
year = st.sidebar.selectbox("Select Year", sorted(df['year'].unique()))

# Filter by selected year
df_year = df[df['year'] == year]

# Dashboard Title
st.title(f"🌍 Global Happiness Dashboard ({year})")

# 1️⃣ Display top 10 happiest countries
st.subheader("Top 10 Happiest Countries")
top10 = df_year.nlargest(10, 'happiness_score')
fig_bar = px.bar(top10, x='happiness_score', y='country', orientation='h',
                 color='happiness_score', color_continuous_scale='viridis',
                 labels={'happiness_score':'Happiness Score', 'country':'Country'})
st.plotly_chart(fig_bar, use_container_width=True)

# 2️⃣ Animated Global Choropleth
st.subheader("Global Happiness Scores Map")
fig_map = px.choropleth(df, locations='country', locationmode='country names',
                        color='happiness_score', hover_name='country',
                        animation_frame='year', color_continuous_scale='Viridis',
                        title='Animated Global Happiness Scores (2015–2019)')
st.plotly_chart(fig_map, use_container_width=True)

# 3️⃣ Correlation Heatmap
st.subheader("Correlation Heatmap")
numeric_df = df_year.select_dtypes(include='number')
correlation = numeric_df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)
