import requests
from bs4 import BeautifulSoup
import lxml,smtplib
#The product is motorola edge 40 neo and the current price is 23999 and target is 21999
TARGET = 24999.0
URL = "https://www.amazon.in/Motorola-Edge-Neo-Soothing-Sea/dp/B0CK63FY9S/ref=sr_1_1?dib=eyJ2IjoiMSJ9.yh11JB6xXEiOEmhZTYCY5L3qwaMZaZsKMxBPjMHFDItbNDIUR_6zMmO5YSQQgaBhhx-B05UjjxNlkvuj0OIZkngrt-s2Byro-50qgcJ6vmW2P8F1K1ax_YKzxtzvrTweWFT4yv2Ev8gSPXzOdeQn5d-c2SzTtd3oKPlvh9LsOygy0RclsMV7lbk3sLIM9RqkVE6lAmUZE-JAVfuehDc3EQR_FL_BP9Ha6cSIgz_XV3o.AdNFfS_StHjEmAnZcLMUXRbkXEJxIQ7Ge6G6I7HhYcs&dib_tag=se&keywords=moto+edge+40+neo&qid=1713591203&sr=8-1"
header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(URL,headers = header)
content = response.text
soup = BeautifulSoup(content,"lxml")
price = soup.find(name = "span", class_="a-price-whole")
price_str = price.getText()
s=''
for i in price_str:
    if i.isdigit():
        s += i
current_price = float(s)
if current_price <= TARGET:
    my_email = "apashyamkirikiri849@gmail.com"
    password = "bqsiwpqrnninvoww"
    recipient_email = "alpinekamande@gmail.com"
    try:
        connection = smtplib.SMTP("smtp.gmail.com",587)# port is must
        connection.starttls()
        connection.login(user=my_email, password=password)
        subject = "Amazon Price drop alert"
        message = "Your product motorola edge 40 neo price was dropped.Check it out."
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"{subject} \n \n {message} \n.".encode("utf-8"))
        print("email sent successfully")
    except Exception as e:
        print(e)