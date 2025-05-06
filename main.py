class Item:

    def __init__(self, name:str, price:float, quantity=0):

        assert price>=0, f'price {price} is not greater than equal to zero!'
        assert quantity>=0, f'quantity {quantity} is not greater than equal to zero!'

        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_pay_amount(self):
        return self.price*self.quantity
    

#if __name__=='__main__':
item1 = Item('laptop',1000,1)
print(item1.calculate_pay_amount())
        
