# -----------Exercise 8.1-------------
# def display_message():
#     print("Hello everyone, in this chapter I have learnt about functions, parameters and arguments")
#
# display_message()

# -----------Exercise 8.2-------------
# def favorite_book(title):
#     print(f"One of my favorite book is {title}")
#
# favorite_book("Python Crash Course")

# -----------Exercise 8.3-------------
# def make_shirt(size, message):
#     print(f'Shirt size is {size} and inscription is: {message}')
#
# make_shirt('medium', 'I am a Python Genuis')
# make_shirt(size ='medium', message = 'I am a Python Genuis')

# -----------Exercise 8.4-------------
# def make_shirt(size, message = 'I love Python'):
#     print(f'Shirt size is {size} and inscription is: {message}')
#
# make_shirt('Large')
# make_shirt('Medium')
# make_shirt('Extra Large', 'Programming is fun')

# -----------Exercise 8.5-------------

# def describe_country(city, country = 'Sierra Leone'):
#     print(f"{city} is in {country}")
#
# describe_country('Freetown')
# describe_country('Kenema')
# describe_country('Accra', 'Ghana')

# -----------Exercise 8.6-------------
# def city_country(city, country):
#     print(f'{city}, {country}')
#
# city_country('Freetown', 'Sierra Leone')
# city_country('Conakry', 'Guinea')
# city_country('Monrovia', 'Liberia')

# -----------Exercise 8.7-------------
# def make_album(artist_name, album, number_of_songs = None):
#
#     def check_number_of_songs():
#         artist_info = {
#             "Artist Name": artist_name,
#             "Album Title": album
#         }
#         if number_of_songs:
#             artist_info['Number of Songs'] = number_of_songs
#         return artist_info
#
#     return check_number_of_songs()

# album_0 = make_album('Emmerson', 'Borbor Belle', 2)
# album_1 = make_album('Drizilik', 'Sukubly')
# album_2 = make_album('David', 'The Word of GOD')
# print(album_0)
# print(album_1)
# print(album_2)

# -----------Exercise 8.8-------------

# def make_album(artist_name, album, number_of_songs = None):
#
#     def check_number_of_songs():
#         artist_info = {
#             "Artist Name": artist_name,
#             "Album Title": album
#         }
#         if number_of_songs:
#             artist_info['Number of Songs'] = number_of_songs
#         return artist_info
#
#     return check_number_of_songs()
#
# prompt_1= "Enter Artist Name: "
# prompt_2= "Enter Album Name: "
# artist_input = ''
# album_input = ''
# print("Enter quit or q to exit program")
# while True:
#     artist_input = input(prompt_1)
#     if artist_input != 'quit' :
#         album_input = input(prompt_2)
#         album_info = make_album(artist_input, album_input)
#
#     else:
#         break
#     print(album_info)

# -----------Exercise 8.9-------------

# def show_messages(short_text_messages ):
#     for message in short_text_messages:
#         print(message)
#
# short_text_messages = ['Hello', 'Hi', 'Howdy']
# show_messages(short_text_messages)

# -----------Exercise 8.10-------------

# sent_messages = []
# def send_messages(messages):
#     for message in messages:
#         print(message)
#         sent_messages.append(message)
#     print(f'Short Text Messages: {messages}')
#     print(f'Sent Messages: {sent_messages}')
#
# short_text_messages = ['Hello', 'Hi', 'Howdy']
# send_messages(short_text_messages[:])

# -----------Exercise 8.11-------------

# sent_messages = []
# def send_messages(messages):
#     for message in messages:
#         sent_messages.append(message)
#     print(sent_messages)
#
# short_text_messages = ['Hello', 'Hi', 'Howdy']
#
# send_messages(short_text_messages[:])
# print(short_text_messages)

# -----------Exercise 8.12-------------

# def make_sandwich(*sandwich_ingredients):
#     print(f"Adding the following to your sandwich: ")
#     for sandwich_ingredient in sandwich_ingredients:
#         print(f'- {sandwich_ingredient}')
#
# make_sandwich('Lettuce','Mayonnaise','Carrot', 'Ketch up', 'Luncheon Meat')

# -----------Exercise 8.13-------------
# def build_profile(partner, status, **user_info):
#
#  """Build a dictionary containing everything we know about a user."""
#  user_info['Marriage Status'] = status
#  user_info['Partner'] = partner
#  return user_info
#
# user_profile = build_profile('Adama', 'Almost Married',
#  first_name ='Joseph',
#  last_name='Cooper',
#  passion = 'Programming'                      )
# print(user_profile)

# -----------Exercise 8.14-------------

# def car_make(manufacturer, model, **car_info):
#  car_info['manufacturer'] = manufacturer
#  car_info['model'] = model
#
#
#  msg = f'{car_info.get('manufacturer')} is my best car, particularly {car_info.get('model')} Edition, '\
#        f'{car_info.get('color')} color, Tow Package: {car_info.get('tow_package')}'
#
#  return msg
#
# car = car_make('Toyota', 'Rav4 2024', color = 'blue', tow_package= True)
# print(car)


# -----------Extra Practice-------------

# def greeting(name):
#     """"Greet user"""
#     print(f"Hello, {name}! Congrats on writing your first python function.")
#
# number_of_person = 1
# learners = []
# while number_of_person < 3:
#     prompt = "Enter name: "
#     message = input(prompt)
#     greeting(message)
#     learners.append(message)
#     number_of_person +=1
#
# print("\nCongratulations to our new learners for writing your first python code.")
# count = 0
# for learner in learners:
#     count +=1
#     print(f"{count}. {learner}")
#

