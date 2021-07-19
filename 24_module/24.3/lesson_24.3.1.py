class User:
    username = "Noname"
    password = "Password"
    is_banned = False
    friends = []

    def print_info(self):
        print(f"Name: {self.username}\n"
              f"Password: {self.password}\n"
              f"Ban status: {self.is_banned}")

    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.username)
        else:
            self.friends.append(friend)


user_1 = User()
user_2 = User()
user_2.username = "Alina"
user_1.print_info()
user_1.add_friend("Bob")
user_1.add_friend(user_2)
print(user_1.friends)
