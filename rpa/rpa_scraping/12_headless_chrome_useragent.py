from selenium import webdriver


# 크롬을 백그라운드에서 실행
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")
options.add_argument("user-agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")


browser = webdriver.Chrome('./personal_thing/chromedriver', options=options)
browser.maximize_window() # 창 최대화

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()
