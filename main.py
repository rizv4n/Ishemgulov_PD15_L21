from base_storage import BaseStorage
from utils import Request
from exepctions import LogisticError, TooManyDifferentProducts
from data import store_products


class Store(BaseStorage):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, product, amount):
        if product not in self.get_items() and self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(product, amount)


store = Store(store_products)
shop = Shop({})

storages = {
    "склад": store,
    "магазин": shop
}


def main():
    while True:
        print('Введите запрос в виде "Доставить 3 соль из склад в магазин"')
        request = input('Ввод: ')
        req = Request(request)

        try:
            storages[req.from_str].remove(req.product, req.amount)
            print(f"Курьер забрал {req.amount} {req.product} из {req.from_str}")
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[req.to_str].add(req.product, req.amount)
            print(f"Курьер доставил {req.amount} {req.product} из {req.to_str}")
        except LogisticError as error:
            print(error.message)
            continue

        print('На складе хранится')
        for key, value in store.get_items().items():
            print(key, value)

        print('В магазине хранится')
        for key, value in shop.get_items().items():
            print(key, value)


if __name__ == "__main__":
    main()
