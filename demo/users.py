class Users():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == 'xutt' and self.password == '123456':
            return True

        return False

username = input("Username:")
password = input("Password:")

user = Users(username, password)

if (user.login()):
    print("Login Success")
else:
    print("Login Failed")