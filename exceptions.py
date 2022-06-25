class BaseStorageError(Exception):
    def __init__(self, storage_name: str, item_name: str):
        self.storage_name = storage_name
        self.item_name = item_name


class InsufficientStorageCapacity(BaseStorageError):
    """
    Error raised in case of insufficient storage capacity
    """
    def __init__(self, storage_name: str, item_name: str, item_quantity: int, free_space: int):
        super().__init__(storage_name=storage_name, item_name=item_name)
        self.item_quantity = item_quantity
        self.free_space = free_space

        self.message = self.message_constructor()

    def message_constructor(self):
        message = f"Недостаточно места в хранилище: {self.storage_name}\n" \
                  f"Доступно места: {self.free_space}\n" \
                  f"Уменьшите количество добавляемых товаров \"{self.item_name}\" на " \
                  f"{self.item_quantity - self.free_space}"
        return message


class NotEmptyItem(BaseStorageError):
    """
    Error raised in case of item quantity in storage is not empty
    """
    def __init__(self, storage_name: str, item_name: str):
        super().__init__(storage_name=storage_name, item_name=item_name)

        self.message = self.message_constructor()

    def message_constructor(self):
        message = f"Позиция \"{self.item_name}\" в хранилище \"{self.storage_name}\" не пуста!\n" \
                  f"Удаление невозможно! Сначала очистите позицию в хранилище."
        return message


class ItemNotFound(BaseStorageError):
    """
    Error raised if item not found in storage
    """
    def __init__(self, storage_name: str, item_name: str):
        super().__init__(storage_name=storage_name, item_name=item_name)

        self.message = self.message_constructor()

    def message_constructor(self):
        message = f"Позиция \"{self.item_name}\" не найдена в хранилище \"{self.storage_name}\"."
        return message
