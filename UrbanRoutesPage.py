import selector
import time
import utility
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.from_field)
        )  #You must wait for the page to load and the elements to be found before assigning values.
        self.driver.find_element(*selector.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.to_field)
        )  #You must wait for the page to load and the elements to be found before assigning values.
        self.driver.find_element(*selector.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*selector.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*selector.to_field).get_property('value')
    def click_in_button_order_a_taxi(self):
        #Click on the first button to order a taxi
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.button_order_a_taxi)
        )
        return self.driver.find_element(*selector.button_order_a_taxi).click()
    def click_in_select_rate(self):
        #Function performed by clicking on a rate type. It is parameterizable by changing the assignment of the variable {select_rate}
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.select_rate)
        )
        button = self.driver.find_element(*selector.select_rate)
        button.click()
        class_after_click = button.get_attribute("class")
        return f"class after click: {class_after_click}"
    def set_input_id_phone_number(self, phone_number):
        #Function assigned by the phone input ID.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.input_id_phone)
        )
        self.driver.find_element(*selector.input_id_phone).send_keys(phone_number)
    def get_input_id_phone_number(self):
        #Function that obtains the value using the phone input ID.
        return self.driver.find_element(*selector.input_id_phone).get_property('value')
    def set_input_code_phone_number(self,code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.input_text_code_phone_number)
        )
        self.driver.find_element(*selector.input_text_code_phone_number).send_keys(code)
    def get_input_code_phone_number(self):
        return self.driver.find_element(*selector.input_text_code_phone_number).get_property('value')
    def complete_phone_number(self,phone_number):
        #Function that correctly completes the phone number.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.div_phone_number)
        )
        self.driver.find_element(*selector.div_phone_number).click()
        self.set_input_id_phone_number(phone_number)
        value_input_phone_number = self.get_input_id_phone_number()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.next_phone_number)
        )
        self.driver.find_element(*selector.next_phone_number).click()
        time.sleep(2)
        #confirmar el celular utilizando la funcion del archivo utility.py
        code_phone_number = utility.retrieve_phone_code(self.driver)
        self.set_input_code_phone_number(code_phone_number)
        if self.get_input_code_phone_number() != code_phone_number:
            return "error code"
        time.sleep(2)
        self.driver.find_element(*selector.confirm_code_phone_number).click()
        time.sleep(2)
        return "Value input Phone number " + value_input_phone_number

    def click_in_div_method_of_payment(self):
        #Function that only performs the click on the payment method, it can be reused for other tests, for example, negative tests.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.div_method_of_payment)
        )
        return self.driver.find_element(*selector.div_method_of_payment).click()
    def click_in_add_a_card(self):
        #Function that is only performed by clicking on 'Add a card'.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.add_a_card)
        )
        return self.driver.find_element(*selector.add_a_card).click()

    def set_card_input(self,card_number):
        #Function that assigns the value of a credit card to the input.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.card_input)
        )
        self.driver.find_element(*selector.card_input).send_keys(card_number)
    def get_card_input(self):
        #Function that obtains the card number.
        return self.driver.find_element(*selector.card_input).get_property('value')
    def set_card_code(self,card_code):
        #Function that assigns a card code to the input.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.card_code_input)
        )
        self.driver.find_element(*selector.card_code_input).send_keys(card_code, Keys.TAB)
    def get_card_code(self):
        #Function that obtains the card code.
        return self.driver.find_element(*selector.card_code_input).get_property('value')
    def click_in_button_enlace(self):
        return self.driver.find_element(*selector.button_enlace).click()
    def click_in_button_cerrar_modal_opcion_de_pago(self):
       return self.driver.find_element(*selector.button_cerrar_modal_opcion_de_pago).click()
    def set_message_for_driver(self,message):
        #Function that assigns a message to the driver.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.input_message_for_driver)
        )
        self.driver.find_element(*selector.input_message_for_driver).send_keys(message)
    def get_message_for_driver(self):
        #Function that obtains the value of the message for the driver.
        return self.driver.find_element(*selector.input_message_for_driver).get_property('value')
    def get_value_ask_for_a_blanket_and_tissues(self):
        return self.driver.find_element(*selector.switch_ask_for_a_blanket_and_tissues).is_selected()
    def change_switch_ask_for_a_blanket_and_tissues(self):
        #Function that changes the blanket and scarves switch.
        checkbox_element = self.driver.find_element(*selector.switch_ask_for_a_blanket_and_tissues)
        return self.driver.execute_script("arguments[0].checked = true;", checkbox_element)
    def get_value_input_ice_cream(self):
        #Gets the amount of ice cream added.
        return self.driver.find_element(*selector.value_input_ice_cream).text
    def add_input_ice_cream(self,cantidad):
        #Function that adds x amount of ice cream.
        if cantidad > 0 and cantidad <= 2:
            for i in range(cantidad):
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.visibility_of_element_located(selector.input_ice_cream)
                )
                self.driver.find_element(*selector.input_ice_cream).click()
            return 1
        else:
            return 0
    def get_modal_shown_to_search_for_a_taxi(self):
        #Validate that the modal is displayed on the screen using its class.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.modal_shown_to_search_for_a_taxi)
        )
        button = self.driver.find_element(*selector.modal_shown_to_search_for_a_taxi)
        class_after_click = button.get_attribute("class")
        return f"modal is displayed with class: {class_after_click}"
    def click_button_order_a_taxi_final_part(self):
        #Function that performs the click on the last button to order a taxi.
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(selector.button_order_a_taxi_final_part)
        )
        return self.driver.find_element(*selector.button_order_a_taxi_final_part).click()
    def validate_order_header_title_search_driver(self):
        #Function that validates the change of the "search car" text
        #the initial text is obtained
        order_header_title_search_driver_local = selector.order_header_title_search_driver
        try:
            text_search_car = WebDriverWait(self.driver, 36).until(
                expected_conditions.presence_of_element_located(order_header_title_search_driver_local)
            ).text
        except Exception as e:
            return f"Error text: {e}"
        #wait until the div text is different
        try:
            WebDriverWait(self.driver, 36).until_not(
                expected_conditions.text_to_be_present_in_element(order_header_title_search_driver_local, text_search_car)
            )
            return "Different text"
        except Exception as e:
           return f"Error: {e}"