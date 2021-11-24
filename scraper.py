
import requests
from bs4 import BeautifulSoup
import urllib


def get_content(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    title = soup.title
    # print(title)
    print(title.get_text())

    filename = "urls.txt"
    f = open(filename, "w")

    media_titles = soup.find_all('h3', class_="media__title")
    for title in media_titles:
        print(title.text.strip())
    # print(media_titles)
    #print("title" + str(len(media_titles)))

    anchors = soup.find_all('a', class_="media__link")

    for link in anchors:
        linkText = urllib.parse.urljoin(url, str(link.get('href')))
        print(linkText)

    # print(link.get('href'))
    #print("a" + str(len(anchors)))

    media_summary = soup.find_all('p', class_="media__summary")

    for content in media_summary:
        print(content.text.strip())
        # print("summary" + str(len(media_summary)))

    media_contents = soup.find_all('div', class_="media__content")
    for article in media_contents:
        f.write(str(article))
    #print("content" + str(len(media_contents)))

  # print(soup.prettify())
  # print(soup.get_text())


get_content("https://www.bbc.com/")
