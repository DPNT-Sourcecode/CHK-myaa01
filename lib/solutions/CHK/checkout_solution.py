class Item():
    def __init__(self, letter, price):
        self.letter = letter
        self.price = price


class Order():
    def __init__(self, order_string):
        self.order_string = order_string

    def get_item_count(self, item):
        return self.order_string.count(item.letter)


class SpecialOffer():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def is_applicable_to_order(self, order):
        item_count = order.get_item_count(self.item)
        return item_count >= self.quantity


class MultiPricingOffer(SpecialOffer):
    def __init__(self, item, quantity, offer_price):
        super().__init__(item, quantity)
        self.offer_price = offer_price

    def calculate_discount(self, order):
        if not self.is_applicable_to_order(order):
            raise ValueError("Cannot apply special offer to order")

        apply_frequency = order.get_item_count(self.item) // self.quantity
        discount = (self.quantity * self.item.price) - self.offer_price
        total_discount = discount * apply_frequency
        return total_discount


class FreeOffer(SpecialOffer):
    def __init__(self, item, quantity, free_item):
        super().__init__(item, quantity)
        self.free_item = free_item

    def is_applicable_to_order(self, order):
        free_item_count = order.get_item_count(self.free_item)
        return super().is_applicable_to_order(order) and free_item_count > 0

    def calculate_discount(self, order):
        if not self.is_applicable_to_order(order):
            raise ValueError("Cannot apply special offer to order")

        apply_frequency = order.get_item_count(self.item) // self.quantity
        total_discount = self.free_item.price * apply_frequency
        return total_discount


# Define items and offers

ITEM_A = Item('A', 50)
ITEM_B = Item('B', 30)
ITEM_C = Item('C', 20)
ITEM_D = Item('D', 15)
ITEM_E = Item('E', 40)
ITEM_F = Item('F', 10)

ITEMS = [
    ITEM_A,
    ITEM_B,
    ITEM_C,
    ITEM_D,
    ITEM_E,
    ITEM_F,
]

MULTI_PRICING_OFFERS = [
    MultiPricingOffer(ITEM_A, 3, 130),
    MultiPricingOffer(ITEM_A, 5, 200),
    MultiPricingOffer(ITEM_B, 2, 45),
]

FREE_OFFERS = [
    FreeOffer(ITEM_E, 2, ITEM_B),
    FreeOffer(ITEM_F, 2, ITEM_F),
]

def checkout(skus):
    available_item_letters = [item.letter for item in ITEMS]

    if not all(sku in available_item_letters for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    order = Order(skus)

    # First
    for free_offer in FREE_OFFERS:
        order = free_offer.apply_on_order(order)

    subtotal = 0
    # Then calculate subtotal without taking into account of special offers
    for item in ITEMS:
        quantity = order.get_item_count(item)
        subtotal += item.price * quantity

    # Deduct the offers discounts equivalent prices.
    for free_offer in MULTI_PRICING_OFFERS:
        if offer.is_applicable_to_order(order):
            discount = offer.calculate_discount(order)
            subtotal -= discount

    return subtotal



"""
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }
    special_offers = {
        'B': {
            'amount': 2,
            'offer_price': 45
        }
    }
    if not all(sku in sku_prices for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    letter_counts = Counter(skus)
    price = 0

    if 'E' in letter_counts:
        count_E = letter_counts.pop('E')
        set_frequency = count_E // 2
        while letter_counts['B'] > 0 and set_frequency > 0:
            letter_counts['B'] -= 1
            set_frequency -= 1
        price += (sku_prices['E'] * count_E)

    if 'A' in letter_counts:
        count_A = letter_counts.pop('A')
        set_frequency, count_A = divmod(count_A, 5)
        price += (200 * set_frequency)
        set_frequency, count_A = divmod(count_A, 3)
        price += (130 * set_frequency)
        price += (sku_prices['A'] * count_A)

    for letter, count in letter_counts.items():
        if letter in special_offers:
            set_amount = special_offers[letter]['amount']
            set_frequency, count = divmod(count, set_amount)
            price += (special_offers[letter]['offer_price'] * set_frequency)

        price += (sku_prices[letter] * count)

    return price
"""




