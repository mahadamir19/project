from cleaner import fetch_data_from_cleaner
import sqlite3
import pandas as pd

def initialize_db():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE jobs(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   company TEXT,
                   salary INTEGER
                   )""")
    
    conn.commit()
    conn.close()

def insert_jobs(df):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""INSERT INTO jobs (title, company, salary) VALUES (:title, :company, :salary)""", 
                       {"title": row['title'], "company": row['company'], "salary": row['salary']})
    
    conn.commit()
    conn.close()

def load_all_jobs():
    conn = sqlite3.connect('jobs.db')
    df_jobs = pd.read_sql("SELECT * FROM jobs",conn)
    return df_jobs

if __name__ == "__main__":
    df = fetch_data_from_cleaner()

    # initialize_db()   # <--- run this once to setup the jobs table
    # insert_jobs(df)   # <--- run this to insert jobs from the pandas df


    # ----TESTING----
    # print(df['salary'].min())
    # print(df['salary'].max())
    # print(df['salary'].mean())

    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()

    # cursor.execute("SELECT * FROM jobs WHERE salary > 100000 ORDER BY salary DESC")
    # cursor.execute("SELECT COUNT(DISTINCT company) FROM jobs")
    # cursor.execute("SELECT COUNT(DISTINCT title) FROM jobs")

    print(cursor.fetchall())
    print(len(cursor.fetchall()))

    conn.close()
