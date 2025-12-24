## 📝 Project Overview
This project is an automated **ETL (Extract, Transform, Load) Pipeline** designed to analyze the remote job market. 

The application scrapes job postings from *https://realpython.github.io/fake-jobs/*, cleans the unstructured text using Regex, stores historical data in a SQL database, and visualizes trends (such as top paying jobs) via an interactive dashboard.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Collection:** BeautifulSoup4, Requests
* **Data Processing:** Pandas, Regular Expressions (Regex)
* **Database:** SQLite
* **Visualization:** Streamlit, Matplotlib, Seaborn
* **Deployment:** Streamlit Cloud

## ⚙️ Architecture
The system follows a linear pipeline structure:

1.  **Scraper (`scraper.py`):** Fetches raw HTML from job boards and parses the DOM to extract Title, Company strings, and I also generated a salary column.
2.  **Cleaner (`cleaner.py`):**
    * Cleans the salary text column and converts it into integers e.g. "$62.4K" --> "62400".
3.  **Database (`database.py`):**
    * Persists data in a local `jobs.db` SQLite file.
4.  **Dashboard (`app.py`):** Reads from the database and renders an interactive UI with filtering capabilities.

## 📂 Project Structure
```text
├── app.py              # Main dashboard application (Streamlit)
├── scraper.py          # Logic for extracting raw data
├── cleaner.py          # Logic for cleaning and normalizing data
├── database.py         # SQL schema and storage functions
├── requirements.txt    # Project dependencies
└── jobs.db             # SQLite database (stores the data)

I deployed the final app via streamlit at the following link:
[![Streamlit App](https://8zanys3tsvgjbohnphpch2.streamlit.app/)

## 🔧 How to Run It on Your Own

If you want to run this project locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/mahadamir19/project.git](https://github.com/mahadamir19/project.git)
cd project

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Launch the dashboard
streamlit run app.py
