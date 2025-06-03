from test_UI_tyazhova_pw.conftest import sale_page


def test_navigate_to_women_deals_link(sale_page):
    sale_page.open_page()
    sale_page.click_to_women_deals_link()
    assert "women-sale.html" in sale_page.get_current_url()


def test_navigate_to_men_deals_link(sale_page):
    sale_page.open_page()
    sale_page.click_to_men_deals_link()
    assert "men-sale.html" in sale_page.get_current_url()


def test_sale_page_displays_product_items(sale_page):
    sale_page.open_page()
    products = sale_page.get_visible_product_items()
    assert len(products) > 0
