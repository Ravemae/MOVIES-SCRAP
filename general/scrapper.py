import requests
from session import add_movie
from bs4 import BeautifulSoup

def main():
    base_url = "https://yts.mx/browse-movies/"
    for num in range(1, 3043):
        url = f"{base_url}page/{num}"
        page_content = requests.get(url)
        print(f"Getting data for page {num}")
        content = BeautifulSoup(page_content.text, 'html.parser')
        for movies in content.find_all('article'):
            title = movies.find('div', {'class': "browse-movie-bottom"})
            if title:
                name = title.text.strip()
            else:
                print("Title not found")
                continue

            f_type = movies.find('h2', {'class': "hidden-xs"})
            if f_type:
                m_type = f_type.text.strip()
            else:
                print("Movie type not found")
                continue

            date = movies.find('div', {'class': "browse-movie-year"})
            if date:
                year = date.text.strip()
            else:
                print("Year not found")
                continue

            img = movies.find('img')
            image = img.get('src') if img else None

            f_rating = movies.find('div', {'class': "rating-row"})
            if f_rating:
                rating = f_rating.text.strip()
            else:
                print("Rating not found")
                continue

            link = movies.find('a')['href']
            if link:
                movie_page = requests.get(link)
                movie_soup = BeautifulSoup(movie_page.text, 'html.parser')
                download_link = None
                for x in movie_soup.find_all('a', {'class': "torrent-modal-download button-green-download2-big hidden-xs hidden-sm"}):
                    download = x.get('href')
                    if 'javascript' not in download:
                        download_link = download
                        break

                if download_link:
                    add_movie(name, m_type, year, rating, image, download_link)
                else:
                    print("Download link not found")
            else:
                print("Movie link not found")

main()
print("Successfully added into Database! :)")
