from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import data
from data.data import message_for_driver
from helpers import utilities





class UrbanRoutesPage:

    #Address configuration
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_tariff_icon = (By.XPATH, '//div[@class= "tcard-title" and text()="Comfort"]')
    comfort_tariff_assert = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"] ')

    #Tariff selection
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.ID, 'phone')
    phone_next_button = (By.CSS_SELECTOR, '.button.full')
    phone_code_field = (By.ID, 'code')
    phone_confirmation_button = (By.XPATH, '//button[@type="submit" and text()="Confirmar"]')
    phone_close_button = (By.CSS_SELECTOR, 'button.close-button.section-close')

    #Payment Method
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.ID, 'number')
    card_code_field = (By.NAME, 'code')  # Campo CVV - ¡importante!
    submit_card_button = (By.XPATH, "//div[contains(@class,'section active')]//button[text()='Agregar']")
    added_card_label = (By.CLASS_NAME, "pp-value-text")
    close_payment_modal = (By.XPATH, '//div[@class="section active"]/button[@class="close-button section-close"]')


    #Write Message to driver
    message_input = (By.ID, "comment")

    #Blankets & Tissues
    requirement_arrow = (By.XPATH, '//input[@class="switch-input"]')
    blanket_tissue_slider =(By.XPATH, '//span[@class="slider round"]')


    #ice cream
    ice_cream_bucket = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']")
    ice_cream_plus = (By.XPATH, "//div[@class='counter-plus' and text()='+']")
    ice_cream_count = (By.XPATH, '//div[@class="counter-value"]')

    #Modal order taxi
    smart_button_taxi = (By.XPATH, '//span[@class="smart-button-main"]')
    modal_taxi = (By.XPATH, '//div[text()="Buscar automóvil"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    #Address config
    def set_from (self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):  #paso 2
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    # Comfort tariff selection
    def get_comfort_tariff_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_tariff_icon)
        )

    def click_comfort_tariff_icon(self):
        self.get_comfort_tariff_icon().click()

    def get_comfort_tariff_assert(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.comfort_tariff_assert)
        )

    def read_comfort_tariff_assert(self):
        return self.get_comfort_tariff_assert().text


    #User information fill in
    def get_phone_number_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_field)
        )

    def set_phone_number_field(self):
        self.get_phone_number_field().send_keys(data.phone_number)

    def get_phone_next_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_next_button)
        )

    def click_on_phone_next_button(self):
        self.get_phone_next_button().click()

    def get_phone_code_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_code_field)
        )

    def set_phone_code_field(self):
        code = utilities.retrieve_phone_code(self.driver)
        self.get_phone_code_field().send_keys(code)

    def get_phone_confirmation_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_confirmation_button)
        )

    def click_on_phone_confirmation_button(self):
        self.get_phone_confirmation_button().click()


    #Payment method
    def get_payment_method_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.payment_method_button)
        ).click()

    def get_add_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def set_card_number_field(self):
        self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        ).send_keys(data.card_number)

    def get_card_number_value(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        ).get_attribute("value")

    def set_card_code_field(self):
        self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        ).send_keys(data.card_code)

    def get_card_code_value(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        ).get_attribute("value")

    def set_key_tab(self):
        self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        ).send_keys(keys.Keys.TAB)

    def click_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.submit_card_button)
        ).click()

    def is_card_added(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.added_card_label)
        ).text

    def click_close_modal(self):
        self.wait.until(EC.presence_of_all_elements_located(self.close_payment_modal))[1].click()


    #Write Message to Driver

    def get_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.message_input))

    def set_message(self):
        self.wait.until(EC.visibility_of_element_located(self.message_input)).send_keys(message_for_driver)

    #Blanket and Tissues

    def get_requirement_arrow(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.requirement_arrow)
        ).click()

    def click_on_blanket_slider(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.blanket_tissue_slider)
        ).click()

    def get_checked_blanket_and_tissues(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.requirement_arrow))[0]

    #Ice cream (CORRECCIÓN: Corregir la lógica de set_two_ice_creams. En pages/urban_routes_page.py el click queda fuera del for, así que en la práctica no garantiza dos clics.)

    def get_ice_cream_count(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.ice_cream_count))[0]


    def click_on_ice_cream(self, cnt):
        for n in range(cnt):
            self.wait.until(
                EC.visibility_of_all_elements_located(self.ice_cream_plus)
            )[0].click()


    #Order Taxi Button

    def get_smart_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.smart_button_taxi)
        )

    def click_on_smart_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.smart_button_taxi)
        ).click()

    def get_modal(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.modal_taxi)
        )