import requests
from bs4 import BeautifulSoup
import csv

url = "https://thegirlnextdoorword.wordpress.com/"

page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')

# print(soup.prettify())
file_name = open("C://Users/sheetal/Desktop/WebScrapingProjects/articles.csv",'w')
csv_writer = csv.writer(file_name)
csv_writer.writerow(['Heading','Article'])


for article in soup.find_all('article'):
    heading = article.header.text
    content = article.find('div', class_="post-content clear").text.strip()
    csv_writer.writerow([heading,content])
    print(heading)
    print(content)
    print()

file_name.close()