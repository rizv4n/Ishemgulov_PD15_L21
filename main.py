from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, product, amount):
        pass

    @abstractmethod
    def remove(self, product, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        return self._items, self._capacity

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, product, amount):
        if self._capacity >= 100:
            print("Склад заполнен")
        else:
            print(f'курьер доставил {amount} {product} на склад')
            self._items[product] = amount

    def remove(self, product, amount):
        try:
            if amount > self._items[product]:
                print('На складе недостаточное количество товара')
            else:
                print('Нужное количество есть на складе')
                print(f'курьер забрал {amount} {product} из склада')
                self._items[product] -= amount
        except KeyError:
            print('На складе нет такого товара')

    def get_free_space(self):
        return self._capacity - sum(self.get_items().values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return self.get_items().keys()


class Shop(Storage):
    def __init__(self, items, capacity=0):
        self._items = items
        self._capacity = capacity

    def add(self, product, amount):
        if self._capacity >= 20:
            print("Склад магазина заполнен")
        else:
            print(f'курьер доставил {amount} {product} в магазин')
            self._items[product] = amount

    def remove(self, product, amount):
        try:
            if amount > self._items[product]:
                print('В магазине недостаточное количество товара')
            else:
                print('Нужное количество есть в магазине')
                print(f'курьер забрал {amount} {product} из магазина')
                self._items[product] -= amount
        except KeyError:
            print('В магазине нет такого товара')

    def get_free_space(self):
        return self._capacity - sum(self.get_items().values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return self.get_items().keys()


class Request:
    def __init__(self, request):

        req_list = request.split()
        count = 0

        for i in req_list:
            count += 1
            if i in ['из', 'с', 'со']:
                break

        amount = req_list[count - 3]
        product = req_list[count - 2]
        from_str = req_list[count]
        to_str = req_list[count + 2]

        self.from_str = from_str
        self.to_str = to_str
        self.amount = int(amount)
        self.product = product


store_products = {'хлеб': 10, 'соль': 20, 'вода': 30, 'печенье': 40}
store = Store(store_products)
shop = Shop({})


def main():
    while True:
        print('Введите запрос в виде "Доставить 3 соль из склад в магазин"')
        request = input('Ввод: ')
        req = Request(request)

        if req.from_str == 'склад':
            store.remove(req.product, req.amount)
            if shop.get_free_space() > req.amount:
                print("На сладе магазина недостаточно места")
            else:
                shop.add(req.product, req.amount)

        elif req.from_str == 'магазин':
            shop.remove(req.product, req.amount)
            if store.get_free_space() > req.amount:
                print("На сладе недостаточно места")
            else:
                store.add(req.product, req.amount)

        print('На складе хранится')
        for key, value in store.get_items().items():
            print(key, value)

        print('В магазине хранится')
        for key, value in shop.get_items().items():
            print(key, value)


if __name__ == "__main__":
    main()
