# ---------------------Exercise 7.1--------------------

prompt = "What type of rental car will you want? "
car = input(prompt)

print(f"Let me see if I can find you a {car}")

# ---------------------Exercise 7.2--------------------

# waiter = "How many people are in you dinner group? "
# response = int(input(waiter))
#
# if response >= 8:
#     print("Sorry you will have to wait for a dinner table")
# else:
#     print("Your table is ready")

# ---------------------Exercise 7.3--------------------

# prompt = "Enter any number: "
# number = int(input(prompt))
# if number % 10 == 0:
#   print(f'{number} is a multiply of 10')
# else:
#   print(f"{number} is not a multiple of 10")

# ---------------------Exercise 7.4--------------------
# prompt = "\nHello Customers, welcome to Ada fries."
# prompt += "\nPlease enter pizza toppings, and enter 'quit' to send the order. "
# message = ""
#
# while True:
#     message  = input(prompt)
#     if message != 'quit':
#         print(f"{message} added to pizza")
#     else:
#         break

# ---------------------Exercise 7.5--------------------

# prompt = 'Welcome to Cooper Threater! Please enter your age: '
#
# while True:
#     age = int(input(prompt))
#     if age < 3:
#         print("You have a free ticket")
#     elif age <= 12:
#         print("Ticket cost $10")
#     elif age > 12:
#         print("Ticket cost $15")
#     break

# ---------------------Exercise 7.6--------------------

# Already implemented in 7.5

# ---------------------Exercise 7.7--------------------
# Please Note: This loop runs till infinity.

# infinity = True
#
# while infinity:
#     print("Looping forever")


# ---------------------Exercise 7.8--------------------

# sandwich_orders = ['Beef', 'Chicken', 'Cheese']
# finished_sandwiches = []
#
# while sandwich_orders:
#     orders = sandwich_orders.pop()
#     finished_sandwiches.append(orders)
#     print(f'I made your {orders} sandwich')
#
# print("\n---------------List of  Prepared Sandwiches---------------")
# print(f'The following sandwiches were made: ')
# for finished_sandwich in finished_sandwiches:
#     print(f'\t{finished_sandwich}')


# ---------------------Exercise 7.9--------------------

# sandwich_orders = ['Pastrami','Beef', 'Chicken', 'Pastrami','Pastrami','Cheese']
# finished_sandwiches = []
#
# while 'Pastrami' in sandwich_orders:
#     sandwich_orders.remove('Pastrami')
#     print('Deli has run out of pastrami,')
#
# while sandwich_orders:
#     orders = sandwich_orders.pop()
#     finished_sandwiches.append(orders)
#     print(f'I made your {orders} sandwich')
# print("\n---------------List of  Prepared Sandwiches---------------")
# print(f'The following sandwiches were made: ')
# for finished_sandwich in finished_sandwiches:
#     print(f'\t{finished_sandwich}')

# ---------------------Exercise 7.10--------------------

# prompt = "If you could visit one place in the world, where would you go: "
# name = ''

# users = {}
#
# number_of_users = 1
#
# while number_of_users <=3:
#     name = input("Enter your name: ")
#     place = input(prompt)
#     users[name] = place
#     number_of_users += 1
#
# print('\n----Travel Destinations----')
# for user, city in users.items():
#     print(f"{user} will love to travel to {city}")

# ---------------------Extra Practices --------------------
# books = []
#
# prompt = "Book Collection \n"
# prompt += "Type \'quit\' to exit, enter your favorite book title: "
#
# book_title = ''
#
# while book_title != 'quit':
#     book_title = input(prompt)
#     if book_title != 'quit':
#         books.append(book_title)
#         prompt = "Enter your next favorite book title: "
#
# print("\nThe following is a list of you favorites books: \n")
#
# count = 0
# for book in books:
#     count += 1
#     print(f"{count}. {book}.")
