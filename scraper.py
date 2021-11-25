
import requests
from bs4 import BeautifulSoup

#import urllib


def get_content(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')

    page_title = soup.title
    # print(title)
    print("Page Title: ", page_title.get_text())

    filename = "urls.txt"
    f = open(filename, "w")
    '''

    media_titles = soup.find_all('h3', class_="media__title")
    for title in media_titles:
        print("Title: ", title.text.strip())

    media_links = soup.find_all('a', class_="media__link")

    for link in media_links:
        linkText = urllib.parse.urljoin(url, str(link.get('href')))
        print("URL: ", linkText)

    media_contents = soup.find_all('p', class_="media__summary")

    for summary in media_contents:
        print("Content: ", summary.text.strip())

    '''

    media_contents = soup.find_all('div', class_="media__content")
    for article in media_contents:
        f.write(str(article))
    #print("content" + str(len(media_contents)))
    f.close()

    for content in media_contents:
        m_title = content.h3.text.strip()
        #media_link = content.h3.a["href"]
        #media_summary = content.p.text
        try:
            media_link = content.h3.a["href"]
            if media_link.startswith(('http://', 'https://')):
                m_link = media_link
            else:
                m_link = url + media_link
        except Exception as e:
            m_link = None

        try:
            media_content = requests.get(m_link).text
            m_soup = BeautifulSoup(media_content, 'lxml')

            m_content = m_soup.find('article').text.strip()

        except Exception as e:
            m_content = None

        print("Title: ", m_title)
        print("URL: ", m_link)
        print("Content: ", m_content)

        print()

    # print(soup.prettify())
  # print(soup.get_text())
get_content("https://www.bbc.com")
