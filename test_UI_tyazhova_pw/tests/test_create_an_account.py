from test_UI_tyazhova_pw.tests.data import AccountData, InvalidAccountData


def test_create_account_with_all_required_fields(create_new_account):
    data = AccountData()
    create_new_account.open_page()
    create_new_account.fill_all_required_fields(data)
    create_new_account.check_message_of_successful_registration_is(
        "Thank you for registering with Main Website Store."
    )


def test_create_account_with_empty_required_fields(create_new_account):
    create_new_account.open_page()
    create_new_account.click_create_account_button()
    create_new_account.check_required_field_errors_displayed("This is a required field.", 5)


def test_error_message_displayed_for_password_mismatch(create_new_account):
    create_new_account.open_page()
    create_new_account.fill_all_required_fields(InvalidAccountData)
    create_new_account.click_create_account_button()
    create_new_account.check_password_mismatch_error_displayed("Please enter the same value again.")
