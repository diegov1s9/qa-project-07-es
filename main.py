import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_pedir_un_taxi = (By.XPATH, '//div[@class="type-picker shown"]/div[@class="results-container"]/div[@class="results-text"]/button')
    comfort_rate = (By.XPATH, '//div[@class="tariff-cards"]/div[5]')
    select_rate = comfort_rate
    div_phone_number = (By.CLASS_NAME, 'np-text')
    input_id_phone = (By.ID, 'phone')
    close_modal_phone_number = (By.CLASS_NAME, 'close-button.section-close')
    div_method_of_payment = (By.CLASS_NAME, 'pp-text')
    add_a_card = (By.CLASS_NAME, 'pp-row.disabled')
    card_input = (By.ID, 'number')
    card_code_input = (By.XPATH, '//div[@class="card-code"]/div[@class="card-code-input"]/input[@id="code"]')
    button_enlace = (By.XPATH, '//div[@class="pp-buttons"]/button')
    button_cerrar_modal_opcion_de_pago = (By.XPATH, '//div[@class="payment-picker open"]/div[@class="modal"]/div[@class="section active"]/button')
    input_message_for_driver = (By.XPATH, '//input[@id="comment"]')
    switch_ask_for_a_blanket_and_tissues = (By.XPATH, '//input[@class="switch-input"]')
    input_ice_cream = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    value_input_ice_cream = (By.XPATH, '(//div[@class="counter-value"])[1]')
    button_pedir_un_taxi_parte_final = (By.XPATH, '//div[@class="workflow"]/div[@class="smart-button-wrapper"]/button')
    modal_shown_to_search_for_a_taxi = (By.XPATH, '//div[@class="order shown"]')
    order_header_title_search_driver = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')
    def click_in_pedir_un_taxi(self):
        #Perdón por esto, pero quería practicar y no encontraba la manera de aplicar el assert. :)
        button = self.driver.find_element(*self.button_pedir_un_taxi)
        #Obtener el ID del elemento padre utilizando JavaScript en este caso 2 div antes
        parent_id_script_before = "return arguments[0].parentNode.parentNode.parentNode.getAttribute('class');"
        parent_id_before = self.driver.execute_script(parent_id_script_before, button)
        button.click()
        parent_id_script = "return arguments[0].parentNode.parentNode.parentNode.getAttribute('class');"
        parent_id_after = self.driver.execute_script(parent_id_script, button)
        return f"clase antes del clic: {parent_id_before}" + f" clase después del clic: {parent_id_after}"
    def click_in_select_rate(self):
        #Función que realiza el click en un tipo de tarifa. Es parametrizable cambiando la asignación de la variable  {select_rate}
        button = self.driver.find_element(*self.select_rate)
        class_before_click = button.get_attribute("class")
        button.click()
        class_after_click = button.get_attribute("class")
        return f"clase antes del clic: {class_before_click}" + f" clase después del clic: {class_after_click}"

    def set_input_id_phone_number(self, phone_number):
        #Función que asigna mediante el ID del input del teléfono.
        self.driver.find_element(*self.input_id_phone).send_keys(phone_number)
    def get_input_id_phone_number(self):
        #Función que obtiene el valor mediante el ID del input del teléfono.
        return self.driver.find_element(*self.input_id_phone).get_property('value')
    def complete_phone_number(self,phone_number):
        #Función que completa correctamente el número de teléfono.
        self.driver.find_element(*self.div_phone_number).click()
        time.sleep(2)
        self.set_input_id_phone_number(phone_number)
        value_input_phone_number = self.get_input_id_phone_number()
        time.sleep(2)
        self.driver.find_element(*self.close_modal_phone_number).click()
        return "Value input Phone number " + value_input_phone_number

    def click_in_div_method_of_payment(self):
        #Función que solo realiza el clic en la forma de pago, puede ser reutilizado para otras pruebas, por ejemplo, pruebas negativas.
        return self.driver.find_element(*self.div_method_of_payment).click()
    def click_in_add_a_card(self):
        #Función que solo realiza el click en 'Agregar una tarjeta'.
        return self.driver.find_element(*self.add_a_card).click()

    def set_card_input(self,card_number):
        #Función que asigna el valor de una tarjeta de crédito al input.
        self.driver.find_element(*self.card_input).send_keys(card_number)
    def get_card_input(self):
        #Función que obtiene el número de tarjeta.
        return self.driver.find_element(*self.card_input).get_property('value')
    def set_card_code(self,card_code):
        #Función que asigna un código de tarjeta al input.
        self.driver.find_element(*self.card_code_input).send_keys(card_code, Keys.TAB)
    def get_card_code(self):
        #Función que obtiene el código de tarjeta.
        return self.driver.find_element(*self.card_code_input).get_property('value')
    def click_in_button_enlace(self):
        return self.driver.find_element(*self.button_enlace).click()
    def click_in_button_cerrar_modal_opcion_de_pago(self):
       return self.driver.find_element(*self.button_cerrar_modal_opcion_de_pago).click()
    def set_message_for_driver(self,message):
        #Función que asigna un mensaje al conductor.
        self.driver.find_element(*self.input_message_for_driver).send_keys(message)
    def get_message_for_driver(self):
        #Función que obtiene el valor del mensaje para el conductor.
        return self.driver.find_element(*self.input_message_for_driver).get_property('value')
    def get_value_ask_for_a_blanket_and_tissues(self):
        return self.driver.find_element(*self.switch_ask_for_a_blanket_and_tissues).is_selected()
    def change_switch_ask_for_a_blanket_and_tissues(self):
        #Función que cambia el switch de manta y pañuelos.
        checkbox_element = self.driver.find_element(*self.switch_ask_for_a_blanket_and_tissues)
        return self.driver.execute_script("arguments[0].checked = true;", checkbox_element)
    def get_value_input_ice_cream(self):
        #Obtiene la cantidad de helado agregado.
        return self.driver.find_element(*self.value_input_ice_cream).text
    def add_input_ice_cream(self,cantidad):
        #Función que agrega x cantidad de helados.
        if cantidad > 0 and cantidad <= 2:
            for i in range(cantidad):
                self.driver.find_element(*self.input_ice_cream).click()
                time.sleep(2)
            return 1
        else:
            return 0
    def get_modal_shown_to_search_for_a_taxi(self):
        #Validar que modal se muestre en pantalla mediante su clase.
        button = self.driver.find_element(*self.modal_shown_to_search_for_a_taxi)
        class_after_click = button.get_attribute("class")
        return f"modal se visualiza con la clase: {class_after_click}"
    def click_button_pedir_un_taxi_parte_final(self):
        #Función que realiza el clic en el último botón para pedir un taxi.
        return self.driver.find_element(*self.button_pedir_un_taxi_parte_final).click()
    def validate_order_header_title_search_driver(self):
        #Funcion que valida el cambio del texto "buscar automóvil"
        #se obtiene el texto inicial
        text_search_car = WebDriverWait(self.driver, 22).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'order-header-title'))
        ).text
        #se espera hasta que el texto del div sea diferente
        try:
            WebDriverWait(self.driver, 22).until_not(
                expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, 'order-header-title'), text_search_car)
            )
            return "Texto diferente"
        except Exception as e:
           return f"Error: {e}"

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        capabilities = Options()
        capabilities.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=capabilities)

    def test_set_route(self):
        #Ejercicio Acción 1
        #Configura la dirección desde y hasta y valida que los campos contengan las direcciones ingresadas.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_click_in_pedir_un_taxi(self):
        #Se realiza clic en pedir taxi
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
    def test_select_comfort_rate(self):
        #Ejercicio Acción 2
        #Función que selecciona la tarifa Comfort.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
    def test_fill_in_phone_number(self):
        #Ejercicio Acción 3
        #Se rellena el número de teléfono.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number

    def test_add_credit_card(self):
        #Ejercicio Acción 4
        #Función que agrega una tarjeta de crédito.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        # assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number  no parece ser necesario validar antes el número de teléfono
        routes_page.click_in_div_method_of_payment()
        time.sleep(2)
        routes_page.click_in_add_a_card()
        time.sleep(2)
        card_number = data.card_number
        routes_page.set_card_input(card_number)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_card_input() == card_number
        card_code = data.card_code
        routes_page.set_card_code(card_code)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_card_code() == card_code
        routes_page.click_in_button_enlace()
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        return

    def test_message_for_driver(self):
        #Ejercicio Acción 5
        #Función que agrega un mensaje para el conductor.
        message_for_driver = data.message_for_driver
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        routes_page.set_message_for_driver(message_for_driver)
        time.sleep(4)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_message_for_driver() == message_for_driver
        return
    def test_ask_for_a_blanket_and_tissues(self):
        #Ejercicio Acción 6
        #Función que cambia el switch de manta y pañuelos.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert not routes_page.get_value_ask_for_a_blanket_and_tissues(), "Switch is not in false state"
        time.sleep(2)
        routes_page.change_switch_ask_for_a_blanket_and_tissues()
        time.sleep(2)
        assert routes_page.get_value_ask_for_a_blanket_and_tissues(), "Switch is still false"
        return

    def test_add_two_ice_cream(self):
        #Ejercicio Acción 7
        #Función que agrega dos helados.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        routes_page.add_input_ice_cream(2)
        time.sleep(2)
        assert routes_page.get_value_input_ice_cream() == '2'
        return


    def test_validate_modal_to_search_for_a_taxi(self):
        #Ejercicio Acción 8
        #Función que valida el modal para buscar un taxi.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number
        time.sleep(2)
        routes_page.click_in_div_method_of_payment()
        time.sleep(2)
        routes_page.click_in_add_a_card()
        time.sleep(2)
        card_number = data.card_number
        routes_page.set_card_input(card_number)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_card_input() == card_number
        card_code = data.card_code
        routes_page.set_card_code(card_code)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_card_code() == card_code
        routes_page.click_in_button_enlace()
        time.sleep(2)
        routes_page.click_in_button_cerrar_modal_opcion_de_pago()
        time.sleep(2)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        time.sleep(2)
        assert routes_page.get_message_for_driver() == message_for_driver
        time.sleep(2)
        routes_page.click_button_pedir_un_taxi_parte_final()
        time.sleep(2)
        assert routes_page.get_modal_shown_to_search_for_a_taxi() == "modal se visualiza con la clase: order shown"
        time.sleep(2)

    def test_validate_driver_information_modal(self):
        #Ejercicio Acción 9
        #Funcion que valida la información del conductor en modal de busqueda del conductor
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_pedir_un_taxi() == "clase antes del clic: type-picker shown clase después del clic: type-picker"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "clase antes del clic: tcard clase después del clic: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number
        time.sleep(2)
        routes_page.click_in_div_method_of_payment()
        time.sleep(2)
        routes_page.click_in_add_a_card()
        time.sleep(2)
        card_number = data.card_number
        routes_page.set_card_input(card_number)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_card_input() == card_number
        card_code = data.card_code
        routes_page.set_card_code(card_code)
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_card_code() == card_code
        routes_page.click_in_button_enlace()
        time.sleep(2)
        routes_page.click_in_button_cerrar_modal_opcion_de_pago()
        time.sleep(2)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        time.sleep(2)
        assert routes_page.get_message_for_driver() == message_for_driver
        time.sleep(2)
        routes_page.click_button_pedir_un_taxi_parte_final()
        time.sleep(2)
        assert routes_page.get_modal_shown_to_search_for_a_taxi() == "modal se visualiza con la clase: order shown"
        time.sleep(2)
        assert routes_page.validate_order_header_title_search_driver() == "Texto diferente"
        time.sleep(2)
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
