from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Sayfayı aç
driver.get("https://playerpro.live/")

# Sayfa yüklenene kadar bekle
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'm3u8_link')))

# Gerekli form verilerini gir
m3u8_input = driver.find_element(By.NAME, 'm3u8_link')
referer_input = driver.find_element(By.NAME, 'referer')
origin_input = driver.find_element(By.NAME, 'origin')

# M3U8 linki, Referer, ve Origin değerlerini gir
m3u8_input.send_keys("your_m3u8_link_here")
referer_input.send_keys("your_referer_here")
origin_input.send_keys("your_origin_here")

# Submit butonunu bul ve tıklanabilir olmasını bekle
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)

# Sayfayı kaydırarak butonu görünür yap
driver.execute_script("arguments[0].scrollIntoView();", submit_button)

# Submit butonuna tıkla
submit_button.click()

# Sayfa yanıtının yüklenmesini bekle
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# HTML içeriğini al ve yazdır
html_content = driver.page_source

with open('data.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# Tarayıcıyı kapat
driver.quit()

print("HTML başarıyla 'data.html' dosyasına yazdırıldı.")
