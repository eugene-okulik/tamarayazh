import random


class AccountData:
    def __init__(self):
        self.first_name = "Petr"
        self.last_name = "Petrov"
        self.email = f"user{random.randint(100, 999)}@example.com"
        self.password = "SuperPass123!"
        self.confirm_password = "SuperPass123!"


class InvalidAccountData:
    first_name = "Petr"
    last_name = "Petrov"
    email = "mismatch@example.com"
    password = "Password123!"
    confirm_password = "Different123!"
