"""
A simple python sales management system
1. View Products
2. Add New Product
3. Record Sales
4. View Sales
5. Generate Sales Summary
"""
# Shop product details
products= [
    {'name': 'Bread', 'price': 70, 'stock': 12},
    {'name': 'Milk', 'price':90, 'stock':50 },
    {'name': 'Sugar', 'price': 150, 'stock':30},
    
]

# Initial sales
sales= []

# view_products
products= [
    {'name': 'Bread', 'price': 70, 'stock': 12},
    {'name': 'Milk', 'price':90, 'stock':50 },
    {'name': 'Sugar', 'price': 150, 'stock':30},
    
]
print("--------View_products-------")
def view_products():
    for product in products:
        print(f"Product Name: {product['name']} | Price: {product['price']} | Stock {product['stock']}")
view_products()

# add_product()
print("------add_product-------")
def add_product():
    product_name= input("Enter product name: ")
    price = float(input("Enter price: "))
    stock= int(input("Enter stock: "))
    for product in products:
        if product_name.lower() == product['name'].lower():
            print(product_name, "already exists!")
            return
    new_product = {
        'name': product_name,
        'price': price,
        'stock': stock
    }
    products.append(new_product)
    print(product_name, "added.")
    
add_product()    
    

# view_sales()
print("-------view_sales---------")
def view_sales():
    product_name= input("Enter product name: ")
    price = float(input("Enter price: "))
    stock= int(input("Enter stock: "))
for s in sales:
    print(s['name'], '- Total:', s['total_sale'])
view_sales()



# record_sales()
print('--------record_sales---------')
def record_sales():
    product_name= input("Enter Product Name: ")
    for product in products:
        if product_name.lower() == product['name'].lower():
            quantity= int(input("Enter quantity: "))
            total= quantity * product['price']
            product['stock'] -= quantity
            sale={
                'product_name': product['name'],
                'quantity': quantity,
                'total_sale': total
            }
            sales.append(sale)
            return
    print('Product not found!!')
record_sales()    
# sales_summary()
print('--------sales_summary-------')
def sales_summary():
    total_revenue = 0
    for sale in sales:
        
        print(f"Product Name: {sale['product_name']} | Quantity: {sale['quantity']} | Total Sales: {sale['total_sale']}")
        total_revenue += sale['total_sale']
    print("Total Revenue", total_revenue)
sales_summary()
    
    
        
            