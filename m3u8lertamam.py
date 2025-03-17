import re
import requests
from urllib.parse import urlparse, parse_qs

# Sayfa URL'si
page_url = "https://main.uxsyplayerd22c8f9c2ba8.click/index.php?id=selcukbeinsports2"

# User-Agent ekleyerek isteği yap (Bazı siteler botları engelliyor)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Sayfanın kaynak kodunu al
response = requests.get(page_url, headers=headers)

# Eğer istekte hata varsa
if response.status_code != 200:
    print("Sayfa yüklenemedi!")
    exit()

# Sayfa içeriğini al
html_content = response.text

# baseStreamUrl'yi bul
match = re.search(r"this\.baseStreamUrl\s*=\s*['\"](.*?)['\"]", html_content)
if match:
    base_stream_url = match.group(1)
else:
    print("Base stream URL bulunamadı!")
    exit()

# Sayfadaki ID'yi al
parsed_url = urlparse(page_url)
query_params = parse_qs(parsed_url.query)
stream_id = query_params.get("id", ["selcukbeinsports1"])[0]  # Varsayılan ID

# m3u8 bağlantısını oluştur
m3u8_url = f"{base_stream_url}{stream_id}/playlist.m3u8"
print("m3u8 URL:", m3u8_url)
