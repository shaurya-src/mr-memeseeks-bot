from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from subprocess import call

# >>>>>>>>>>>>>>>>>>>> EXTRACT CREDENTIALS <<<<<<<<<<<<<<<<<<<<


with open("E:\Python Projects\Meme Bot\Assets\cred_insta","r") as ig_cred:
    ig_id = ig_cred.readline()
    ig_pwd = ig_cred.readline()


# driver setup
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36")
opts.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opts)

# open instagram
def openinsta():
    driver.get('https://m.instagram.com/')
    sleep(2)

# login using dynamic xpath
def xlogin(uid,pwd):
    driver.find_element_by_xpath('//button[contains(text(),"Log")]').click()
    sleep(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(uid)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(pwd)
    sleep(1)
    driver.find_element_by_xpath('//div[text()="Log In"]').click()
    sleep(5)
    driver.find_element_by_xpath('//button[text()="Not Now"]').click()     # don't save pass
    sleep(3)
    driver.find_element_by_xpath('//button[text()="Cancel"]').click()    # cancel home-screen
    sleep(4)



# driver login
openinsta()
xlogin('bot_meme6','incarnatebot!!!')

# driver upload
upload_button = driver.find_element_by_xpath('//div[@data-testid="new-post-button"]')
upload_button.click()

# run AutoIT script
call('E:\Python Projects\Meme Bot\AutoIT\FileUpload.exe')
sleep(2)

# after img is selected
def memeup(cpt):
    driver.find_element_by_xpath('//button[text()="Next"]').click()
    sleep(2)
    driver.find_element_by_xpath('//textarea').send_keys(cpt)
    driver.find_element_by_xpath('//button[text()="Share"]').click()
    sleep(8)

# add caption and upload
memeup('caption')

# remove notification dialog box
driver.find_element_by_xpath('//button[text()="Not Now"]').click()
sleep(15)

# complete execution
driver.quit()