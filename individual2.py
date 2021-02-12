# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 18. Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

# Для варианта задания лабораторной работы 8 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON. Необходимо проследить за
# тем, чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
# работы.

# Выполнить индивидуальное задание 2 лабораторной работы 9, использовав классы данных,
# а также загрузку и сохранение данных в формат XML.

from dataclasses import dataclass, field
import sys
from typing import List
import xml.etree.ElementTree as ET
import json



@dataclass(frozen=True)
class market:
    shop: str
    product: str
    price: int


@dataclass
class Staff:
    markets: List[market] = field(default_factory=lambda: [])

    def add(self, shop, product, price):
        self.markets.append(
            market(
                shop=shop,
                product=product,
                price=price
            )
        )

        self.markets.sort(key=lambda market: market.shop)

    def __str__(self):
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Магазин",
                "Товар",
                "Стоимость в руб."
            )
        )
        table.append(line)

        for idx, market in enumerate(self.markets, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    market.shop,
                    market.product,
                    market.price
                )
            )
        table.append(line)

        return '\n'.join(table)

    def select(self):

        parts = command.split(' ', maxsplit=2)

        period = str(parts[1])

        count = 0

        for market in self.markets:
            if markets.get('shop') ==  period:
                count += 1
                print('Магазин:', market.shop)
                print('Продукт:', market.product)
                print('Цена:', market.price)

        if count == 0:
            print("Продукт не найден.")

        def load(self, filename):
            with open(filename, 'r', encoding='utf8') as fin:
                xml = fin.read()
            parser = ET.XMLParser(encoding="utf8")
            tree = ET.fromstring(xml, parser=parser)
            self.markets = []

            for market_element in tree:
                shop, product, price = None, None, None

                for element in market_element:
                    if element.tag == 'shop':
                        shop = element.text
                    elif element.tag == 'product':
                        product = element.text
                    elif element.tag == 'price':
                        price = element.text

                    if shop is not None and product is not None \
                            and price is not None:
                        self.markets.append(
                            markets(
                                shop=shop,
                                product=product,
                                price=price
                            )
                        )

        def save(self, filename):
            root = ET.Element('markets')
            for market in self.markets:
                market_element = ET.Element('market')

                shop_element = ET.SubElement(market_element, 'shop')
                shop_element.text = market.shop

                product_element = ET.SubElement(market_element, 'product')
                product_element.text = market.product

                price_element = ET.SubElement(market_element, ' price')
                price_element.text = (market.price)

                root.append(market_element)

            tree = ET.ElementTree(root)
            with open(filename, 'wb') as fout:
                tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    markets = []
    staff = Staff()

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            shop = input("Название магазина? ")
            product = input("Название товара? ")
            price = input("Стоимость товара в руб.? ")

            staff.add(shop, product, price)

        elif command == 'list':
            print(staff)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])

            count = 0

            for market in markets:
                if markets.get('shop') == sel:
                    count += 1
                    print('Названи магазина', market.shop)
                    print('Название товара:', market.product)
                    print('Стоимость в руб.:', markets.price)

            # Если счетчик равен 0, то продукты не найдены.
            if count == 0:
                print("Продукт не найден.")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                markets = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(markets, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <товар> - информация о товаре;")ad
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)