from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Scan QR code di WhatsApp Web, lalu tekan Enter...")

nomor = "6282221222753"  
pesan = "121w1w1wdssfd"
jumlah = 30

for i in range(jumlah):
    driver.get(f"https://web.whatsapp.com/send?phone={nomor}")
    time.sleep(8)
    kotak = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    kotak.send_keys(pesan + f" #{i+1}")
    kotak.send_keys(Keys.ENTER)
    time.sleep(2)
    print(f"Pesan ke-{i+1} dikirim")

driver.quit()