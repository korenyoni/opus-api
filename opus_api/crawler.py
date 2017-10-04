import settings
import selenium
from selenium.webdriver.support.ui import Select

driver = selenium.webdriver.PhantomJS()


def get(src, target):
    driver.get(settings.site_url)
    select_src = Select(driver.find_element_by_name('src'))
    select_src.select_by_value(src)
    select_target = Select(driver.find_element_by_name('trg'))
    select_target.select_by_value(target)
    return driver.execute_script("return document.body;")\
        .get_attribute("innerHTML")
