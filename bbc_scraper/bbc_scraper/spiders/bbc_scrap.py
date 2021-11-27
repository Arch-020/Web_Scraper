import scrapy
from bs4 import BeautifulSoup


class BbcSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ["www.bbc.com"]
    start_urls = ['https://www.bbc.com']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        media_contents = soup.find_all('div', class_="media__content")

        for content in media_contents:

            try:
                media_link = content.h3.a["href"]
                if media_link.startswith(('http://', 'https://')):
                    media_link = media_link

                else:
                    url = "https://www.bbc.com"
                    media_link = url + media_link

            except Exception as e:
                media_link = None

            try:

                url = response.urljoin(media_link)

                yield scrapy.Request(url, callback=self.parse_dir_contents)

            except Exception as e:
                continue

    def parse_dir_contents(self, response):

        m_soup = BeautifulSoup(response.body, 'lxml')
        data = {}
        media_title = m_soup.title.get_text()
        data['Title'] = media_title
        #print("Title: ", med_title)

        m_link = m_soup.find('meta', property="og:url")
        data['URL'] = m_link
        # print(med_link)

        m_content = m_soup.find('article').text.strip()
        data['Content'] = m_content
        #print("Content: ", m_content)

        yield data
