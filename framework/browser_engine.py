# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from public.models.log import Log
from config import setting

log=Log()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/driver/chromedriver.exe'
    ie_driver_path = dir + '/driver/IEDriverServer.exe'
    edge_driver_path=dir+'/driver/msedgedriver.exe'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        # file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(setting.BROWSER_TYPE, encoding='utf-8')

        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        log.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        log.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            log.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            log.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            log.info("Starting IE browser.")
        else:driver=webdriver.Edge(self.edge_driver_path)

        driver.get(url)
        log.info("Open url: %s" % url)
        driver.maximize_window()
        log.info("Maximize the current window.")
        driver.implicitly_wait(10)
        log.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        log.info("Now, Close and quit the browser.")
        self.driver.quit()

