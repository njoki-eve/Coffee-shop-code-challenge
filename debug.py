from customer import Customer
from coffee import Coffee
from order import Order

# --- Create Customers ---
alex = Customer("Alex")
brian = Customer("Brian")

# --- Create Coffees ---
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# --- Create Orders ---
order1 = alex.create_order(latte, 3.5)
order2 = alex.create_order(espresso, 4.0)
order3 = brian.create_order(latte, 5.0)

# --- Check Relationships ---
print("\n--- Customer Orders ---")
print([o.price for o in alex.orders()])  # Fixed: Changed alice.orders() to alice.orders
print([c.name for c in alex.coffees()])  # Fixed: Changed alice.coffees() to alice.coffees

print("\n--- Coffee Orders ---")
print([o.price for o in latte.orders()])  # Fixed: Changed latte.orders() to latte.orders
print([c.name for c in latte.customers()])  # Fixed: Changed latte.customers() to latte.customers

print("\n--- Coffee Aggregates ---")
print(latte.num_orders())  # Should show 2
print(latte.average_price())  # Should show 4.25

if latte.num_orders() > 0:
    print(latte.average_price())
else:
    print("No orders for Latte.")

print("\n--- Aficionado Check ---")
aficionado = Customer.most_aficionado(latte)
print(aficionado.name if aficionado else "No aficionado")  # Should show Bob

# --- Error Handling Examples ---
print("\n--- Error Handling ---")
try:
    bad_customer = Customer("ThisNameIsWayTooLong")
except ValueError as e:
    print(e)

try:
    bad_coffee = Coffee("Yo")
except ValueError as e:
    print(e)

try:
    bad_order = Order(alex, latte, 20.0)  # Invalid price
except ValueError as e:
    print(e)