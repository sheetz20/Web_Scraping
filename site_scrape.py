import requests
from bs4 import BeautifulSoup
import csv

url = "http://coreyms.com"

page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

csv_file = open('C://Users/sheetal/Desktop/python_projects/cms_scraper.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

# print(soup.prettify())

for article in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.div.p.text
    print(headline)
    print(summary)
    for vdo_src in article.find_all('iframe', class_="youtube-player"):
        vdo_id = vdo_src['src'].split("/")[4].split("?")[0]
        vdo_link = f"https://youtube.com/watch?v={vdo_id}"
        print(vdo_link)

    print()

    csv_writer.writerow([headline,summary,vdo_link])

csv_file.close()