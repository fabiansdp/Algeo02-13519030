import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.jawapos.com/ekonomi/finance/12/11/2020/fintech-hadir-literasi-dan-inklusi-keuangan-nasional-perlu-diperkuat/")

print(r.status_code)


soup = BeautifulSoup(r.text, "html.parser")
article = soup.find_all('p', text=True)

scrape = "."
for each in article: 
    scrape += str(each.get_text())

print(scrape)
