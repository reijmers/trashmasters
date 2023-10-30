from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.pbl.nl/en/topics/circular-economy/publications"
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


publications = soup.find_all("div", class_="node-title")
dates = soup.find_all("div", class_="meta")
findings = soup.find_all("div", class_="field-items")


publication_data = []


for publication, date, finding in zip(publications, dates, findings):
    title = publication.a.text.strip()
    pub_date = date.find("span", class_="date-display-single").text.strip()
    finding_text = finding.text.strip()
        
    publication_data.append({'Title': title, 'Publication Date': pub_date, 'Findings': finding_text})

df = pd.DataFrame(publication_data)

print(df)

df.to_csv('publications.csv', index=False)