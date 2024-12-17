class Restaurant:
    food_items = []
    customers_account = []
    
    def show_food_items(self):
        print("---- Restaurant Menu ----")
        print("Name:\tPrice:")
        for item in self.food_items:
            print(f'{item['name']}\t{item['price']}$')

    def find_food(self,name):
        for item in self.food_items:
            if item['name'] == name:
                return item
        return None
    
    def find_customer(self,name):
        for customer in self.customers_account:
            if customer['name'] == name or customer['email'] == name:
                return customer
        return None
    
class Admin(Restaurant):
    admin_name = 'Admin'

    # def find_food(self,name):
    #     for item in self.food_items:
    #         if item['name'] == name:
    #             return item
    #     return None
    
    # def find_customer(self,name):
    #     for customer in self.customers_account:
    #         if customer['name'] == name or customer['email'] == name:
    #             return customer
    #     return None

    def add_food_item(self, name,price):
        food_item = {"name" : name, "price": price}
        self.food_items.append(food_item)
        print(f"Item: '{name}' added successfully")
    
    # def update_food_item(self,name,price):
    #     for item in self.food_items:
    #         if item['name'] == name:
    #             item['price'] = price
    #             print(f"Item price: '{price}$' updated successfully")
    #             break
    def update_food_item(self,name,price):
        item = self.find_food(name)
        if item:
            item['price'] = price
            print(f"Item price: '{price}$' updated successfully")
        else:
            print(f"Sorry!! Item: '{name}' not found for update!")

    # def remove_food_item(self,name):
    #     for item in self.food_items:
    #         if item['name'] == name:
    #             self.food_items.remove(item)
    #             print(f"Item: '{name}' removed successfully")
    #             break
    def remove_food_item(self,name):
        item = self.find_food(name)
        if item:
            self.food_items.remove(item)
            print(f"Item: '{name}' removed successfully")
        else:
            print(f"Sorry!! Item: '{name}' not found for remove!")


    def create_customer_account(self,name,email,address):
        customer_info = {"name" : name, "email" : email, "address" : address, "balance" : 0, "orders" : []}
        self.customers_account.append(customer_info)
        print(f"Customer account: '{name}' created successfully")
    
    def show_all_customers(self):
        print("Name:\tEmail:\t\tAddress:")
        for customer in self.customers_account:
            print(f'{customer['name']}\t{customer['email']}\t{customer['address']}')

    # def remove_customer_account(self,email):
    #     for account in self.customers_account:
    #         if account['email'] == email:
    #             self.customers_account.remove(account)
    #             print(f"Customer account: '{account['name']}' removed successfully")
    def remove_customer_account(self,email):
        account = self.find_customer(email)
        if account:
            self.customers_account.remove(account)
            print(f"Customer account: '{account['name']}' removed successfully")
        else:
            print(f"Sorry!! Account: '{email}' not found for remove a customer!")


class Customer(Restaurant):

    # def view_balance(self,customer_name):
    #     for customer in self.customers_account:
    #         if customer['name'] == customer_name:
    #             print(f"Welcome '{customer_name}' in your account!!!")
    #             print(f'Your available balance is: {customer['balance']}$')
    #             break
    def view_balance(self,customer_name):
        customer = self.find_customer(customer_name)
        print(f"Welcome '{customer_name}' in your account!!!")
        print(f'Your available balance is: {customer['balance']}$')
    
    # def add_balance(self,customer_name,amount):
    #     for customer in self.customers_account:
    #         if customer['name'] == customer_name:
    #             customer['balance'] += amount
    #             print(f"You add: {amount}$ and now your balance is: {customer['balance']}$")
    #             break
    def add_balance(self,customer_name,amount):
        customer = self.find_customer(customer_name)
        customer['balance'] += amount
        print(f"You add: {amount}$ and now your balance is: {customer['balance']}$")
    
    # def place_order(self,customer_name,item_name):
    #     for customer in self.customers_account:
    #         if customer['name'] == customer_name:
    #             for item in self.food_items:
    #                 if item['name'] == item_name:
    #                     if item['price'] <= customer['balance']:
    #                         customer['orders'].append(item)
    #                         customer['balance'] -= item['price']
    #                         print(f"Your Order: '{item_name}' Placed Successfully!!")
    #                         break
    #                     else:
    #                         print(f"Sorry!! Item price is: {item['price']}$ but you have: {customer['balance']}$")
    #                         break
    #             break
    def place_order(self,customer_name,item_name):
        customer = self.find_customer(customer_name)
        item = self.find_food(item_name)
        if item:
            if item['price'] <= customer['balance']:
                customer['orders'].append(item)
                customer['balance'] -= item['price']
                print(f"Your Order: '{item_name}' Placed Successfully!!")
            else:
                print(f"Sorry!! Item price is: {item['price']}$ but you have: {customer['balance']}$, Please recharge your account!")
        else:
            print(f"Sorry!! Item: '{item_name}' not found for placing an order!")
    
    # def view_past_orders(self,customer_name):
    #     for customer in self.customers_account:
    #         if customer['name'] == customer_name:
    #             if len(customer['orders']) >= 1:
    #                 print("Your Previous Orders:")
    #                 print("Item name:\tPrice:")
    #                 for item in customer['orders']:
    #                     print(f'{item['name']}\t\t{item['price']}$')
    #             else:
    #                 print("You didn't Order anything Yet!!")
    def view_past_orders(self,customer_name):
        customer = self.find_customer(customer_name)
        if len(customer['orders']) >= 1:
            print("Your Previous Orders:")
            print("Item name:\tPrice:")
            for item in customer['orders']:
                print(f'{item['name']}\t\t{item['price']}$')
        else:
            print("You didn't Order anything Yet!!")


def admin_menu():
    while True:
        print("----- Admin Menu -----")
        print("1. Create Customer Account")
        print("2. Remove Customer Account")
        print("3. View All Customers")
        print("4. Manage Restaurant Menu")
        print("5. Exit")
        admin = Admin()
        option = int(input("Select an option: "))
        if option == 1:
            name = input('Enter name: ')
            email = input('Enter email: ')
            address = input('Enter address: ')
            admin.create_customer_account(name,email,address)
        elif option == 2:
            email = input('Enter email: ')
            admin.remove_customer_account(email)
        elif option == 3:
            admin.show_all_customers()
        elif option == 4:
            while True:
                print("1. Show all items")
                print("2. Add new item")
                print("3. Remove an item")
                print("4. Update an item")
                print("5. Exit")
                choice = int(input("Select an option: "))
                if choice == 1:
                    admin.show_food_items()
                elif choice == 2:
                    name = input('Enter item name: ')
                    price = int(input('Enter item price: '))
                    admin.add_food_item(name,price)
                elif choice == 3:
                    name = input('Enter item name: ')
                    admin.remove_food_item(name)
                elif choice == 4:
                    name = input('Enter item name: ')
                    price = int(input('Enter new price to update: '))
                    admin.update_food_item(name,price)
                elif choice == 5:
                    break
                else:
                    print("Invalid option choice!! Please Insert the correct one.")
        elif option == 5:
            break
        else:
            print("Invalid option choice!! Please Insert the correct one.")

def customer_menu(customer_name):
    while True:
        print(f"----- {customer_name}'s Menu -----")
        print("1. View Restaurant Menu")
        print("2. View Balance")
        print("3. Add Balance")
        print("4. Place Order")
        print("5. View Past Order")
        print("6. Exit")
        customer = Customer()
        option = int(input("Select an option: "))
        if option == 1:
            customer.show_food_items()
        elif option == 2:
            customer.view_balance(customer_name)
        elif option == 3:
            amount = int(input("Enter amount you want to add: "))
            customer.add_balance(customer_name,amount)
        elif option == 4:
            item_name = input('Enter item name: ')
            customer.place_order(customer_name,item_name)
        elif option == 5:
            customer.view_past_orders(customer_name)
        elif option == 6:
            break
        else:
            print("Invalid option choice!! Please Insert the correct one.")


# Demo Food Items
admin_access = Admin()
admin_access.add_food_item('apple',20)
admin_access.add_food_item('orange',35)
admin_access.add_food_item('banana',12)

while True:
    print("----- Restaurant Management System -----")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")
    admin = Admin()
    option = int(input("Select an option: "))
    if option == 1:
        print("Please type: 'Admin' to get admin access")
        admin_name = input("Enter your name: ")
        if admin_name == admin.admin_name:
            admin_menu()
        else:
            print(f"Sorry '{admin_name}' you are no a Admin!!")
    elif option == 2:
        # customer_name = input("Enter your name: ")
        # flag = False
        # for customer in admin.customers_account:
        #     if customer['name'] == customer_name:
        #         flag = True
        #         break
        # if flag == True:
        #     customer_menu(customer_name)
        # else:
        #     print(f"Sorry '{customer_name}' you don't have any account!!")
        #     print("Request to Admin for create a account for you!")
        customer_name = input("Enter your name: ")
        customer = admin.find_customer(customer_name)
        if customer:
            customer_menu(customer_name)
        else:
            print(f"Sorry '{customer_name}' you don't have any account!!")
            print("Request to Admin for create a account for you!")
    elif option == 3:
        break
    else:
        print("Invalid option choice!! Please Insert the correct one.")
