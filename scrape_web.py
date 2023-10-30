import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the webpage
url = "https://www.pbl.nl/en/topics/circular-economy/publications"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section or element that contains the publications
    # You may need to inspect the webpage source to identify the correct HTML structure
    publications_section = soup.find('section', {'class': 'publication-list'})

    # Iterate through the list of publications and extract the information you need
    for publication in publications_section.find_all('article', {'class': 'publication'}):
        title = publication.find('h3', {'class': 'publication-title'}).text
        date = publication.find('time', {'class': 'publication-date'}).text
        link = publication.find('a', {'class': 'publication-link'})['href']

        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Link: {url}{link}\n")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
