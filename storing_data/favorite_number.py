from pathlib import Path
import json


class User_profile:
    """This class takes user info and remembers it"""

    def __init__(self):
        self.path = Path('username.json')
        self.user_info = {}

    def get_stored_username(self):
        """Get stored username if available."""
        if self.path.exists():
            contents = self.path.read_text()
            data = json.loads(contents)
            return data
        else:
            return None

    def get_user_info(self):
        """Prompt for a new username."""

        username = input("What is your name? ")
        favorite_color = input("What is your favorite color? ")
        birthday = input("When is your Birthday? ")
        self.user_info = {
            'username': username,
            'favorite_color': favorite_color,
            'birthday': birthday
        }
        contents = json.dumps(self.user_info)
        self.path.write_text(contents)
        return self.user_info

    def greet_user(self):
        """Greet the user by name."""
        if self.path.exists():
            return print(f"Welcome back, {self.user_info.get('username')}!")
        else:
            self.get_user_info()
            print(f"We'll remember you when you come back, {self.greet_user()}!")


greeting = User_profile()

greeting.greet_user()
