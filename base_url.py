import requests
from bs4 import BeautifulSoup

# Hedef URL
url = "https://trgoals1234.xyz/"

# URL'den HTML içeriğini çek
response = requests.get(url)

# Eğer istek başarılı olduysa
if response.status_code == 200:
    # HTML içeriğini parse et
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # HTML'yi güzel bir formatta alın
    pretty_html = soup.prettify()
    
    # Dosyaya yaz
    with open("base_url.html", "w", encoding="utf-8") as file:
        file.write(pretty_html)
    
    print("HTML içeriği 'base_url.html' dosyasına yazıldı.")
else:
    print("Hata:", response.status_code)
