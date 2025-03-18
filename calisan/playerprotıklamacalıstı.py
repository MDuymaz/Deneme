from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Başsız modda Chrome ayarlarını yapma
chrome_options = Options()
chrome_options.add_argument("--headless")  # Başsız modda çalıştır
chrome_options.add_argument("--no-sandbox")  # GitHub Actions ortamı için güvenlik ayarı
chrome_options.add_argument("--disable-dev-shm-usage")  # GitHub Actions ortamı için performans ayarı

# ChromeDriver'ı başlatma
driver = webdriver.Chrome(options=chrome_options)

# Web sayfasına gitme ve etkileşim
driver.get('https://playerpro.live/')

# Burada verilerinizi almanız gerekiyor, örneğin bir dosyadan okuma
# data, ana_link, ana_link gibi veriler bir dosyadan okunabilir
with open("datam3u.txt", "r") as file:
    data = file.read()

with open("ana_link.txt", "r") as file:
    ana_link = file.read()

with open("ana_link.txt", "r") as file:
    ana_link = file.read()

# HTML elemanlarına erişip formu dolduruyoruz
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/form/div[1]/input').send_keys(data)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/form/div[2]/input').send_keys(ana_link)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/form/div[3]/input').send_keys(ana_link)

# Buton üzerinde tıklama işlemi yapmak için ActionChains kullanıyoruz
button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/form/button')
actions = ActionChains(driver)
actions.move_to_element(button).click().perform()

# Sonuçları almak için sayfanın kaynak kodunu al
page_source = driver.page_source
print(page_source)

# Tarayıcıyı kapatma
driver.quit()
