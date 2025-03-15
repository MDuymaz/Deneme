import requests
from bs4 import BeautifulSoup

# Web sayfasının URL'sini belirle
url = 'https://www.ornekwebsite.com'

# HTML içeriğini al
response = requests.get(url)

# İstek başarılı ise içeriği işleme
if response.status_code == 200:
    # Web sayfasının HTML içeriğini al
    content = response.text

    # BeautifulSoup ile HTML'yi çözümle
    soup = BeautifulSoup(content, 'html.parser')

    # m3u8 uzantılı linkleri bul
    m3u8_links = []
    for link in soup.find_all('a', href=True):
        if 'workers' in link['href']:
            m3u8_links.append(link['href'])

    # Linkleri bir TXT dosyasına yaz
    with open('m3u8_links.txt', 'w', encoding='utf-8') as file:
        for m3u8_link in m3u8_links:
            file.write(m3u8_link + '\n')
    
    print("m3u8 linkleri başarıyla txt dosyasına yazıldı.")
else:
    print("Web sayfasına erişilemedi:", response.status_code)
