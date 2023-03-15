from selenium import webdriver
import requests

# Chrome tarayıcısının sürüm numarasını al
version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
response = requests.get(version_url)
chrome_version = response.text.strip()

# ChromeDriver'ın indirme URL'sini oluştur
driver_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip"

# ChromeDriver'ı indir ve ayıkla
response = requests.get(driver_url)
with open("chromedriver_win32.zip", "wb") as f:
    f.write(response.content)
    
import zipfile
with zipfile.ZipFile("chromedriver_win32.zip", "r") as zip_ref:
    zip_ref.extractall(".")
    
# Driver'ı başlat
driver = webdriver.Chrome()
