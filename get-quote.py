
#Created a random quote generator, and send it using email.
# Web scraping implemented using BeautifulSoup

import requests, random
from bs4 import BeautifulSoup

import smtplib
def random_quote(url):
    conn = requests.get(url)
    soup = BeautifulSoup(conn.content,'html.parser')
    quotes = soup.find_all('a', attrs={"title": "view quote"})
    quotesList = []
    for quote in quotes:
        quotesList.append(quote.text)

    num = random.randint(0,len(quotesList))
    your_quote = 'Here is Your Quote:\n"'+quotesList[num]+'"'
    return(print(your_quote))

def send_email(mail):
    
    sender = input("Enter Sender's Email ID:")
    passwd = input("Enter Sender's Password:") 
   
    
    reciever = input("Enter Reciever's Email ID:")
    
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    server.ehlo()
    server.login(sender,passwd)
    server.sendmail(sender,reciever,mail)
    print("Mail Sent Successfully!")


msg = random_quote('https://www.brainyquote.com/topics/inspirational-quotes')
mail = f'Subject: "Quote Of The Day"\n\n{msg}'
send_email(mail)
