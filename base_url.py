from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Chrome seçeneklerini ayarla
chrome_options = Options()

# Farklı bir kullanıcı veri dizini kullan
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data")  # Geçici bir dizin oluşturulabilir

# WebDriver'ı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Sayfayı aç
url = "https://trgoals1235.xyz/"
driver.get(url)

# Sayfanın tamamen yüklenmesi için bir süre bekle
time.sleep(5)

# Sayfanın HTML içeriğini al
html_content = driver.page_source

# 'workers' kelimesini ara
if "workers" in html_content:
    print("HTML içinde 'workers' kelimesi bulundu.")
    
    # HTML içeriğini base_url.txt dosyasına yazdır
    with open("base_url.txt", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML içeriği base_url.txt dosyasına yazıldı.")
else:
    print("HTML içinde 'workers' kelimesi bulunamadı.")

# Tarayıcıyı kapat
driver.quit()
