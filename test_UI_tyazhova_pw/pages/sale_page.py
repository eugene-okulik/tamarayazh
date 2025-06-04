from test_UI_tyazhova_pw.pages.base_page import BasePage
from test_UI_tyazhova_pw.pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = "/sale.html"

    def click_to_women_deals_link(self):
        self.find(loc.womens_deals_link).click()

    def click_to_men_deals_link(self):
        self.find(loc.mens_bargains_link).click()

    def get_visible_product_items(self):
        self.page.wait_for_selector(loc.product_items_loc, timeout=10000)
        return self.page.locator(loc.product_items_loc).all()
