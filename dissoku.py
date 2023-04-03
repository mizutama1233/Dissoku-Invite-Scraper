from bs4 import BeautifulSoup
import requests
h = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 Chrome/109.0.0.0 Safari/537.36'
}
for i in range(134):
    r = requests.get(f'https://dissoku.net/ja/servers?page={i}', headers=h).text
    al = BeautifulSoup(r, 'html.parser').find_all('a', class_ = "join-btn")
    for link in al:
        url = requests.get(link.get("href") + "/", headers=h, allow_redirects=False)
        location = url.headers.get('location')
        if location != None:
            print(location)