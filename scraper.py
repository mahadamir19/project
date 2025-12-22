import requests
from bs4 import BeautifulSoup

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
        job = {
            'title': row.h2.text.strip(),
            'company': row.h3.text.strip()
        }
        job_data.append(job)

    return job_data

if __name__ == "__main__":
    text = get_html("https://realpython.github.io/fake-jobs/")
    job_list = parse_html(text)
    print(job_list)