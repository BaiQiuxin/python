# 向哲煜 2024.2.9

sandwiches_orders = ['ham', 'pastrami', 'pork', 'pastrami', 'beef', 'pastrami', 'tuna']
finished_sandwiches = []

print("Sorry, pastrami sandwiches are sold out.")

while 'pastrami' in sandwiches_orders:
    sandwiches_orders

while sandwiches_orders:
    sandwiches_order = sandwiches_orders.pop()
    print(f"I made you {sandwiches_order} sandwich.")
    finished_sandwiches.append(sandwiches_order)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)