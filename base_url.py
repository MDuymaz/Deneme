from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

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

# base_url.txt dosyasını oku ve mevcut baseurl ile karşılaştır
base_url_file_path = 'base_url.txt'

# Eğer base_url.txt dosyası varsa, mevcut baseurl'i oku
if os.path.exists(base_url_file_path):
    with open(base_url_file_path, 'r', encoding='utf-8') as file:
        current_baseurl = file.read().strip()
else:
    current_baseurl = ""

# baseurl, dosyadaki mevcut baseurl ile aynı olsa bile dosyaya yazmaya devam et
try:
    # Dosyayı yazma işlemi
    with open(base_url_file_path, 'w', encoding='utf-8') as file:
        file.write(baseurl)
    print("Base URL yazıldı.")
except Exception as e:
    print(f"Base URL yazılırken bir hata oluştu: {e}")

# Tarayıcıyı kapat
driver.quit()
