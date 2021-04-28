import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

instagram_id = "ch.ium"
instagram_pw = "1q2w3e4r!"

followers = []
following = []


driver = webdriver.Chrome(
    '/Users/dain/Downloads/chromedriver')

# 3초 지연
driver.implicitly_wait(3)
driver.get('https://www.instagram.com/accounts/login/')

# 로그인
driver.find_element_by_name('username').send_keys(instagram_id)
driver.find_element_by_name('password').send_keys(instagram_pw)

driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div[1]/div[3]/button').click()

driver.implicitly_wait(3)

# 팔로워 크롤링
driver.get(f'https://www.instagram.com/{instagram_id}/followers/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

applicant_num_list = []

for follow in soup.select('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li'):
    followers.append(follow.attrs['title'])

print(followers)
