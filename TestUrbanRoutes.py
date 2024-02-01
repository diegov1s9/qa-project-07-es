import UrbanRoutesPage
import data
import time
from selenium import webdriver

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
        # Ejercicio Acción 1
        # Configura la dirección desde y hasta y valida que los campos contengan las direcciones ingresadas.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        # Ejercicio Acción 2
        # Función que selecciona la tarifa Comfort.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores

    def test_fill_in_phone_number(self):
        # Ejercicio Acción 3
        # Se rellena el número de teléfono.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)
        assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number
        time.sleep(2)

    def test_add_credit_card(self):
        # Ejercicio Acción 4
        # Función que agrega una tarjeta de crédito.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2) # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
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
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar

    def test_message_for_driver(self):
        # Ejercicio Acción 5
        # Función que agrega un mensaje para el conductor.
        message_for_driver = data.message_for_driver
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        routes_page.set_message_for_driver(message_for_driver)
        time.sleep(4)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.get_message_for_driver() == message_for_driver

    def test_ask_for_a_blanket_and_tissues(self):
        # Ejercicio Acción 6
        # Función que cambia el switch de manta y pañuelos.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert not routes_page.get_value_ask_for_a_blanket_and_tissues(), "Switch is not in false state"
        time.sleep(2)
        routes_page.change_switch_ask_for_a_blanket_and_tissues()
        time.sleep(2)
        assert routes_page.get_value_ask_for_a_blanket_and_tissues(), "Switch is still false"

    def test_add_two_ice_cream(self):
        # Ejercicio Acción 7
        # Función que agrega dos helados.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignar
        routes_page.add_input_ice_cream(2)
        time.sleep(2)
        assert routes_page.get_value_input_ice_cream() == '2'

    def test_validate_modal_to_search_for_a_taxi(self):
        # Ejercicio Acción 8
        # Función que valida el modal para buscar un taxi.
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)
        assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number
        time.sleep(2)
        routes_page.click_in_div_method_of_payment()
        time.sleep(2)
        routes_page.click_in_add_a_card()
        time.sleep(2)
        card_number = data.card_number
        routes_page.set_card_input(card_number)
        time.sleep(2)
        assert routes_page.get_card_input() == card_number
        card_code = data.card_code
        routes_page.set_card_code(card_code)
        time.sleep(2)
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
        routes_page.click_button_order_a_taxi_final_part()
        time.sleep(2)
        assert routes_page.get_modal_shown_to_search_for_a_taxi() == "modal is displayed with class: order shown"
        time.sleep(2)

    def test_validate_driver_information_modal(self):
        # Ejercicio Acción 9
        # Funcion que valida la información del conductor en modal de busqueda del conductor
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        time.sleep(2)  # se debe esperar para que la pagina sea cargada y se puedan encontrar los elementos antes de asignarle valores
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(2)
        routes_page.click_in_button_order_a_taxi()
        time.sleep(2)
        assert routes_page.click_in_select_rate() == "class after click: tcard active"
        time.sleep(2)
        assert routes_page.complete_phone_number(phone_number) == "Value input Phone number " + phone_number
        time.sleep(2)
        routes_page.click_in_div_method_of_payment()
        time.sleep(2)
        routes_page.click_in_add_a_card()
        time.sleep(2)
        card_number = data.card_number
        routes_page.set_card_input(card_number)
        time.sleep(2)
        assert routes_page.get_card_input() == card_number
        card_code = data.card_code
        routes_page.set_card_code(card_code)
        time.sleep(2)
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
        routes_page.click_button_order_a_taxi_final_part()
        time.sleep(2)
        assert routes_page.get_modal_shown_to_search_for_a_taxi() == "modal is displayed with class: order shown"
        time.sleep(2)
        assert routes_page.validate_order_header_title_search_driver() == "Different text"
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
