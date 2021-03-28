import requests
from bs4 import BeautifulSoup
import smtplib
import os
import time

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

url = "https://www.flipkart.com/poco-m3-cool-blue-64-gb/p/itmc8ec867cb0472?pid=MOBFZTCUDDCTDN3G&lid=LSTMOBFZTCUDDCTDN3GBY0LIO&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_banner_2_9.bannerX3.BANNER_mobile-phones-store_Q46MFY7ACZJT&fm=neo%2Fmerchandising&iid=02e614a7-b5c3-4c1f-a46e-fc4fa6659ccb.MOBFZTCUDDCTDN3G.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=zhqmv3bsk00000001616921491579"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

title = soup.find(class_='B_NuCI').get_text()

price = soup.find(class_="_25b18c").get_text()
convertedPrice = float(price[1:7].replace(",",""))

print(title)
print(convertedPrice)

def checkPrice():
    if(convertedPrice < 12000):
        sendMail()


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject = "Price Drop Alert!"
    body = "Check out the Link https://www.flipkart.com/poco-m3-cool-blue-64-gb/p/itmc8ec867cb0472?pid=MOBFZTCUDDCTDN3G&lid=LSTMOBFZTCUDDCTDN3GBY0LIO&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_banner_2_9.bannerX3.BANNER_mobile-phones-store_Q46MFY7ACZJT&fm=neo%2Fmerchandising&iid=02e614a7-b5c3-4c1f-a46e-fc4fa6659ccb.MOBFZTCUDDCTDN3G.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=zhqmv3bsk00000001616921491579"

    msg = f"subject: {subject}\n\n{body}"
    server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)
    print("Email has been sent!")
    server.quit()

if __name__ == "__main__":
    while True:
        checkPrice()
        time.sleep(60*60)