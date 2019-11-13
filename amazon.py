import requests
from bs4 import BeautifulSoup
import smtplib
URL='https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B07S8CZCMC/ref=sr_1_5?crid=TOK1C45FLFG8&keywords=macbook+pro+13+inch&qid=1573630022&sprefix=mac%2Caps%2C506&sr=8-5'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
def checck_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    a=(price[2:6])
    converted_price=float((a.translate({ord(','): None})))
    if(converted_price<150.0):
        send_mail()
    print(converted_price)
    print(title.strip())
    if(converted_price<150.0):
        send_mail()
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('kuttythomas00@gmail.com','password')
    subject='Price Fell down!'
    body='check the link https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B07S8CZCMC/ref=sr_1_5?crid=TOK1C45FLFG8&keywords=macbook+pro+13+inch&qid=1573630022&sprefix=mac%2Caps%2C506&sr=8-5'
    
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'kuttythomas00@gmail.com',
        'kuttythomas01@gmail.com',
         msg

    )
    print('email has been sent')
    server.quit()