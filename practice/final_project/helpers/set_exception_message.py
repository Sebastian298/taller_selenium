
from practice.final_project.helpers.selenium_exception import SeleniumException

def set_exception_message(type):
    match type:
        case "timeOut":
            return SeleniumException("El tiempo de espera para encontrar el elemento se cumplió.")
        case "noSuchElement":
            return SeleniumException("No se encontró el elemento.")
        case "webDriverException":
            return SeleniumException("Error en el driver al buscar el elemento.")