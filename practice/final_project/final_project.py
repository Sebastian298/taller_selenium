from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from practice.final_project.helpers.selenium_actions import SeleniumActions
from practice.final_project.services.students_service import StudentsService


class SeleniumSimposiumPortal:
    def __init__(self):
        self.driver = self.__initialize_driver()

    def run_process(self):
        self.driver.get('https://taller-selenium.netlify.app/')
        self.__logIn()
        self.__writeInformation()
        self.__report_process()
        self.driver.quit()

    def __logIn(self):
        try:
            user_name_input = SeleniumActions.get_element_by_id(self.driver, 'username',15)
            password_input = SeleniumActions.get_element_by_id(self.driver, 'password',15)
            user_text = SeleniumActions.get_element_by_xpath(self.driver, '//*[@id="containerUsers"]/ul/li[1]/strong',15)
            user_name_input.send_keys(user_text.text);
            password_text = SeleniumActions.get_element_by_xpath(self.driver, '//*[@id="containerPasswords"]/p/strong',15)
            password_input.send_keys(password_text.text);
            login_button = SeleniumActions.get_element_by_id(self.driver, 'logginButton',15)
            SeleniumActions.wait_and_click_element(self.driver, login_button,15)
        except Exception as e:
            print(e)
            self.driver.quit()

    def __writeInformation(self):
        try:
            SeleniumActions.wait_for_element(self.driver, '/html/body/div[2]/main/div[1]/h2',15)
            students = StudentsService.get_students()
            no_control_input = SeleniumActions.get_element_by_id(self.driver, 'noControl',15)
            name_input = SeleniumActions.get_element_by_id(self.driver, 'name',15)
            email_input = SeleniumActions.get_element_by_xpath(self.driver, '/html/body/div[2]/main/div[2]/div/div[1]/div[3]/input',15)
            semestre_input = SeleniumActions.get_element_by_id(self.driver, 'semestre',15)
            select_grupo = SeleniumActions.get_element_by_id(self.driver, 'grupo',15)
            select_talla = SeleniumActions.get_element_by_xpath(self.driver, '/html/body/div[2]/main/div[2]/div/div[1]/div[6]/select',15)
            radio_masculino = SeleniumActions.get_element_by_xpath(self.driver, '/html/body/div[2]/main/div[2]/div/div[2]/div/div[1]/input',15)
            radio_femenino = SeleniumActions.get_element_by_xpath(self.driver, '/html/body/div[2]/main/div[2]/div/div[2]/div/div[2]/input',15)
            check_taller = SeleniumActions.get_element_by_id(self.driver, 'checkTaller',15)
            check_cuota = SeleniumActions.get_element_by_id(self.driver, 'checkCuota',15)
            save_button = SeleniumActions.get_element_by_id(self.driver, 'registerStudent',15)

            for student in students:
                no_control_input.send_keys(student.no_control)
                name_input.send_keys(student.nombre)
                email_input.send_keys(student.correo)
                semestre_input.send_keys(student.semestre)
                SeleniumActions.select_option(select_grupo, student.grupo)
                SeleniumActions.select_option(select_talla, student.talla)
                if student.genero == 'M':
                    radio_masculino.click()
                else:
                    radio_femenino.click()
                if student.taller_registrado == True:
                    check_taller.click()
                if student.cuota_cubierta == True:
                    check_cuota.click()
                
                SeleniumActions.wait_and_click_element(self.driver, save_button,20)
                SeleniumActions.wait_for_text_to_appear(self.driver, 'alertSuccess', 'La información del estudiante se guardó correctamente',20)
        except Exception as e:
            print(e)
            self.driver.quit()

    def __report_process(self):
        try:
           reports_menu_option = SeleniumActions.get_element_by_xpath(self.driver, '/html/body/div[1]/ul/li[2]/a',15)
           reports_menu_option.click()
           SeleniumActions.wait_for_element(self.driver, '/html/body/div[2]/h1',15)
           download_button = SeleniumActions.get_element_by_id(self.driver, 'btnDownload',15)
           download_button.click()
           SeleniumActions.wait_for_text_to_appear(self.driver, 'alertSuccess', 'El archivo se generó correctamente',20)
        except Exception as e:
            print(e)
            self.driver.quit()

    def __initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # Desactivar el guardado de contraseñas
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver