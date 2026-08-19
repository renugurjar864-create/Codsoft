import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Fetch web page data
url = 'https://quotes.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. Extract Structured Information
    quotes_data = []
    quotes = soup.find_all('div', class_='quote')
    
    for q in quotes:
        text = q.find('span', class_='text').get_text()
        author = q.find('small', class_='author').get_text()
        quotes_data.append({'Quote': text, 'Author': author})
    
    # 3. Clean and Organize into DataFrame
    df_quotes = pd.DataFrame(quotes_data)
    print("--- Web Scraping Results ---")
    print(df_quotes.head())
    
    # 4. Export results to CSV
    df_quotes.to_csv('scraped_quotes.csv', index=False)
    print("\nData successfully scraped and saved to CSV!")
else:
    print("Failed to retrieve web page")
