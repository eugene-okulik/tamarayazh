def test_eco_friendly_page_title_is_correct(eco_friendly_page):
    eco_friendly_page.open_page()
    assert eco_friendly_page.get_title() == "Eco Friendly"


def test_add_product_to_cart_from_eco_friendly_page(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.select_size_option(28)
    eco_friendly_page.select_color_option("Orange")
    eco_friendly_page.click_add_selected_product_to_cart()
    eco_friendly_page.check_add_to_cart_success_message("You added Ana Running Short to your")


def test_add_to_cart_requires_size_and_color_options(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.hover_over_product()
    eco_friendly_page.click_add_selected_product_to_cart()
    eco_friendly_page.check_required_option_message("You need to choose options for your item.")
