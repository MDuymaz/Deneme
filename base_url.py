from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome seçeneklerini ayarla
chrome_options = Options()

# User data directory ile ilgili hatayı engellemek için --no-sandbox ve --disable-dev-shm-usage ekleyelim
chrome_options.add_argument("--no-sandbox")  # Sandbox kullanmamak
chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm kullanımını engelle

# Başsız (headless) modda çalıştırmak isterseniz
chrome_options.add_argument("--headless")  # GUI'siz modda çalıştır

# Tarayıcıyı başlatmak için gerekli path ve driver'ı ayarla
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Sayfayı aç
url = "https://trgoals1235.xyz/"
driver.get(url)

# Sayfanın tamamen yüklenmesi için bir süre bekle
time.sleep(5)

# Sayfanın HTML içeriğini al
html_content = driver.page_source

# 'baseurl' kelimesini ara
if "baseurl" in html_content:
    print("HTML içinde 'baseurl' kelimesi bulundu.")
    
    # HTML içeriğini base_url.txt dosyasına yazdır
    with open("base_url.txt", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML içeriği base_url.txt dosyasına yazıldı.")
else:
    print("HTML içinde 'baseurl' kelimesi bulunamadı.")

# Tarayıcıyı kapat
driver.quit()
