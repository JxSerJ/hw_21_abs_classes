from abc import ABC, abstractmethod


class Storage(ABC):
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self, item_name: str, item_quantity: int):
        """
        Adds determined quantity of items into storage based on item name and quantity.

        :param item_name: item name which will be added
        :param item_quantity: item quantity which will be added
        :return: None
        """
        pass

    @abstractmethod
    def remove(self, item_name: str, item_quantity: int):
        """
        Removes determined quantity of items from storage based on item name and quantity.

        :param item_name: item name which will be removed
        :param item_quantity: item quantity which will be removed
        :return: None
        """
        pass

    @abstractmethod
    def remove_item_entirely(self, item_name: str):
        """
        Removes item from storage database. Works only if item quantity = 0

        :param item_name: Name of the item which you want to remove form storage
        :return: None
        """
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """
        Returns storage free space

        :return: int storage free space
        """
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        """"
        Returns storage content

        :return: storage content in dict {item name: quantity}
        """
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        Returns unique items count

        :return: int count of items
        """
        pass
