from playwright.sync_api import Page, expect, Route
import re
import json


def test_title_is_changed(page: Page):
    def handle_rout(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 16 про"

        route.fulfill(
            response=response,
            body=json.dumps(body)
        )

    page.route(re.compile("https://www.apple.com/shop/api/digital-mat"), handle_rout)

    page.goto("https://www.apple.com/shop/buy-iphone")

    page.locator("//h3[text()='iPhone 16 Pro &']").click()
    title = page.locator("//h2[contains(normalize-space(), 'яблокофон 16 про')]")

    expect(title).to_have_text("яблокофон 16 про")
