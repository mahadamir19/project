import streamlit as st
import pandas as pd
from database import load_all_jobs
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return load_all_jobs()

def configure_sidebar(df):
    st.sidebar.title("Filter Jobs")
    titles = ["All"] + list(df['title'].dropna().unique())
    title_filter = st.sidebar.selectbox("Select job title", titles)
    min_salary = st.sidebar.number_input("Enter minimum search salary", min_value=30000, max_value=150000, value=30000, step=10000)

    dict = {'title_choice': title_filter, 'salary_choice': min_salary}
    return dict

def filter_data(df, user_choices):
    if user_choices['title_choice'] == "All":
        filtered_df = df[df['salary'] >= user_choices['salary_choice']]
    else:
        filtered_df = df[(df['salary'] >= user_choices['salary_choice']) & (df['title'] == user_choices['title_choice'])]
    return filtered_df

def display_metrics(filtered_df):
    st.title("Search Results")
    st.write(f"Total jobs found: {len(filtered_df)}")
    
    col1, col2 = st.columns(2)

    with col1:
        bins = [0, 40000, 60000, 80000, 100000, 120000, 150000]
        labels = ["30k-40k", "40k-60k", "60k-80k", "80k-100k", "100k-120k", "120k-150k"]
        filtered_df['salary_range'] = pd.cut(filtered_df['salary'], bins=bins, labels=labels, include_lowest=True)

        salary_counts = filtered_df['salary_range'].value_counts().sort_index()
        salary_counts_df = salary_counts.reset_index()
        salary_counts_df.columns = ['salary_range', 'job_count']

        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(x='salary_range', y='job_count', data=salary_counts_df, palette='viridis',hue='salary_range', ax=ax)
        ax.set_xlabel("Salary Range")
        ax.set_ylabel("Number of Jobs")
        ax.set_title("Jobs per Salary Range")
        st.pyplot(fig)
    
    with col2:
        top_jobs = filtered_df.sort_values(by='salary', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(x='salary', y='title', data=top_jobs, color='skyblue', ax=ax)
        ax.set_xlabel("Salary")
        ax.set_ylabel("Job Title")
        ax.set_title("Top 10 Highest Paying Jobs")
        st.pyplot(fig)

    filtered_df.drop(columns='salary_range', inplace=True)
    filtered_df.sort_values(by='salary', ascending=True, inplace=True)
    st.write("Jobs list")
    st.dataframe(filtered_df)


if __name__ == '__main__':
    df_jobs = load_data()
    user_choices = configure_sidebar(df_jobs)
    filtered_df = filter_data(df_jobs, user_choices)
    display_metrics(filtered_df)