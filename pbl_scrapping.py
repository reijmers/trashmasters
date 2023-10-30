from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.pbl.nl/en/topics/circular-economy/publications"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

publications = soup.find_all("article", class_="node-publicatie")
publication_data = []

for article in publications:
    title = article.find("h2", class_ = "node-title").text.strip()

    findings = article.find("div", class_ = "field-item").text.strip()

    date_div = article.find("div", class_="meta")
    date= date_div.get_text(strip=True)
    date_1 = date.split('|')
    date = date_1[0].strip()

    publication_data.append({'Title': title, 'Publication Date': date, 'Findings': findings})

df = pd.DataFrame(publication_data)

print(df)

df.to_csv('publications.csv', index=False)