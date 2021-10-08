from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import requests
import time 

#Code Part ---------------------------
for _ in range(99999):
    url = 'https://www.worldometers.info/coronavirus/'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    x = soup.find('div', {"class":"maincounter-number"}).getText()

    toast = ToastNotifier()
    toast.show_toast("Covid Prevention","In total" + x + "people have been infected by Covid-19, So put on your mask" ,duration=10)
    time.sleep(3000)
