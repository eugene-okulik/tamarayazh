from playwright.sync_api import Page, expect, BrowserContext
import re


def test_alert(page: Page):
    page.on('dialog', lambda confirm: confirm.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text("Ok")


def test_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    link_button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        link_button.click()
    new_page = new_page_event.value
    expected_text = new_page.locator('#result-text')
    expect(expected_text).to_have_text("I am a new page in a new tab")
    new_page.close()
    expect(link_button).to_be_enabled()


def test_color_change(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    color_change_btn = page.locator('#colorChange')
    expect(color_change_btn).to_have_class(re.compile('text-danger'))
    color_change_btn.click()
