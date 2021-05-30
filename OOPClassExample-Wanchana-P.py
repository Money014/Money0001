class Customer:
     name = ""
     lastName = ""
     age = 0
     def aadCart(self):
         print("Added to",self.name,self.lastName+"'s Cart")
customer1 = Customer()
customer1.name = "Wanchana"
customer1.lastName = "Phuphansakun"
customer1.aadCart()

customer2 = Customer()
customer2.name = "A"
customer2.lastName = "1"
customer2.aadCart()

customer3 = Customer()
customer3.name = "A"
customer3.lastName = "2"
customer3.aadCart()

customer4 = Customer()
customer4.name = "A"
customer4.lastName = "3"
customer4.aadCart()
