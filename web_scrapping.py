import requests
from bs4 import BeautifulSoup

url = """https://finance.yahoo.com/quote/%5EDJI"""
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    header_info = soup.find('div', id='quote-header-info')
    streamer=header_info.find_all("fin-streamer")
    values = [i.text for i in streamer if i!=""]
    date_time=header_info.find("div",id="quote-market-notice").find("span").text
    print(values,date_time)
else:
    print("Not Found")