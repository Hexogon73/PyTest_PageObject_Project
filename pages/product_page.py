from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_present_success_message(self):
        """Проверяет что сообщение об успешности добавления товара в корзину отображается
        """
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCSESS), 'Success alert is not presented'
        product_name = self.get_product_name()
        expected_text = '{} has been added to your basket.'.format(product_name)
        alert = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCSESS)
        assert alert.text == expected_text, '{} != {}'.format(
            alert.text, expected_text)

    def should_be_present_cost_basket_message(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_CHANGE_COST_BASKET), 'Success alert is not presented'
        price = self.get_product_price()
        expected_text = 'Your basket total is now {}'.format(price)
        alert = self.browser.find_element(*ProductPageLocators.MESSAGE_CHANGE_COST_BASKET)
        assert alert.text == expected_text, '{} != {}'.format(
            alert.text, expected_text)

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LABEL).text

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LABEL).text
