# Simple Grocery Bill Generator with GST
# Finance & Retail Domain – VITyarthi Project
from datetime import datetime

print("✦" * 25)
print("    QUICK MART GROCERY STORE")
print("✦" * 25)

# Item code → [Name, Price, GST%]
menu = {
    1: ["Rice 5kg",         450,  5],
    2: ["Wheat Flour 10kg",  380,  0],
    3: ["Sugar 5kg",         220,  5],
    4: ["Cooking Oil 5L",    720,  5],
    5: ["Milk 1L",            68,  0],
    6: ["Maggi 12 packet",   144, 12],
    7: ["Lux Soap",           45, 18],
    8: ["Dal 1kg",           195,  5]
}

cart = []
total_items = 0
subtotal = 0

while True:
    print("\n" + "="*45)
    print("CODE  ITEM NAME           PRICE   GST")
    print("-"*45)
    for code, item in menu.items():
        print(f"{code:<4}  {item[0]:<18} ₹{item[1]:<6}  {item[2]}%")
    print("-"*45)
    print("0   → Generate Bill & Exit")
    
    choice = int(input("\nEnter item code (0 to finish): "))
    
    if choice == 0:
        break
    if choice not in menu:
        print("Wrong code! Try again.")
        continue
    
    qty = int(input(f"How many {menu[choice][0]} ? "))
    name, price, gst = menu[choice]
    amount = price * qty
    gst_amount = amount * gst / 100
    total = amount + gst_amount
    
    cart.append([name, price, qty, gst, total])
    subtotal += amount
    total_items += qty
    print("Added to cart!")

# ============ FINAL BILL ============
if len(cart) == 0:
    print("\nNo items bought. Thank you!")
else:
    total_gst = 0
    grand_total = 0
    
    print("\n" + "═"*55)
    print("                FINAL BILL")
    print("═"*55)
    print(f"Date: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
    print("-"*55)
    print(f"{'ITEM':<18} {'PRICE':>6} {'QTY':>4} {'GST':>5} {'TOTAL':>10}")
    print("-"*55)
    
    for item in cart:
        total_gst += item[1] * item[2] * item[3] / 100
        grand_total += item[4]
        print(f"{item[0]:<18} ₹{item[1]:>5} {item[2]:>4}  {item[3]:>3}% ₹{item[4]:>9.2f}")
    
    print("-"*55)
    print(f"{'Subtotal':<38} ₹{subtotal:>10.2f}")
    print(f"{'Total GST':<38} ₹{total_gst:>10.2f}")
    print(f"{'GRAND TOTAL':<38} ₹{grand_total:>10.2f}")
    print("═"*55)
    print("         THANK YOU! VISIT AGAIN ")
    print("═"*55)

input("\nPress Enter to close...")