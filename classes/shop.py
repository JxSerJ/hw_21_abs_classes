from classes.abstractions import Storage
from exceptions import InsufficientStorageCapacity, NotEmptyItem, ItemNotFound, InsufficientUniqueItemsCapacity
from colorama import Fore


class Shop(Storage):
    def __init__(self, name: str, items: dict[str, int], capacity: int = 20, unique_items_capacity: int = 5):
        self._name = name
        self._items = items
        self._capacity = capacity
        self._unique_items_capacity = unique_items_capacity

    def __repr__(self):
        new_line = '\n'
        return f'Наименование: {Fore.CYAN}{self.name}\n{Fore.RESET}' + \
               f'Содержимое: ' + \
               f'{new_line.join(["".rjust(14 - (len("Содержимое: ") if list(self.items.keys()).index(item) == 0 else 0), " ") + f"{Fore.YELLOW}" + (str(value) + f" {Fore.WHITE}" + item + f"{Fore.RESET}") for item, value in self.items.items()]) + new_line}'

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @property
    def unique_items_capacity(self):
        return self._unique_items_capacity

    def add(self, item_name: str, item_quantity: int):
        if self.get_free_space() < item_quantity:
            raise InsufficientStorageCapacity(storage_name=self.name, item_name=item_name,
                                              item_quantity=item_quantity, free_space=self.get_free_space())

        if item_name not in self.items:
            if self.unique_items_capacity == self.get_unique_items_count():
                raise InsufficientUniqueItemsCapacity(storage_name=self.name, item_name=item_name,
                                                      unique_items_space=self.unique_items_capacity)
            self.items[item_name] = item_quantity
        else:
            self.items[item_name] += item_quantity

    def remove(self, item_name: str, item_quantity: int):
        if item_name not in self.items:
            raise ItemNotFound(storage_name=self.name, item_name=item_name)
        elif self.items[item_name] < item_quantity:
            quantity = self.items[item_name]
            self.items[item_name] = 0
            self.remove_item_entry(item_name=item_name)
            return quantity
        else:
            self.items[item_name] -= item_quantity
            if self.items[item_name] == 0:
                self.remove_item_entry(item_name=item_name)
            return item_quantity

    def remove_item_entry(self, item_name: str):
        if item_name not in self.items:
            raise ItemNotFound(storage_name=self.name, item_name=item_name)
        elif self.items[item_name] != 0:
            raise NotEmptyItem(storage_name=self.name, item_name=item_name)
        self.items.pop(item_name)

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_free_space_unique_items(self) -> int:
        return self.unique_items_capacity - self.get_unique_items_count()

    def get_items(self) -> dict[str, int]:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)
