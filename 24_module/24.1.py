username = input("Как вас зовут: ")

while True:
    print("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2")
    response = input("Введите 1 или 2: ")
    if response == "1":
        try:
            with open("chat.txt", "r") as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: пока нет сообщений!\n")
    elif response == "2":
        new_message = input("Введите сообщение: ")
        with open("chat.txt", "a") as file:
            file.write(f"{username}: {new_message}\n")
    else:
        print("Не известная команда")
