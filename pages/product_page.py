from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_present_success_message(self, product_name=None):
        """Проверяет что сообщение об успешности добавления товара в корзину отображается
        """
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCSESS), 'Success alert is not presented'
        if not product_name:
            product_name = self.get_product_name()
        alert = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCSESS)
        assert product_name in alert.text, f'Product name({product_name}) should be in alert.text({alert.text}) but not'

    def should_be_present_cost_basket_message(self, product_price=None):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_CHANGE_COST_BASKET), 'Success alert is not presented'
        if not product_price:
            product_price = self.get_product_price()
        alert = self.browser.find_element(*ProductPageLocators.MESSAGE_CHANGE_COST_BASKET)
        assert product_price in alert.text, f'Price({product_price}) should be in alert.text({alert.text}) but not'

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LABEL).text

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LABEL).text
