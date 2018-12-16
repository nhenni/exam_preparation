# EXAM PREPARATION PRACTICE ASSESSMENT EXAM INFORMATICS I
# 13. Dezember 2016

class Product:
    product_code = 0

    def __init__(self, price):
        self.__price = price
        self.tax = self.__price * 0.07
        self.code_id = Product.code()

    def get_total_price(self):
        total = self.__price + self.tax
        return "{} {} CHF".format(self.code_id, total)

    @staticmethod
    def code():
        code_id = Product.product_code
        Product.product_code += 1
        return code_id


p1 = Product(50)
p2 = Product(100)
print(p1) # prints 0 53.5 CHF # it doesn't work
print(p2) # prints 1 107.0 CHF

print(p1.get_total_price()) # works with this though, but why?
print(p2.get_total_price())