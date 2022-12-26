from selenium import webdriver
import time
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options


# 원하는 위치에 파일 다운로드 하기
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory' : r'/Users/mokjaemin/Desktop/pythonfile'})



browser = webdriver.Chrome("./chromedriver", options = chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# 다운로드 링크를 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

browser.switch_to.default_content()


time.sleep(5)

browser.quit()
