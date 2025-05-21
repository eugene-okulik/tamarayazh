from playwright.sync_api import Page, expect


def test_submit_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")

    page.get_by_placeholder("First Name").fill("Tamara")
    page.get_by_placeholder("Last Name").fill("Yazhova")
    page.get_by_placeholder("name@example.com").fill("test999@gmail.com")

    gender_field = page.locator("//label[@for='gender-radio-2']")
    gender_field.click()

    mobile_field = page.locator("//input[@id='userNumber']")
    mobile_field.fill('1234567890')

    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.click()
    page.select_option(".react-datepicker__month-select", label='April')
    page.select_option('.react-datepicker__year-select', label="1990")
    page.locator("//div[@aria-label='Choose Monday, April 2nd, 1990']")

    subject_field = page.locator("#subjectsInput")
    subject_field.type("English")
    subject_field.press('Enter')

    hobbies_field = page.locator("//label[@for='hobbies-checkbox-2']")
    hobbies_field.check()

    address_field = page.get_by_placeholder("Current Address")
    address_field.fill("Efrain Huerta 55")

    state_field = page.locator("#state")
    state_field.click()
    state_option = page.locator("//div[text()='Haryana']")
    state_option.click()

    city_field = page.locator("#city")
    city_field.click()
    city_option = page.locator("//div[text()='Panipat']")
    city_option.click()

    submit_btn = page.locator(".btn-primary")
    submit_btn.click()
    expect(page.locator(".modal-content")).to_contain_text("Tamara Yazhova")
