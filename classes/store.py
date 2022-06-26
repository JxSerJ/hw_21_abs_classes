from classes.abstractions import Storage
from exceptions import InsufficientStorageCapacity, NotEmptyItem, ItemNotFound
from colorama import Fore


class Store(Storage):
    def __init__(self, name: str, items: dict[str, int], capacity: int = 100):
        self._name = name
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        new_line = '\n'
        return f'Наименование: {Fore.CYAN}{self.name}\n{Fore.RESET}' + \
               f'Содержимое: ' + \
               f'{new_line.join(["".rjust(14-(len("Содержимое: ") if list(self.items.keys()).index(item)==0 else 0), " ") + f"{Fore.YELLOW}" + (str(value) + f" {Fore.WHITE}" + item + f"{Fore.RESET}") for item, value in self.items.items()]) + new_line}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, item_name: str, item_quantity: int):
        try:
            if self.get_free_space() < item_quantity:
                raise InsufficientStorageCapacity(storage_name=self.name, item_name=item_name,
                                                  item_quantity=item_quantity, free_space=self.get_free_space())
            if item_name not in self.items:
                self.items[item_name] = item_quantity
            self.items[item_name] += item_quantity

        except InsufficientStorageCapacity as err:
            print(err.message)

    def remove(self, item_name: str, item_quantity: int):
        try:
            if item_name not in self.items:
                raise ItemNotFound(storage_name=self.name, item_name=item_name)
            elif self.items[item_name] < item_quantity:
                self.items[item_name] = 0
            else:
                self.items[item_name] -= item_quantity

        except ItemNotFound as err:
            print(err.message)

    def remove_item_entirely(self, item_name: str):
        try:
            if item_name not in self.items:
                raise ItemNotFound(storage_name=self.name, item_name=item_name)
            elif self.items[item_name] != 0:
                raise NotEmptyItem(storage_name=self.name, item_name=item_name)
            self.items.pop(item_name)

        except NotEmptyItem as err:
            print(err.message)
        except ItemNotFound as err:
            print(err.message)

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_items(self) -> dict[str, int]:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)
