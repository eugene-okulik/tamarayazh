from playwright.sync_api import expect
from test_UI_tyazhova_pw.pages.base_page import BasePage
from test_UI_tyazhova_pw.pages.locators import eco_friendly_locators as loc
from test_UI_tyazhova_pw.pages.locators.eco_friendly_locators import size_loc, color_loc


class EcoFriendlyPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def select_size_option(self, size_label):
        self.find(size_loc(size_label)).first.click()

    def select_color_option(self, color_label):
        self.find(color_loc(color_label)).first.click()

    def click_add_selected_product_to_cart(self):
        button = self.page.locator(loc.add_to_cart_btn_loc)
        button.click()

    def check_add_to_cart_success_message(self, expected_text):
        message = self.page.locator(loc.message_success_loc)
        message.wait_for(state="visible", timeout=5000)
        expect(message).to_contain_text(expected_text)

    def check_required_option_message(self, expected_message):
        message = self.page.locator(loc.message_required_option_loc)
        message.wait_for(state="visible", timeout=15000)
        expect(message).to_have_text(expected_message)

    def hover_over_product(self):
        self.page.locator(loc.product_loc).hover()
