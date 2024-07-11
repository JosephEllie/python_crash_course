from pathlib import Path

path = Path('guests.txt')
prompt = "Enter your name: "
message = ''


while True:
    message += input(prompt) + " \n"
    if 'quit' not in message:
        path.write_text(message)
    else:
        break

