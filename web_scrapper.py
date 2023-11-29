import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # URL of the website to scrape
    url = ''

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data (quotes and authors in this case)
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')

        # Print the scraped data
        for quote, author in zip(quotes, authors):
            print(f"{quote.text.strip()} - {author.text.strip()}")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()
