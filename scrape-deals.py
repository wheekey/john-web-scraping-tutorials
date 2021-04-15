import smtplib

import requests
from bs4 import BeautifulSoup

def get_price(url):
    proxyDict = {
        "https": "178.62.94.185:3128",
    }
    r = requests.get(url, proxies=proxyDict)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span', {'itemprop': 'price'})['content']
    return price

def add_prices(p1, p2, p3):
    total = (float(p1) + float(p2) + float(p3))
    return total

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    server.login('yourgmail@gmail.com', 'passwd')
    subject = 'price today'
    body = f'total {total_price}'
    message = f'Subject:{subject}\n\n\n{body}'
    server.sendmail('emailfrom@gmail.com', 'email_to@gmail.com', message)
    print('Email sent')
    server.quit()

cpu = get_price('link1')
motherboard = get_price('link2')
ram = get_price('link3')

total_price = add_prices(cpu, motherboard, ram)
send_mail()