import BeautifulSoup
import requests

url = 'https://www.example.com = requests.get(url)
url_content = r.content
soup = BeautifulSoup(url_content, 'html.parser')
tab = soup.find("table", {"class": "ct-data_table tr-data_table tr-tableStyle"})
print(tab)
