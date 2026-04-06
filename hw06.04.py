# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.


class CreditCardPayment:
    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount: float):
        print(f"Оплата карткою: {amount}{self._currency}")


class PayPalPayment:
    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount: float):
        print(f"Оплата PayPal: {amount}{self._currency}")


class CryptoPayment:
    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount: float):
        print(f"Оплата криптогаманцем: {amount}{self._currency}")


def create_payment():
    pay_type = input("Введіть тип оплати (card, paypal, crypto): ").strip().lower()

    currency = input("Введіть валюту (наприклад $, €, ₴): ")

    if pay_type == "card":
        return CreditCardPayment(currency)
    elif pay_type == "paypal":
        return PayPalPayment(currency)
    elif pay_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Невідомий тип оплати!")
        return None
