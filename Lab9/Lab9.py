class Mall:
    def __init__(self):
        print("Calculate product price and discount")
        self.product_price = int(input("Price of all products you purchase (THB): "))

    def calculate_discount(self):
        if self.product_price > 15000 :
            self.dis = self.product_price * 40 / 100
            self.dis_per = 40
        elif self.product_price > 8001:
            self.dis = self.product_price * 30 / 100
            self.dis_per = 30
        elif self.product_price > 3000 :
            self.dis = self.product_price * 20 / 100
            self.dis_per = 20
        else:
            self.dis = self.product_price * 10 / 100
            self.dis_per = 10

        self.price_dis = self.product_price - self.dis

    def display_info(self):
        print("--------------------------------------------------")
        print(f"Product prices before discount: {int(self.product_price)}")
        print(f"discount percentage : {self.dis_per}% ")
        print(f"Product discount: {self.dis}")
        print(f"Product price after discount: {self.price_dis:.1f}")
        print("--------------------------------------------------")

mall_instance = Mall()
mall_instance.calculate_discount()
mall_instance.display_info()
