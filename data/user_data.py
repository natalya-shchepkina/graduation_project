from faker import Faker


class User:
    first_name = f"{Faker().first_name()}_test"
    last_name = Faker().last_name()
    email = Faker().email()
    telephone = Faker().phone_number()
    password = Faker().password()
    text = Faker().text()
    credit_card = Faker().credit_card_number()
