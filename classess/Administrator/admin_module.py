from user_module import User


class Admin(User):
    def __init__(self, first_name=None, last_name=None, age=None):
        self.user_privileges = ['can add post', 'can delete post', 'can ban user', 'can block user access']
        super().__init__(first_name, last_name, age)

    def show_privileges(self):
        pass
