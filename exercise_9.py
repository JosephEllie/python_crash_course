# ----------9.1---------
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f'{self.restaurant_name} is my favorite restaurant in town')
#         print(f"And my best cuisine is {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")
#
#
# restaurant = Restaurant("Chicken Town", "KenTucky Fried Chicken")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# ----------9.2---------
# uncomment the Restaurant class to run these instances
# restaurant_1 = Restaurant("Lumley Fast Food", "Achekeh")
# restaurant_2 = Restaurant("Varola", "Jollof Rice")
# restaurant_3 = Restaurant("Basha", "Pizza")


# ----------9.3---------

# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.fullname = f"{self.first_name} {self.last_name}"
#
#     def describe_user(self):
#         print(f"My name is {self.fullname} and I am {self.age} years old")
#
#     def greeting(self):
#         print(f"Hello, {self.fullname}")


# ---Comment out this line when using this class as a Parent for exercise 8.7 - starting here---
# user_mic = User("Michael", "Yambasu", 30)
# user_Joe = User("Joseph", "Cooper", 26)
#
# user_Joe.describe_user()
# user_Joe.greeting()
# user_mic.describe_user()
# user_mic.greeting()
# print(restaurant.set_number_served(20))


# ----------9.4---------

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f'{self.restaurant_name} is my favorite restaurant in town')
#         print(f"And my best cuisine is {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")
#
#     def set_number_served(self, servings):
#         """Setting the number of customers feed"""
#         self.number_served = servings
#         return self.number_served
#
#     def increment_number_served(self, increment):
#         self.number_served += increment
#         print(f'{self.number_served} people have been served.')


# Comment this line when using this class as a Parent for exercise 8.7 - starting here

# restaurant = Restaurant("Chicken Town", "KenTucky Fried Chicken")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# print(restaurant.number_served)
# restaurant.number_served = 5
# print(restaurant.number_served)
#
# print(restaurant.set_number_served(20))
#
# restaurant.increment_number_served(2)


# --------------------End here---------------------------


# ----------9.5---------

# class User:
#     def __init__(self, first_name=None, last_name=None, age=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.fullname = f"{self.first_name} {self.last_name}"
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f"My name is {self.fullname} and I am {self.age} years old")
#
#     def greeting(self):
#         print(f"Hello, {self.fullname}")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         return self.login_attempts
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         return self.login_attempts


# user = User()
#
# print(user.increment_login_attempts())
# print(user.reset_login_attempts())


# ----------9.6---------
# For this exercise uncomment the parent class in 9.4

# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         self.flavors = ['KFC', 'Mexican wrap']
#         super().__init__(restaurant_name, cuisine_type)
#
#     def favor(self):
#         print(f"Welcome to {self.restaurant_name} \nMenu on the list is {self.cuisine_type} "
#               f"\nList of Flavors: ")
#         for flavor in self.flavors:
#             print(f"\t - {flavor}")


# flavorList = IceCreamStand('Ada Cooks', 'Sharwama')
#
# flavorList.favor()


# ----------9.7---------
# uncomment exercise 9.3 as User is the parent class for Admin.


# class Admin(User):
#     def __init__(self, first_name=None, last_name=None, age=None):
#         self.user_privileges = ['can add post', 'can delete post', 'can ban user', 'can block user access']
#         super().__init__(first_name, last_name, age)
#
#     def show_privileges(self):
#         print("Administrators set of privileges: ")
#         count = 0
#         for user_privilege in self.user_privileges:
#             count += 1
#             print(f'{count}. {user_privilege.title()}')
#
#
# system_admin = Admin()
# system_admin.show_privileges()
