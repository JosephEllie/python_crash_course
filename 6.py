# # -----------Exercise 6-1 -------------

# person = {
#     "first_name": "Joseph",
#     "last_name": "Cooper",
#     "age": 26,
#     "city": "Freetown",
# }
# fullname = person["first_name"] + " " + person["last_name"]
# print(
#     f"My name is {fullname} and I am {person['age']} years old. I live in {person['city']}"
# )

# -----------Exercise 6-2 -------------

# persons = {"joe": 3, "tom": 4, "ben": 1, "sam": 2, "dan": 5}

# for name, fav_number in persons.items():
#     print(f"{name.title()} your favorite number is {fav_number}")


# -----------Exercise 6-3,4 -------------

# dictionary = {
#     "variables": "A variable is a container that holds data, "
#     "could be anything like string, number etc",
#     "loop": "This is making literations over an object or any iterable expression",
#     "range": "Is a method used to generate numbers",
#     "sort": "You used a sort method to change the order of items",
#     "sorted": "Works like sort method but create a new copy instead",
# }
# for word, meaning in dictionary.items():
#     print(f"{word.title()}: \n \t {meaning}")


# -----------Exercise 6-5 -------------

# major_rivers = {
#     'egypt': 'nile',
#     'sierra leone': 'mano',
#     'congo': 'congo',
# }

# countries = []
# print('The three major rivers are: ')
# for country, rivers in major_rivers.items():
#     print(rivers.title())
#     countries.append(country)

# print("\nThe counties of the three major rivers are: ")
# for nation in countries:
#     print(nation.title())


# -----------Exercise 6-6 -------------

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }

# candidates = ["adama", "susan", "jen", "sarah"]

# for name in favorite_languages.keys():
#     if name in candidates:
#         print(f"{name.title()} thank you for taking the poll")
#     else:
#         print(f"{name.title()} please take the poll")


# -----------Exercise 6-7 -------------

# person_0 = {
#     "first_name": "Joseph",
#     "last_name": "Cooper",
#     "age": 26,
#     "city": "Freetown",
# }
# person_1 = {
#     "first_name": "Adama",
#     "last_name": "Gargar",
#     "age": 19,
#     "city": "Freetown",
# }
# person_2 = {
#     "first_name": "Joyce",
#     "last_name": "Cooper",
#     "age": 29,
#     "city": "Freetown",
# }

# people = [person_0, person_1, person_2]

# for persons in people:
#     fullname = persons["first_name"] + " " + persons["last_name"]
#     print(
#         f"Hello {fullname}, please verify your details: \n \t age:{persons['age']} city: {persons['city']}"
#     )

# -----------Exercise 6-8 -------------

# pets = [
#     {"animal": "dog", "owner": "Adama"},
#     {"animal": "cat", "owner": "Julie"}
# ]

# for pet_info in pets:
#     print(f'{pet_info['owner']} has a {pet_info['animal']} for a pet')

# -----------Exercise 6-9 -------------

# favorite_places = {
#     "joseph": ["canada", "austrialia, USA"],
#     "adama": ["canada", "england", "America"],
#     "joyce": ["england", "Ireland", "canada"],
# }
# for name, places in favorite_places.items():
#     print(f"{name.title()}'s favorite countries are: ")
#     for place in places:
#         print(f"\t {place.title()}")


# -----------Exercise 6-10 -------------

# persons = {
#     "joe": [2, 3, 4],
#     "tom": [5, 6, 7],
#     "ben": [4, 3, 2],
#     "sam": [3, 2, 1],
#     "dan": [9, 0, 8],
# }

# for name, fav_numbers in persons.items():
#     print(f"{name.title()} your favorite number is: ")
#     for fav_number in fav_numbers:
#         print(fav_number)


# -----------Exercise 6-11 -------------

cities = {
    "freetown": {
        "country": "sierra leone",
        "population": "8.5m",
        "fact": "was a british crown colony",
    },
    "accra": {
        "country": "ghana",
        "population": "12m",
        "fact": "it was regarded as the gold coast of Africa",
    },
    "addis ababa": {
        "country": "ethopia",
        "population": "12m",
        "fact": "only African nation that was not colonized",
    },
}

for city, city_info in cities.items():
    print(
        f'{city.title()} is a city in {city_info['country'].title()} with a population '
    f'of {city_info['population']}, one fun fact about the count is that {city_info['fact']}\n'
    )
