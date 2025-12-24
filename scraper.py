import requests
from bs4 import BeautifulSoup
import random

salaries = [
    "$45.2k", "$78.9K", "$120.5k", "$32.1K", "$65.0k", 
    "$98.4K", "$55.7k", "$41.3K", "$110.2k", "$88.6K", 
    "$72.1k", "$60.4K", "$150.8k", "$39.5K", "$92.3k", 
    "$50.0K", "$105.1k", "$44.8K", "$81.7k", "$67.2K", 
    "$135.4k", "$48.9K", "$76.3k", "$59.1K", "$112.6k", 
    "$42.7K", "$85.0k", "$69.8K", "$95.5k", "$36.2K", 
    "$125.3k", "$52.6K", "$79.4k", "$63.9K", "$101.7k", 
    "$47.5K", "$83.2k", "$71.6K", "$118.9k", "$40.4K", 
    "$91.1k", "$58.3K", "$140.2k", "$37.8K", "$74.5k", 
    "$66.7K", "$108.4k", "$53.9K", "$87.1k", "$61.5K"
]

def get_html(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=header)
    if (r.status_code != 200):
        print(f"The GET request was not a success as the status code is: {r.status_code}")
        return None
    
    return r.text

def parse_html(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    job_data = []
    for row in soup.find_all('div', class_='media-content'):
        random_index = random.randint(1,49)
        job = {
            'title': row.h2.text.strip(),
            'company': row.h3.text.strip(),
            'salary' : salaries[random_index] # since the target url did not have a salary or a numerical column,
            # I generated random salaries from indexing a list so I can perform data cleaning too
        }
        job_data.append(job)

    return job_data

def fetch_data_from_scraper():
    text = get_html("https://realpython.github.io/fake-jobs/")
    job_list = parse_html(text)
    return job_list

if __name__ == "__main__":
    text = get_html("https://realpython.github.io/fake-jobs/")
    job_list = parse_html(text)
    print(job_list)