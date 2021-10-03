from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import requests
import time 

x = 'y'

url = 'https://www.worldometers.info/coronavirus/'

#Code Part ---------------------------
while  x == 'y':
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    x = soup.find('div', {"class":"maincounter-number"})
    print(str(x))

    toast = ToastNotifier()

    toast.show_toast("Covid Prevention","In total " + x + "people have been infected by Covid-19; So put on your mask",duration=5,icon_path="Covid Prevention\Covid.ico")
    time.sleep(5)