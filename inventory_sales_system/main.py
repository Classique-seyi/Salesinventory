import math
products = []

def add_product():

    while True:
        try:
            product_id = int(input("Enter the product ID: "))
            if product_id <= 0:
                print("Product ID has to be positive")
                continue
            duplicate = False

            for product in products:
                if product["product_id"] == product_id:
                    duplicate = True

            if duplicate:
                print("Product already exists")
                continue
            break

        except ValueError:
            print("Invalid product ID")
            continue
    

    while True:
        name = input("Enter the name of the product: ").strip().capitalize()
        if not name:
            print("Name cannot be empty")
            continue
        break

    while True:
        category = input("Enter the category of the product: ").strip().capitalize()
        if not category:
            print("Category can't be empty")
            continue
        break

    while True:
        try:  
            cost_price = float(input("Enter the cost price of the product: "))
            if not math.isfinite(cost_price) or cost_price <= 0:
                print("Cost price has to be a valid positive value")
                continue
        except ValueError:
            print("Invalid cost price")
            continue
        break

    while True:
        try:
            selling_price = float(input("Enter the selling price of the product: "))
            if selling_price <= cost_price:
                print("Selling price should be higher than the cost")
                continue
            if not math.isfinite(selling_price) or selling_price <= 0:
                print("Selling price has to be a valid positive value")
                continue
        except ValueError:
            print("Invalid selling price")
            continue
        break

    while True:
        try:
            quantity = int(input("Enter the quantity of the product: "))
            if quantity <= 0:
                print("Quantity has to be positive")
                continue
        except ValueError:
            print("Invalid quantity")
            continue
        break

    while True:
        try:
            low_stock = int(input("Enter products with low stocks: "))
            if low_stock < 0:
                print("Low stock can't be negative")
                continue
        except ValueError:
            print("Invalid stock")
            continue
        break

    product = {
        "product_id": product_id,
        "name": name,
        "category": category,
        "cost_price": cost_price,
        "selling_price": selling_price,
        "quantity": quantity,
        "low_stock_threshold": low_stock
    }

    products.append(product)
    print("Products added successfully")

def view_product():
    if not products:
        print("No product to view")
        return

    print(f'''
======================================================== PRODUCTS LIST ================================================================================
''')

    print(f"{'PRODUCT ID':^10} | {'NAME':^20} | {'CATEGORY':^20} | {'COST PRICE(₦)':^15} | {'SELLING PRICE(₦)':^15} | {'QUANTITY':^15} | {'LOW STOCK THRESHOLD':^15}")
    
    for product in products:
        print(f"{product['product_id']:^10} | {product['name']:<20} | {product['category']:<20} | {product['cost_price']:>15.2f} | {product['selling_price']:>15.2f} | {product['quantity']:^15} | {product['low_stock_threshold']:^15}")

        if product['quantity'] <= product['low_stock_threshold']:
            print("LOW STOCK!!")

def search_product():
    if not products:
        print("Product list is empty")
        return
    try:
        product_number = int(input("Enter Product ID to search: "))
    except ValueError:
        print("Invalid product ID")
        
    for product in products:
        if product_number == product["product_id"]:
            print(product)
        
    print("Product not found")


def update_product():
    pass

def delete_product():
    pass

def record_sale():
    pass

def view_sales():
    pass

def business_reports():
    pass

def display_menu():
    return '''
=====================================
    INVENTORY & SALES MANAGEMENT     
=====================================

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Record Sale
7. View Sales History
8. Business Reports
9. Exit
'''

def main():
    menu = display_menu()

    while True:

        print(menu)

        choice = input("What would you like to do today: ").strip()

        if not choice:
            print("Your choice can't be empty")
            continue

        if choice == "1":
            add_product()

        elif choice == "2":
            view_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            record_sale()

        elif choice == "7":
            view_sales()

        elif choice == "8":
            business_reports()

        elif choice == "9":
            break

        else:
            print("Please input a valid menu option.")


main()