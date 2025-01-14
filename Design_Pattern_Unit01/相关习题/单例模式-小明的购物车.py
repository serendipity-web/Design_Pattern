"""
小明去了一家大型商场，拿到了一个购物车，并开始购物。请你设计一个购物车管理器，记录商品添加到购物车的信息（商品名称和购买数量），并在购买结束后打印出商品清单。（在整个购物过程中，小明只有一个购物车实例存在）。
"""
import sys


class ShoppingCar:
    instance = None
    def __init__(self):
        if ShoppingCar.instance is not None:
            raise Exception("Can not create more instance")
        ShoppingCar.instance = self
        self.goods_numbers = {}

    def add_goods(self, goods_name, goods_number):
        if goods_name not in self.goods_numbers:
            self.goods_numbers[goods_name] = 0
        self.goods_numbers[goods_name] += goods_number

    def show_goods(self):
        for goods_name, goods_number in self.goods_numbers.items():
            print(f"{goods_name} {goods_number}")

if __name__ == "__main__":
    car = ShoppingCar()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        item_name, quantity = line.split()
        quantity = int(quantity)
        car.add_goods(item_name, quantity)
    car.show_goods()

