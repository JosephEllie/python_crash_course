def get_username(first, last, middle=''):
    # first = input('Enter First name: ')
    # last = input('Enter First name: ')
    fullname = ''
    if middle:
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"


print(f"My fullname is {get_username('Tom', 'Coops')}")
