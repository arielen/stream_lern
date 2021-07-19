class User:
    username = "Noname"
    password = "Password"
    is_banned = False


user_1 = User()  # экземпляр класса
user_2 = User()
user_2.username = "Alex"
print(user_1.username, user_2.username)
