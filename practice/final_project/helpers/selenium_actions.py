from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException,WebDriverException
from practice.final_project.helpers.set_exception_message import set_exception_message


class SeleniumActions:
    
    @staticmethod
    def get_element_by_id(driver,element_id,timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            return element
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
        
    @staticmethod
    def get_element_by_xpath(driver,xpath,timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def get_element_by_name(driver,name,timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.NAME, name))
            )
            return element
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def wait_and_click_element(driver,element,timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(element)
            ).click()
            return True
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def wait_for_element(driver,xpath,timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def get_text_from_element(driver,element,timeout=10):
        try:
            text = WebDriverWait(driver, timeout).until(
                EC.visibility_of(element)
            ).text
            return text
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def write_text_to_element(driver,element,text,timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of(element)
            ).send_keys(text)
            return True
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def select_option(element,option):
        select = Select(element)
        select.select_by_visible_text(option)
        return True
    
    @staticmethod
    def wait_for_text_to_appear(driver, element_id, text, timeout=15):
        try:
            WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element((By.ID, element_id), text)
            )
        except TimeoutException as e:
            print(e)
            raise set_exception_message("timeOut")
        except NoSuchElementException as e:
            print(e)
            raise set_exception_message("noSuchElement")
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")
        
    @staticmethod
    def execute_script(driver,script,element):
        try:
            driver.execute_script(script, element)
            return True
        except WebDriverException as e:
            print(e)
            raise set_exception_message("webDriverException")