# coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def login():

    """自动登录平台获取cookie"""

    driver = webdriver.Firefox()
    driver.get("http://4a.chinatowercom.cn/uac/index")  # 输入平台地址
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_id("username").send_keys("sc_11")   # 输入用户名
    driver.find_element_by_id("password").send_keys('Ww123456*')  # 输入验证码
    #driver.find_element_by_id("password").send_keys('')

    "判断验证码是否正确"


    driver.find_element_by_class_name("login_btn").click()  # 点击登录
    time.sleep(15)
    # 跳入到子页面
    driver.find_element_by_xpath('//div[@class="zoomix"]/ul/li/span').click()
    time.sleep(10)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    time.sleep(30)
    #driver.find_element_by_xpath('//a[contains(text(),"资源管理")]').click()

    move_element = driver.find_element_by_xpath('//a[contains(text(),"资源管理")]')
    ActionChains(driver).move_to_element(move_element).perform()
    time.sleep(2)
    move_element = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/ul/li[3]/dl/dd[1]/a')
    ActionChains(driver).move_to_element(move_element).perform()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/ul/li[3]/dl/dd[1]/dl/dd[1]/a').click()
    #driver.find_element_by_xpath('//dl[@class="nav-level3 28514"]//a[contains(text(),"站址管理")]').click()
    #driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/ul/li[3]/dl/dd[1]/dl/dd[1]/a').click()

    cookies_list = driver.get_cookies()
    cookies = ''
    print(cookies_list)
    """
    for item in cookies_list:
        name = item.get('name')
        value = item.get('value')
        cookies = cookies + name + '=' + value +';'
    cookies = cookies + 'businesstype=2'
    print(cookies)
    return cookies
    """


login()