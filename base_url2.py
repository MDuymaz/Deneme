from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.add_argument("--headless")  # Başsız (headless) modda çalıştırmak için
chrome_options.add_argument("--no-sandbox")  # Sandbox kullanmamak
chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm kullanımını engelle

# Tarayıcıyı başlatmak için gerekli path ve driver'ı ayarla
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Sayfayı aç
url = "https://trgoals1235.xyz//channel.html?id=yayin1"
driver.get(url)

# Sayfanın tamamen yüklenmesi için bir süre bekle
time.sleep(5)

# JavaScript ile tanımlanmış olan baseurl değişkenini almak
baseurl = driver.execute_script("return baseurl;")

# baseurl'i yazdır
print("Base URL:", baseurl)

# baseurl değerini base_url.txt dosyasına yaz
with open("base_url.txt", "w", encoding="utf-8") as file:
    file.write(baseurl)

# Tarayıcıyı kapat
driver.quit()
