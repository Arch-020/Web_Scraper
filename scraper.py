
import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url, timeout=5).text
    soup = BeautifulSoup(response, 'lxml')
    return soup


def parse_page(soup):
    results = {}
    page_title = soup.title.get_text()
    print("Page Title: ", page_title)
    for link in soup.find_all("a"):
        try:
            results[link['href']] = link.text.strip()
        except:
            continue
    return results


def visit(url):
    try:
        soup = fetch_page(url)
    except:
        print(f"Cannot fetch {url}")
        return {}
    return parse_page(soup)


def crawl(seed_url, MAX_URLS=100):
    frontier = {}
    visited = {}

    frontier[seed_url] = ""

    while len(frontier) > 0 and len(visited) < MAX_URLS:
        url, _ = frontier.popitem()
        print(f"Visiting {url}")
        new_urls = visit(url)
        print(
            f"Total {len(new_urls)} discovered, fronter size is {len(frontier)}, pages visited {len(visited)}")
        for candidate_url, _ in new_urls.items():
            if candidate_url not in visited:
                if candidate_url[0] == "/":
                    candidate_url = f"{seed_url}{candidate_url}"
                frontier[candidate_url] = ""
        visited[url] = ""

    with open("url.txt", "w") as output:
        for current in visited:
            output.write(current + "\n")


if __name__ == "__main__":
    crawl("https://www.bbc.com")
