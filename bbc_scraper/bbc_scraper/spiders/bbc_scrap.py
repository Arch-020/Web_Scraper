import scrapy
from bs4 import BeautifulSoup


class BbcSpider(scrapy.Spider):
    name = 'bbc'
    start_urls = ['https://www.bbc.com']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        media_contents = soup.find_all('div', class_="media__content")

        for content in media_contents:
            m_title = content.h3.text.strip()
            #media_link = content.h3.a["href"]
            #media_summary = content.p.text

            try:
                media_link = content.h3.a["href"]
                if media_link.startswith(('http://', 'https://')):
                    m_link = media_link
                else:
                    url = "https://www.bbc.com"
                    m_link = url + media_link
            except Exception as e:
                m_link = None

            try:

                m_content = content.p.text.strip()

            except Exception as e:
                m_content = None

            yield {

                "Title: ": m_title,
                "URL: ": m_link,
                "Content: ":  m_content,


            }
