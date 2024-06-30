class User:
    def __init__(self, first_name=None, last_name=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fullname = f"{self.first_name} {self.last_name}"
        self.login_attempts = 0

    def describe_user(self):
        print(f"My name is {self.fullname} and I am {self.age} years old")

    def greeting(self):
        print(f"Hello, {self.fullname}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
