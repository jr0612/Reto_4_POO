class MenuItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def set_name(self, name):
        self.__name = name
    
    def set_price(self, price):
        self.__price = price



class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        self._size = size


class Appetizer(MenuItem):
    def __init__(self, name, price, servings):
        super().__init__(name, price)
        self.__servings = servings
    
    def get_servings(self):
        return self.__servings

    def set_servings(self, servings):
        self.__servings = servings


class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients: list):
        super().__init__(name, price)
        self._ingredients = ingredients
    
    def get_ingredients(self):
        return self._ingredients
    
    def set_ingredients(self, ingredients: list):
        self._ingredients = ingredients


class Order:
    def __init__(self):
        self.items = []
        

    def add_item(self, item: MenuItem, quantity=1):
        self.items.append((item, quantity))

    def calculate_total_price(self, item: MenuItem, quantity):
        return item.get_price() * quantity
    
    def apply_combo_discount(self):
        #this combo decrement the quantity of one beverage by 1 if the order contains at least 2 main courses, 2 appetizers and 1 beverage
        main_courses = 0
        appetizers = 0
        beverages = 0
        for item , quantity in self.items:
            if isinstance(item,MainCourse):
                main_courses += quantity
            elif isinstance(item, Appetizer):
                appetizers += quantity
            elif isinstance(item, Beverage):
                beverages += quantity
        
       
        if main_courses >= 2 and appetizers >= 2 and beverages >= 1:
            for i, (item, quantity) in enumerate(self.items):
                if isinstance(item, Beverage):
                    self.items[i] = (item, quantity-1)
                    break



              
    def __calculate_total_bill(self):
        total_bill = 0
        self.apply_combo_discount()


        for item, quantity in self.items:
            total_bill += order.calculate_total_price(item, quantity)
        
        if total_bill >= 50:
            discount = total_bill * 0.1  
            total_bill -= discount
        

        
        
        return total_bill
    def get_total_bill(self):
        return self.__calculate_total_bill
    def set_total_bill(self, total_bill):
        self.__calculate_total_bill = total_bill
    
class Payment:
    def __init__(self) -> None:
        pass
        
    def pay(self, total_bill):
        raise NotImplementedError("Subclass should implement pay()")
    

class CreditCard(Payment):
    def __init__(self, number: int, cvv: int) -> None:
        super().__init__()
        self.number = number
        self.cvv = cvv
    def pay(self, total_bill):
        print(f"Paying $ {total_bill} with credit card {str(self.number)[-4:]}")
        return True


class Cash(Payment):
    def __init__(self, cash_received: float) -> None:
        super().__init__()
        self.cash_received = cash_received
    def pay(self, total_bill):
        if self.cash_received >= total_bill:
            print(f"Payment successfully processed.\nChange: ${round(self.cash_received - total_bill, 2)}")
            return True

        else:
            print(f"Insufficient funds to complete the payment. Needed: ${round(total_bill - self.cash_received, 2):.2f} to complete the payment.")
            return False



if __name__ == "__main__":
    
    cola = Beverage("Cola", 2, "Medium")
    wings = Appetizer("Chicken Wings", 9, 10)
    steak = MainCourse("Steak", 16, ["Beef", "Potatoes", "Vegetables"])

   
    order = Order()
    order.add_item(cola, 2)
    order.add_item(wings , 2)
    order.add_item(steak, 2)



    total_bill = order.get_total_bill()()
    print("Total Bill: $", total_bill)
    
    pay = CreditCard(12314234,52)
    pay.pay(total_bill)
