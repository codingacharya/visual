import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Sample data
def generate_data():
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'X': np.random.rand(100) * 100,
        'Y': np.random.rand(100) * 100,
        'Z': np.random.randn(100)
    })
    return df

df = generate_data()

# Streamlit UI
st.title("Data Visualization with 9 Charts")

# Creating a grid layout
col1, col2, col3 = st.columns(3)

# Matplotlib Line Chart
with col1:
    st.subheader("Line Chart (Matplotlib)")
    fig, ax = plt.subplots()
    ax.plot(df.index, df['X'], label='X')
    ax.plot(df.index, df['Y'], label='Y')
    ax.legend()
    st.pyplot(fig)

# Seaborn Bar Chart
with col2:
    st.subheader("Bar Chart (Seaborn)")
    fig, ax = plt.subplots()
    sns.barplot(x=df['Category'], y=df['X'], ax=ax)
    st.pyplot(fig)

# Plotly Scatter Plot
with col3:
    st.subheader("Scatter Plot (Plotly)")
    fig = px.scatter(df, x='X', y='Y', color='Category')
    st.plotly_chart(fig)

# Matplotlib Histogram
with col1:
    st.subheader("Histogram (Matplotlib)")
    fig, ax = plt.subplots()
    ax.hist(df['Z'], bins=20, alpha=0.7)
    st.pyplot(fig)

# Seaborn Boxplot
with col2:
    st.subheader("Boxplot (Seaborn)")
    fig, ax = plt.subplots()
    sns.boxplot(x=df['Category'], y=df['X'], ax=ax)
    st.pyplot(fig)

# Plotly Line Chart
with col3:
    st.subheader("Line Chart (Plotly)")
    fig = px.line(df, x=df.index, y=['X', 'Y'])
    st.plotly_chart(fig)

# Matplotlib Pie Chart
with col1:
    st.subheader("Pie Chart (Matplotlib)")
    fig, ax = plt.subplots()
    df_counts = df['Category'].value_counts()
    ax.pie(df_counts, labels=df_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)

# Seaborn Heatmap
with col2:
    st.subheader("Heatmap (Seaborn)")
    fig, ax = plt.subplots()
    corr = df[['X', 'Y', 'Z']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Plotly Bubble Chart
with col3:
    st.subheader("Bubble Chart (Plotly)")
    fig = px.scatter(df, x='X', y='Y', size='Z', color='Category')
    st.plotly_chart(fig)

st.write("### Data Table")
st.dataframe(df)