from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role('link', name='Form Authentication').click()
    username_field = page.get_by_role('textbox', name='username')
    username_field.fill('tomsmith')
    password_field = page.get_by_role('textbox', name='password')
    password_field.fill('SuperSecretPassword!')
    page.get_by_role('button', name=' Login').click()
    expect(page.get_by_role('link', name='Logout')).to_be_visible()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
