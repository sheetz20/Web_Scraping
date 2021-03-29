import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

csv_file = open("C://Users/sheetal/Desktop/python_projects/rating.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['MovieName','Rating'])
# print(soup.prettify())


for movieTitle in soup.find_all('td',class_="titleColumn"):
    movieName = movieTitle.a.text
    print(movieName)
    csv_writer.writerow([movieName])

for rating in soup.find_all('td',class_="ratingColumn imdbRating"):
    movieRating = rating.text.strip()
    print(movieRating)
    # csv_writer.writerow([movieRating])

csv_file.close()
