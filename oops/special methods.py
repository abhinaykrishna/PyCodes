class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
p1=Product('Iphone',1000)
print(p1)

# The details of the object will be printed because, no functionality is defined for printing an object. The functionality can be defined using a special method called as __str__ method. This method should always return a string.

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
      return self.name + ' ' + str(self.price)

p1=Product('Iphone',1000)
print(p1)


# class Product:
#     counter=100
#     def __init__(self,name,description,brand,price):
#         Product.counter+=1
#         self.id='P'+str(Product.counter)
#         self.name=name
#         self.description=description
#         self.brand=brand
#         self.price=price
#     def purchase(self):
#         total_amount=self.price
#         total_amount+=0.05*total_amount
#         print('Product ID:',self.id)
#         print('Product Name:',self.name)
#         print('Price:',self.price)
#         print('Tax Amount:',total_amount-self.price)
#         print('Grand Total:',total_amount)
#         print('Thanks for the purchase.\n')
# product1=Product('IPhone','A mobile device with 4GB memory and 64GB Storage space which supprots 4G Network','Apple',72500.25)
# product2=Product('Air Max','A Sport Shoe','Nike',1280.0)
# product1+product2

# This is because, we did not define any logic for the + operator in our user defined class Product.

# We have some special function like __add__(), __sub()__, __mul__() to define the functionality of operators.

class Product:
    counter=100
    def __init__(self,name,description,brand,price):
        Product.counter+=1
        self.id='P'+str(Product.counter)
        self.name=name
        self.description=description
        self.brand=brand
        self.price=price
    def __add__(self,other):
        return self.price+other.price

product1=Product('IPhone','A mobile device with 4GB memory and 64GB Storage space which supprots 4G Network','Apple',72500.25)
product2=Product('Air Max','A Sport Shoe','Nike',1280.0)
print(product1+product2)
