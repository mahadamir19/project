from scraper import fetch_data_from_scraper
import pandas as pd

def clean_salary(jobs):
    df = pd.DataFrame(jobs)
    df['salary'] = df['salary'].str.replace('$', '')
    df['salary'] = df['salary'].str.replace(r'[kK]', '', regex=True).astype(float)
    df['salary'] = df['salary'] * 1000
    df['salary'] = df['salary'].astype(int)
    df.drop_duplicates(inplace=True)

    return df

def fetch_data_from_cleaner():
    job_list = fetch_data_from_scraper()
    df = clean_salary(job_list)

    return df

if __name__ == "__main__":
    job_list = fetch_data_from_scraper()
    df = clean_salary(job_list)
    