from selenium import webdriver
import time

driver_path = "/home/x/Downloads/chromedriver"

time.sleep(3) # 5 Saniye bekle
browser = webdriver.Chrome(driver_path)
browser.get("https://google.com") # Bu url i aç
time.sleep(5) 

# inputElement = driver.find_element_by_class_name("vdLsw gsfi")
# inputElement.send_keys('Youtube')
# time.sleep(3)
# inputElement.send_keys(Keys.ENTER)

browser.get("https://youtube.com") 
time.sleep(5) 
print("Site Başlığı = ", browser.title) # Site Başlığını Yazdır
print("-------------------------------------------------------")
print(browser.current_url) # Şuanki url yi yazdır
print("-------------------------------------------------------")
print(browser.page_source) # Sitenin kaynak kodlarını yazdır
print("-------------------------------------------------------")

# browser.refresh() # Yenile

browser.get("https://www.youtube.com/channel/UCPJJbWeR2r1Rs_FWQhsPaFw?view_as=subscriber")
print("Site Başlığı = ", browser.title) # Site Başlığını Yazdır
browser.maximize_window() # Pencereyi max boyuta getir
time.sleep(5) 
browser.save_screenshot("/home/x/Desktop/ScreenShot") # Ekran Görüntüsü Al Masaüstüne Kaydet
time.sleep(5) 
browser.get("https://www.frknyldz.com") 
time.sleep(5) 

browser.quit() # Kapat