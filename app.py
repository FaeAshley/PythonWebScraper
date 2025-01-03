import requests
from bs4 import BeautifulSoup


def get_request():
    url = "https://quotes.toscrape.com/"
    r = requests.get(url=url)

    soup = BeautifulSoup(r.content, 'html.parser')
    quotes = []

    rows = soup.find_all('div', class_='row')

    parent_div = rows[1]
    target_div = parent_div.find('div', class_='col-md-8')

    for row in target_div.find_all('div', attrs={'class': 'quote'}):
        quote = {}
        quote['text'] = row.find('span', class_='text').text
        quote['author'] = row.find('small', class_='author').text
        quote['tags'] = [tag.text for tag in row.find('div', class_='tags').find_all('a', class_='tag')]
        quotes.append(quote)

    print(quotes)


def main():
    get_request()


if __name__ == "__main__":
    main()