from pathlib import Path

# Exercise 10-6

# try:
#     num_1 = int(input("Enter any number: "))
#     num_2 = int(input("Enter any number: "))
#     result = num_1 + num_2
#     print(result)
# except ValueError:
#     print('Only Numerical Computations are allowed!!!')

# Exercise 10-7

# try:
#     while True:
#         num_1 = int(input("Enter any number: "))
#         num_2 = int(input("Enter any number: "))
#
#         result = num_1 + num_2
#         print(result)
#         continue
# except ValueError:
#     pass


# Exercise 10-8

# def display_contents(path):
#     files = Path(path)
#     contents = files.read_text()
#     print(contents)
#
#
# try:
#     file_list = ['cat.txt', 'dog.txt', 'people.txt']
#     for file in file_list:
#         print(f'\nDisplaying: {file}')
#         display_contents(file)
#
# except:
#     print("File not Found")

# Exercise 10-9

# def display_contents(path):
#     files = Path(path)
#     contents = files.read_text()
#     print(contents)
#
#
# try:
#     file_list = ['cat.txt', 'dog.txt', 'people.txt']
#     for file in file_list:
#         print(f'\nDisplaying: {file}')
#         display_contents(file)
#
# except:
#     pass

