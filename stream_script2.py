import requests

# 'datam3u.txt' dosyasından M3U8 linkini al
with open('datam3u.txt', 'r') as file:
    m3u8_link = file.readline().strip()  # M3U8 linki

# 'ana_link.txt' dosyasından Referer ve Origin değerlerini al
with open('ana_link.txt', 'r') as file:
    referer = file.readline().strip()  # Referer
    origin = file.readline().strip()   # Origin

# Siteye POST isteği göndermek için URL ve form verileri
url = "https://playerpro.live/"
data = {
    'm3u8_link': m3u8_link,
    'referer': referer,
    'origin': origin
}

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Proxy kullanıyorsanız, aşağıdaki gibi proxy ayarlarını ekleyebilirsiniz:
# proxies = {
#     'http': 'http://proxy_address:proxy_port',
#     'https': 'http://proxy_address:proxy_port',
# }

# POST isteği gönder
response = requests.post(url, data=data, headers=headers)

# Sonuç kontrolü
if response.ok:
    print("Stream başarılı bir şekilde başlatıldı.")
else:
    print("Hata oluştu:", response.status_code)
