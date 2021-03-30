import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

csv_file = open("C://Users/sheetal/Desktop/WebScrapingProjects/rating.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['MovieName','Rating'])
# print(soup.prettify())

movieList = []
ratingList = []

for movieTitle in soup.find_all('td',class_="titleColumn"):
    movieName = movieTitle.a.text
    movieList.append(movieName)

for rating in soup.find_all('td',class_="ratingColumn imdbRating"):
    movieRating = rating.text.strip()
    ratingList.append(movieRating)

for name, rating in zip(movieList,ratingList):
    csv_writer.writerow([name,rating])

csv_file.close()
