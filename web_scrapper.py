import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Make a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the links on the page and print their titles
            links = soup.find_all('a')
            for link in links:
                title = link.get('title', 'No Title')
                print(f"Link Title: {title}")

        else:
            print(f"Error: Unable to fetch the page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the user input for the URL
    url = input("Enter the URL to scrape: ")

    # Call the scrape_website function with the user-provided URL
    scrape_website(url)
