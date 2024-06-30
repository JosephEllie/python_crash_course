class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fullname = f"{self.first_name} {self.last_name}"

    def describe_user(self):
        print(f"My name is {self.fullname} and I am {self.age} years old")

    def greeting(self):
        print(f"Hello, {self.fullname}")


class Privilege:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can block user access']

    def show_privileges(self):
        print("Administrators set of privileges: ")
        count = 0
        for user_privilege in self.privileges:
            count += 1
            print(f'{count}. {user_privilege.title()}')


class Admin(User):
    def __init__(self, first_name=None, last_name=None, age=None):
        self.privilege = Privilege()

        super().__init__(first_name, last_name, age)

system_admin = Admin()
system_admin.privilege.show_privileges()
