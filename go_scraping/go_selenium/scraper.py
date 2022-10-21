from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


class LaunchChromeBrowser:
    def __init__(self):
        self.chrome_options = Options()

        # self.chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(executable_path='./chromedriver',
                                       chrome_options=self.chrome_options)

    def get_driver(self, url):
        self.driver.get(url)
        return self.driver


#
dept_dropdown_btn_xpath="//div[@class='form-group-rb]/select[@name=DDLDeptname]/"
url = 'https://goir.telangana.gov.in/'
launch_browser = LaunchChromeBrowser()
driver = launch_browser.get_driver(url=url)
drp_down_element = driver.find_element(By.NAME,"DDLDeptname")
drp_down_element.click()
# print(element)

# def scrape_telangana_govt_orders():
#     go_url = 'https://goir.telangana.gov.in/'
#     driver = webdriver.Chrome(executable_path='./chromedriver')
#     print(driver.title)
#     driver.get(go_url)
#     return driver
#
#     assert 'Welcome to Telangana Government Order Issue Register' in driver.title


# driver = scrape_telangana_govt_orders()
