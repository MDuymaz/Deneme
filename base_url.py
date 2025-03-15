import requests

# URL'yi tanımla
url = "https://trgoals1235.xyz/"

# Siteye istek gönder
response = requests.get(url)

# İstek başarılıysa, HTML içeriğini kontrol et
if response.status_code == 200:
    html_content = response.text

    # HTML içinde 'workers' kelimesini ara
    if "workers" in html_content:
        print("HTML içinde 'workers' kelimesi bulundu.")
        
        # HTML içeriğini base_url.txt dosyasına yazdır
        with open("base_url.txt", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("HTML içeriği base_url.txt dosyasına yazıldı.")
    else:
        print("HTML içinde 'workers' kelimesi bulunamadı.")
else:
    print(f"Siteye erişilemedi. HTTP Durum Kodu: {response.status_code}")
