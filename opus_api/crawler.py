import opus_api.settings as settings
import selenium
from selenium.webdriver.support.ui import Select
from opus_api.cache import hcache

driver = selenium.webdriver.PhantomJS()


@hcache
def get(src, target):
    driver.get(settings.site_url)
    select_src = Select(driver.find_element_by_name('src'))
    select_src.select_by_value(src)
    select_target = Select(driver.find_element_by_name('trg'))
    select_target.select_by_value(target)
    return driver.execute_script("return document.body;")\
        .get_attribute("innerHTML")
