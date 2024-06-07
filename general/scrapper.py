import requests
from bs4 import BeautifulSoup


def main():
    base_url = "https://yts.mx/browse-movies/"
    for num in range(1, 3043):
        url = f"{base_url}page/{num}"
        page_content = requests.get(url)    
        print(f"Getting data for page {num}")
        content = BeautifulSoup(page_content.text, 'html.parser')
        for movies in content.find_all('articles'):
            title = movies.find('div', {'class': "browse-movie-bottom"})
            print(title)