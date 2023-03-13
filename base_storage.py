from abc import ABC, abstractmethod
from exepctions import NotEnoughSpace, UnknowmProduct


class Storage(ABC):

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
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class BaseStorage(Storage):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    def add(self, product, amount):
        if self.get_free_space() < amount:
            raise NotEnoughSpace
        if product in self._items:
            self._items[product] += amount
        else:
            self._items[product] = amount

    def remove(self, product, amount):
        try:
            if amount > self._items[product]:
                raise NotEnoughSpace
            else:
                self._items[product] -= amount
                if self._items[product] == 0:
                    del self._items[product]
        except KeyError:
            raise UnknowmProduct

    def get_free_space(self):
        return self._capacity - sum(self.get_items().values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self.get_items().keys())
