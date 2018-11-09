# def greet_user():
#     print("Hello!")
#
# greet_user()

# def greet_user(username):
#     print("Hello, " + username.title() + "!")
#
# greet_user("jesse")

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\n Please tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")


formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")