class BaseError(Exception):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class NotEnoughSpace(LogisticError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(LogisticError):
    message = 'Недостаточно товара на складе'


class UnknowmProduct(LogisticError):
    message = 'Неизвестный товар'


class TooManyDifferentProducts(LogisticError):
    message = 'Слишком много разных товаров'
