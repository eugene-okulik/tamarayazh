from playwright.sync_api import expect

from test_UI_tyazhova_pw.pages.base_page import BasePage
from test_UI_tyazhova_pw.pages.locators import create_account_locators as loc


class CreateNewAccount(BasePage):
    page_url = "/customer/account/create/"

    def fill_all_required_fields(self, data):
        first_name_field = self.find(loc.firstname_field_loc)
        last_name_field = self.find(loc.lastname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc)

        first_name_field.fill(data.first_name)
        last_name_field.fill(data.last_name)
        email_field.fill(data.email)
        password_field.fill(data.password)
        confirm_password_field.fill(data.confirm_password)

        create_account_button = self.find(loc.btn_create_account_loc)
        create_account_button.click()

    def check_message_of_successful_registration_is(self, text):
        success_message_element = self.find(loc.success_message_loc)
        expect(success_message_element).to_have_text(text)

    def click_create_account_button(self):
        self.find(loc.btn_create_account_loc).click()

    def check_required_field_errors_displayed(self, message_text: str, count: int):
        errors = self.page.locator(loc.error_required_field_message_loc)
        expect(errors).to_have_count(count)
        for i in range(count):
            expect(errors.nth(i)).to_have_text(message_text)

    def check_password_mismatch_error_displayed(self, expected_message):
        error = self.find(loc.password_confirmation_error_loc)
        expect(error).to_have_text(expected_message)
