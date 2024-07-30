import httpx
from bs4 import BeautifulSoup


def extract_font_urls(page_url: str = "https://www.nerdfonts.com/font-downloads") -> set[str]:
    response = httpx.get(page_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    font_urls = set()

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".zip"):
            font_urls.add(href)

    return font_urls
