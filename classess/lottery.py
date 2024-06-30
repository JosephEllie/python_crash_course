from random import choice


class Randomizer:
    def __init__(self):
        self.random_choice = [1, 7, 5, 0, 3, 4, 2, 9, 6, 8, "m", "j", "u", "o", "p"]

    def start_randomizer(self):
        result = choice(self.random_choice)
        return result


generate_token = Randomizer()
winning_token = []

for _ in range(4):
    winning_token.append(generate_token.start_randomizer())
    # print(winning_token, end=' ')
    # print(type(winning_token))

print("Any ticket matching these 4 numbers or letters wins a prize: ", winning_token)
my_ticket = []

raffle_numbers = generate_token.random_choice
attempts = 1

while len(raffle_numbers) != 4:
    if raffle_numbers not in winning_token:
        raffle_numbers.pop()
        my_ticket = winning_token
        attempts += 1
print(f"I won, my ticket is: {my_ticket}", "Number of attempts: ", attempts)
