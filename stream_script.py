from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 'datam3u.txt' dosyasından M3U8 linkini al
with open('datam3u.txt', 'r') as file:
    m3u8_link = file.readline().strip()  # M3U8 linki

# 'ana_link.txt' dosyasından Referer ve Origin değerlerini al
with open('ana_link.txt', 'r') as file:
    referer = file.readline().strip()  # Referer
    origin = file.readline().strip()   # Origin

# Selenium için Chrome WebDriver başlatma
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Tarayıcıyı arka planda çalıştırmak için
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# PlayerPro live sitesine git
url = "https://playerpro.live/"
driver.get(url)

# Sayfa tamamen yüklendikten sonra (gerekirse zaman tanıyın)
time.sleep(5)  # Sayfanın yüklenmesi için 5 saniye bekle

# Formu bulup verileri gönder
m3u8_input = driver.find_element(By.NAME, 'm3u8_link')  # M3U8 linki input alanını bul
referer_input = driver.find_element(By.NAME, 'referer')  # Referer input alanını bul
origin_input = driver.find_element(By.NAME, 'origin')    # Origin input alanını bul

# Gerekli verileri inputlara yaz
m3u8_input.send_keys(m3u8_link)
referer_input.send_keys(referer)
origin_input.send_keys(origin)

# Submit butonuna basarak formu gönder
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Butonun xpath'ini bul
submit_button.click()

# Sayfa yanıtının yüklenmesini bekle
time.sleep(5)

# Sonuç sayfasının HTML içeriğini al
html_content = driver.page_source

# HTML içeriğini 'data.html' dosyasına yaz
with open('data.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# Tarayıcıyı kapat
driver.quit()

print("HTML başarıyla 'data.html' dosyasına yazdırıldı.")
