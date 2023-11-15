users = {}
books = {}
with open('users.txt') as f:
    for line in f.readlines():
        users[line] = []

with open('books.txt') as f:
    for line in f.readlines():
        books[line] = 'nobody'

while 1:
    print("1.All users")
    print("2. All books")
    print("3.Get book")
    print("4. Return book")
    print("5. All gotten books")
    print("6. New book")
    print("7. New user")
    print("8. Exit")
    com = input("Please enter one of the options below\n")
    if com == "1":
        for i in users:
            print(i)
    elif com == "2":
        for i in books:
            print(i)
    elif com == "3":
        book_name = input("Please enter book name\n")
        username = input("Please enter user name\n")
        if books[book_name] == 'nobody':
            books[book_name] = username
            users[username].append(book_name)
        else:
            print("The book is not in the library")

    elif com == "4":
        book_name = input("Please enter book name\n")
        user_name = input("Please enter user name\n")
        books[book_name] = 'nobody'
        try:
            users[user_name].remove(book_name)
        except ValueError:
            continue
    elif com == "5":
        for i in books:
            if books[i] != 'nobody':
                print(i)
    elif com == "6":
        book_name = input("Please enter book name\n")
        books[book_name] = 'nobody'

    elif com == "7":
        username = input("Please enter user name\n")
        users[username] = []
    elif com == "8":
        break
