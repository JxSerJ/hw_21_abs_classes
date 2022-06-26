from classes import Store, Shop, Request
from exceptions import IncorrectRequest, StorageNotFound, ItemNotFound, NotEmptyItem, InsufficientStorageCapacity, \
    InsufficientUniqueItemsCapacity
from colorama import Fore

# Generating initial data
store_1 = Store(name='склад', items={'печеньки': 6, 'собачки': 4, 'коробки': 5, 'бананы': 50})
shop_1 = Shop(name='магазин', items={'печеньки': 2, 'собачки': 2, 'коробки': 1, 'вафельки': 1, 'мороженка': 2})

list_of_storages = [store_1, shop_1]

# User interface
if __name__ == '__main__':
    print("\nПриветствую! Эта программа передвигания товаров из одного хранилища в другое.\n\n"
          f"Для работы надо вводить запросы вида: \n{Fore.YELLOW}Доставить {Fore.GREEN}<количество> "
          f"<наименование товара> {Fore.YELLOW}из {Fore.GREEN}<наименование склада отправления> "
          f"{Fore.YELLOW}в {Fore.GREEN}<наименование склада назначения>{Fore.RESET}\n\n"
          f"Пример запроса: {Fore.YELLOW}Доставить {Fore.GREEN}3 собачки {Fore.YELLOW}из {Fore.GREEN}склад "
          f"{Fore.YELLOW}в {Fore.GREEN}магазин{Fore.RESET}\n"
          f"Так же по запросу \"{Fore.GREEN}хранилища{Fore.RESET}\" будет распечатано текущее состояние складов\n")
    print("В Вашем распоряжении находятся:\n")
    [print(entry) for entry in list_of_storages]

    while True:
        try:
            input_data = input('Запрос: ')
            if input_data.lower() == "хранилища":
                [print(entry) for entry in list_of_storages]
                continue

            request = Request(storages=list_of_storages, request_string=input_data)
            request.process_request()
            [print(entry) for entry in list_of_storages]

        except IncorrectRequest as err:
            print(err.message)
        except StorageNotFound as err:
            print(err.message)
        except ItemNotFound as err:
            print(err.message)
        except NotEmptyItem as err:
            print(err.message)
        except InsufficientStorageCapacity as err:
            print(err.message)
            request.rollback()
        except InsufficientUniqueItemsCapacity as err:
            print(err.message)
            request.rollback()
