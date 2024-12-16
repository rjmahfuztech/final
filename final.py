class Restaurant:
    food_items = []
    customers_account = []
    
    def show_food_items(self):
        print("****Restaurant Menu****")
        print("Name:\tPrice:")
        for item in self.food_items:
            print(f'{item['name']}\t{item['price']}$')
    
class Admin(Restaurant):
    admin_name = 'Admin'

    def add_food_item(self, name,price):
        food_item = {"name" : name, "price": price}
        self.food_items.append(food_item)
    
    def update_food_item(self,name,price):
        for item in self.food_items:
            if item['name'] == name:
                item['name'] = name
                item['price'] = price

    def remove_food_item(self,name):
        for item in self.food_items:
            if item['name'] == name:
                self.food_items.remove(item)

    def create_customer_account(self,name,email,address):
        customer_info = {"name" : name, "email" : email, "address" : address, "balance" : 0}
        self.customers_account.append(customer_info)
    
    def show_all_customers(self):
        print("Name:\tEmail:\t\tAddress:")
        for customer in self.customers_account:
            print(f'{customer['name']}\t{customer['email']}\t{customer['address']}')

    def remove_customer_account(self,email):
        for account in self.customers_account:
            if account['email'] == email:
                self.customers_account.remove(account)

class Customer(Restaurant):
    def __init__(self):
        self.order = []

    def view_balance(self,customer_name):
        for customer in self.customers_account:
            if customer['name'] == customer_name:
                print(f"Welcome '{customer_name}' in your account!!!")
                print(f'Your available balance is: {customer['balance']}$')
                break
    
    def add_balance(self,customer_name,amount):
        for customer in self.customers_account:
            if customer['name'] == customer_name:
                customer['balance'] += amount
                print(f"You add: {amount}$ and now your balance is: {customer['balance']}$")


admin = Admin()
admin.add_food_item("Apple",15)
admin.add_food_item("Coconut",90)
admin.add_food_item("Orange",25)
admin.add_food_item("Banana",15)
admin.add_food_item("Mango",8)

admin.create_customer_account("Rohim","rohim@gmail.com","Dhaka")
admin.create_customer_account("Korim","korim@gmail.com","Khulna")
admin.create_customer_account("Sojib","sojib@gmail.com","Borishal")
admin.create_customer_account("Ratul","ratul@gmail.com","Dinajpur")


# admin.show_food_items()
# admin.remove_food_item("Orange")
# admin.show_food_items()

# admin.show_all_customers()
# admin.remove_customer_account("sojib@gmail.com")
# admin.show_all_customers()

customer1 = Customer()
# customer1.view_balance("Ratul")
# customer1.add_balance("Ratul",750)
# customer1.add_balance("Ratul",50)




