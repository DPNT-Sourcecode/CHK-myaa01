

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    registered_skus = ('A', 'B', 'C', 'D')
    if not all(sku in registered_skus for sku in skus):
        return -1

    if len(skus) == 0:
        return 0
