from data import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to


    def test_select_comfort_tariff(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff_icon()
        assert self.routes_page.read_comfort_tariff_assert() == "Manta y pañuelos"

    def test_fill_phone_number(self):
        phone_number = data.phone_number
        self.routes_page.click_on_phone_number_button()
        self.routes_page.set_phone_number_field()
        self.routes_page.click_on_phone_next_button()
        self.routes_page.set_phone_code_field()
        self.routes_page.click_on_phone_confirmation_button()
        assert self.routes_page.get_phone_number_button().text == phone_number

    def test_add_card_button(self):
        self.routes_page.get_payment_method_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number_field()
        self.routes_page.set_card_code_field()
        self.routes_page.set_key_tab()
        self.routes_page.click_submit_button()
        self.routes_page.click_close_modal()

    def test_message(self):
        message = data.message_for_driver
        self.routes_page.set_message()

    def test_blanket_and_tissues(self):
        self.routes_page.click_on_blanket_slider()

    def test_add_two_ice_creams(self):
        self.routes_page.set_two_ice_creams()

    def test_order_taxi(self):
        self.routes_page.click_on_smart_button()
        assert self.routes_page.get_modal().text == 'Buscar automóvil'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()