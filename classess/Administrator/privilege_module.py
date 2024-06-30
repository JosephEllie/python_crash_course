from admin_module import Admin


class Privilege:
    def __init__(self):
        self.my_privileges = Admin().user_privileges

    def show_privileges(self):
        print("Administrators set of privileges: ")
        count = 0
        for user_privilege in self.my_privileges:
            count += 1
            print(f'{count}. {user_privilege.title()}')
