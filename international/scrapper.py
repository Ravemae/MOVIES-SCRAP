import requests
from .session import add_movie
from bs4 import BeautifulSoup
import asyncio


async def fetch_page(url):
    page_content = requests.get(url).text
    return BeautifulSoup(page_content, 'html.parser')

async def fetch():
    base_url = "https://nkiri.com/category/international/"
    for num in range(6, 81):
        url = f'{base_url}page/{num}'
        print(f"Getting data for page {num}")
        soup = await fetch_page(url)
        for movie in soup.find_all('article'):
            name = movie.find('h2', {'class': "blog-entry-title entry-title"})
            title = name.text.strip()
            
            date = movie.find('div', {'class': 'blog-entry-date clr'})
            f_date = date.text.strip()
            
            img = movie.find('img')
            if img:
                image = img.get('src')
            else:
                image = None
            
            link = movie.find('a')['href']
            
            movie_page = requests.get(link)
            movie_soup = BeautifulSoup(movie_page.text, 'html.parser')
            download_link = None
            for x in movie_soup.find_all('a', {'class': "elementor-button elementor-button-link elementor-size-md"}):
                download = x.get('href')
                if 'html' in download:
                    download_link = download
                    break
            desc_text = None
            for item in movie_soup.find_all('div', {'class': 'overview'}):
                desc = item.find('p')
                if desc:
                    desc_text = desc.text.strip()
                    break
            add_movie(name=title, image=image, date=f_date, download_link=download_link, description=desc_text)

async def main():            
    await fetch()
print("Successfully added into Database! :)")
asyncio.run(main())
