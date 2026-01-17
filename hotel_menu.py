menu = {
    'pizza': 120,
    'pasta': 150,
    'burger': 100,
    'salad': 80,
    'coffee': 180,
    'tea': 50,
    'cold coffee': 75,
    'cheese burger': 200
}

print("---------- Welcome To Python Restaurant ----------")
print("pizza: Rs 120\npasta: Rs 150\nburger: Rs 100\nsalad: Rs 80\ncoffee: Rs 180\ntea: Rs 50\ncold coffee: Rs 75\ncheese burger: Rs 200")
print("\n(Type 'exit' to finish ordering)")

order_total = 0

while True:
    item = input("\nEnter item name: ").lower()

    if item == "exit":
        break

    if item in menu:
        order_total += menu[item]
        print(f"------- {item} added to your order -------")
    else:
        print(f"-------❌ {item} is not available Yet! -------")

print(f"\nThe Total Amount Of Items Is ₹{order_total} 💸")
print("\nThank You! Visit Again, Have A Nice Day. 😊")
