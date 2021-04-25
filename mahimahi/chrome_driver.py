import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PROXY = "172.0.0.1:8889"
timeout_LOG_FILE = 'timeout.log'
bitrate_LOG_FILE = 'bitrate.log'
ssim_LOG_FILE = 'ssim_db.log'
chrome_user_dir = '/home/yinwenpei/data_save/chrome_data'
os.system("rm -rf " + chrome_user_dir)
os.system("mkdir " + chrome_user_dir)
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server={0}'.format(PROXY))
options.add_argument('--user-data-dir=' + chrome_user_dir)
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('/home/yinwenpei/data_save/chromedriver', chrome_options=options)

driver.get("http://100.64.0.1:8080")
#driver.get("http://127.0.0.1:8080")

log_in_button = driver.find_element_by_xpath("/html/body/div/div/div[3]/a[2]")
log_in_button.click()

login_user = driver.find_element_by_xpath("/html/body/div/form/div[1]/div/input")
login_user.send_keys("qianqianzi")
login_pwd = driver.find_element_by_xpath("/html/body/div[1]/form/div[2]/div/input")
login_pwd.send_keys("qianqianzi0701")
In_USA = driver.find_element_by_xpath('/html/body/div/form/div[3]/label')
In_USA.click()
log_in_button2 = driver.find_element_by_xpath("/html/body/div/form/div[4]/button")
log_in_button2.click()
last_bit_rate = 0.0
bitrate_list = []
last_ssim_db = 0.0
ssim_db_list = []
# get real bitrate of video
#os.system("gedit bitrate.log")
while(True):
    bit_rate = driver.find_element_by_xpath('//*[@id="video-bitrate"]')
    ssim_db = driver.find_element_by_xpath('//*[@id="video-ssim"]')
    error_xpath = driver.find_element_by_xpath('//*[@id="player-error-list"]')
    try:
        real_bit_rate = float(bit_rate.get_attribute("innerText"))
        real_ssim_db = float(ssim_db.get_attribute("innerText"))
        # inspect error
        error_info = error_xpath.get_attribute("innerText")
    except:
        continue
    if(error_info):
        print(error_info)
        driver.refresh()
        with open(timeout_LOG_FILE, mode='a') as f3:
            f3.writelines(error_info)
            f3.writelines('\n')

    if(last_bit_rate != real_bit_rate):
        bitrate_list.append(real_bit_rate)
        last_bit_rate = real_bit_rate
        print(real_bit_rate)
        with open(bitrate_LOG_FILE,mode = 'a') as f:
            f.writelines(str(real_bit_rate))
            f.writelines('\n')
    if(last_ssim_db != real_ssim_db):
        ssim_db_list.append(real_ssim_db)
        last_ssim_db = real_ssim_db
        with open(ssim_LOG_FILE, mode='a') as f2:
            f2.writelines(str(real_ssim_db))
            f2.writelines('\n')




# qianqianzi
# qianqianzi0701
# driver.get("https://baidu.com")
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# time.sleep(5)
# browser.quit()
#print("hello")
# driver.get("https://www.baidu.com/")
