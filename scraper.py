
import requests
from bs4 import BeautifulSoup


def get_content(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    title = soup.title
    # print(title)
    print(title.get_text())

    # for link in soup.find_all('a'):
    # print(link.get('href'))

    sections = soup.find_all('section', class_="module module--content-block")
    # print(sections)
    container = soup.find_all('div', class_="module__content")
    # print(container)

    articles = soup.find_all(
        'ul', class_="media-list media-list--fixed-height")
    # print(articles)

    media_titles = soup.find_all('h3', class_="media__title")
    for title in media_titles:
        print(title.text)
    # print(media_titles)

    anchors = soup.find_all('a', class_="media__link")
    all_links = set()
    for link in anchors:
        if (link.get('href') != '#'):
            linkText = "https://www.bbc.com/" + \
                link.get('herf')  # Error while concatinating
            all_links.add(link)
            print(linkText)
        # print(link.get('href'))
    # print(anchors)


   # print(soup.prettify())
   # print(soup.get_text())
get_content("https://www.bbc.com/")
