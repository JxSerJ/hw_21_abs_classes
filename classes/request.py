from colorama import Fore

from exceptions import IncorrectRequest, StorageNotFound
from classes import Store, Shop


class Request:
    def __init__(self, storages: list[Store | Shop], request_string: str):
        self._storages = storages
        self._request_string = request_string
        self._from = None
        self._to = None
        self._amount = None
        self._product = None

        self.request_decomposition()

    def __repr__(self):
        return {'from': self.from_,
                'to': self.to,
                'amount': self.amount,
                'product': self.product}

    @property
    def storages(self):
        return self._storages

    @storages.setter
    def storages(self, new_data):
        self._storages = new_data

    @property
    def request_string(self):
        return self._request_string

    @request_string.setter
    def request_string(self, new_data):
        self._request_string = new_data

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    @from_.setter
    def from_(self, new_data):
        self._from = new_data

    @to.setter
    def to(self, new_data):
        self._to = new_data

    @amount.setter
    def amount(self, new_data):
        self._amount = new_data

    @product.setter
    def product(self, new_data):
        self._product = new_data

    def request_decomposition(self):
        input_data = self.request_string.split(" ")
        if len(input_data) != 7:
            raise IncorrectRequest

        self.from_ = input_data[4]
        self.to = input_data[6]
        if self.from_ not in [entry.name for entry in self.storages]:
            raise StorageNotFound(storage_name=self.from_)
        elif self.to not in [entry.name for entry in self.storages]:
            raise StorageNotFound(storage_name=self.to)
        self.amount = int(input_data[1])
        self.product = input_data[2]

    def process_request(self):

        # в задаче был именно список, поэтому пришлось городить эти преобразования
        list_of_storage_names = [entry.name for entry in self.storages]

        self.amount = self.storages[list_of_storage_names.index(self.from_)].remove(item_name=self.product,
                                                                                    item_quantity=self.amount)

        print(f'Курьер забирает {self.amount} {self.product} из хранилища "{self.from_}"')
        print(f'Курьер везёт {self.amount} {self.product} в хранилище "{self.to}"')

        self.storages[list_of_storage_names.index(self.to)].add(item_name=self.product, item_quantity=self.amount)

        print(f'{Fore.LIGHTGREEN_EX}Курьер доставил {self.amount} {self.product} в хранилище "{self.to}"{Fore.RESET}\n')

    def rollback(self):

        list_of_storage_names = [entry.name for entry in self.storages]
        print(f'{Fore.LIGHTRED_EX}Курьер не смог выполнить доставку!{Fore.RESET}\n')
        self.storages[list_of_storage_names.index(self.from_)].add(item_name=self.product, item_quantity=self.amount)
        print(f'Курьер увёз {self.amount} {self.product} обратно в хранилище "{self.from_}"\n')
