def size_loc(size_label):
    return f"//div[@option-label='{size_label}']"


def color_loc(color_label):
    return f"//div[@option-label='{color_label}']"


add_to_cart_btn_loc = "(//button[@title='Add to Cart' and contains(@class, 'tocart')])[1]"
message_success_loc = (
    "//div[contains(@data-bind, 'prepareMessageForHtml') and contains(text(), 'You added Ana Running Short')]"
)
message_required_option_loc = "//div[text()='You need to choose options for your item.']"
product_loc = 'img[alt="Ana Running Short"]'
