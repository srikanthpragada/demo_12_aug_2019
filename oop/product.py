class Product:
    taxrate = 12

    @staticmethod
    def set_taxrate(newrate):
        Product.taxrate = newrate

    def __init__(self, id,name,price):
        self.id = id
        self.name = name
        self.price = price

    def print_details(self):
        print(self.id)
        print(self.name)
        print(self.price)

    @property
    def net_price(self):
        return  self.price + self.price * Product.taxrate / 100

p = Product(1,"Laptop",40000)
print(p.net_price)