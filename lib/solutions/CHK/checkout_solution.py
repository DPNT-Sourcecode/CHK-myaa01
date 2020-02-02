from collections import Counter


class Item():
    def __init__(self, letter, price):
        self.letter = letter
        self.price = price


class Order():
    def __init__(self, order_string):
        self.order_string = order_string
        self.item_count = Counter(order_string)

    def get_item_count(self, item):
        return self.item_count[item.letter]

    def reduce_item_count(self, item, quantity):
        self.item_count[item.letter] -= quantity


class SpecialOffer():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def is_applicable_to_order(self, order):
        item_count = order.get_item_count(self.item)
        return item_count >= self.quantity


class FreeOffer(SpecialOffer):
    def __init__(self, item, quantity, free_item):
        super().__init__(item, quantity)
        self.free_item = free_item
        if item == free_item:
            self.minimum_quantity = quantity + 1
        else:
            self.minimum_quantity =

    def is_applicable_to_order(self, order):
        free_item_count = order.get_item_count(self.free_item)
        item_count = order.get_item_count(self.item)
        return super().is_applicable_to_order(order) and free_item_count > 0 and item_count >= self.minimum_quantity

    def calculate_discount(self, order):
        if not self.is_applicable_to_order(order):
            raise ValueError("Cannot apply special offer to order")

        divisor = self.minimum_quantity if self.minimum_quantity else self.quantity
        apply_frequency = order.get_item_count(self.item) // divisor

        order.reduce_item_count(self.free_item, apply_frequency)
        total_discount = 0
        return order, total_discount


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

        order.reduce_item_count(self.item, apply_frequency * self.quantity)

        return order, total_discount

class GroupDiscountOffer():
    def __init__(self, items, quantity, offer_price):
        self.items = items
        self.quantity = quantity

# Define items and offers

ITEM_A = Item('A', 50)
ITEM_B = Item('B', 30)
ITEM_C = Item('C', 20)
ITEM_D = Item('D', 15)
ITEM_E = Item('E', 40)
ITEM_F = Item('F', 10)
ITEM_G = Item('G', 20)
ITEM_H = Item('H', 10)
ITEM_I = Item('I', 35)
ITEM_J = Item('J', 60)
ITEM_K = Item('K', 70)
ITEM_L = Item('L', 90)
ITEM_M = Item('M', 15)
ITEM_N = Item('N', 40)
ITEM_O = Item('O', 10)
ITEM_P = Item('P', 50)
ITEM_Q = Item('Q', 30)
ITEM_R = Item('R', 50)
ITEM_S = Item('S', 20)
ITEM_T = Item('T', 20)
ITEM_U = Item('U', 40)
ITEM_V = Item('V', 50)
ITEM_W = Item('W', 20)
ITEM_X = Item('X', 17)
ITEM_Y = Item('Y', 20)
ITEM_Z = Item('Z', 21)

ITEMS = [
    ITEM_A,
    ITEM_B,
    ITEM_C,
    ITEM_D,
    ITEM_E,
    ITEM_F,
    ITEM_G,
    ITEM_H,
    ITEM_I,
    ITEM_J,
    ITEM_K,
    ITEM_L,
    ITEM_M,
    ITEM_N,
    ITEM_O,
    ITEM_P,
    ITEM_Q,
    ITEM_R,
    ITEM_S,
    ITEM_T,
    ITEM_U,
    ITEM_V,
    ITEM_W,
    ITEM_X,
    ITEM_Y,
    ITEM_Z,
]

FREE_OFFERS = [
    FreeOffer(ITEM_E, 2, ITEM_B),
    FreeOffer(ITEM_F, 2, ITEM_F),
    FreeOffer(ITEM_N, 3, ITEM_M),
    FreeOffer(ITEM_R, 3, ITEM_Q),
    FreeOffer(ITEM_U, 3, ITEM_U),
]

MULTI_PRICING_OFFERS = [
    MultiPricingOffer(ITEM_A, 5, 200),
    MultiPricingOffer(ITEM_A, 3, 130),
    MultiPricingOffer(ITEM_B, 2, 45),
    MultiPricingOffer(ITEM_H, 10, 80),
    MultiPricingOffer(ITEM_H, 5, 45),
    MultiPricingOffer(ITEM_K, 2, 120),
    MultiPricingOffer(ITEM_P, 5, 200),
    MultiPricingOffer(ITEM_Q, 3, 80),
    MultiPricingOffer(ITEM_V, 3, 130),
    MultiPricingOffer(ITEM_V, 2, 90),
    GroupOffer([ITEM_S, ITEM_T, ITEM_X, ITEM_Y, ITEM_Z], 3, 45),
]


def checkout(skus):
    available_item_letters = [item.letter for item in ITEMS]

    if not all(sku in available_item_letters for sku in skus):
        return -1

    if len(skus) == 0:
        return 0

    order = Order(skus)

    # First check free offers
    for free_offer in FREE_OFFERS:
        if free_offer.is_applicable_to_order(order):
            order, discount = free_offer.calculate_discount(order)

    subtotal = 0
    # Then calculate subtotal without taking into account of special offers
    for item in ITEMS:
        quantity = order.get_item_count(item)
        subtotal += item.price * quantity

    # Deduct the offers discounts equivalent prices.
    for multi_pricing_offer in MULTI_PRICING_OFFERS:
        if multi_pricing_offer.is_applicable_to_order(order):
            order, discount = multi_pricing_offer.calculate_discount(order)
            subtotal -= discount

    return subtotal





