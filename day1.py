## User registration system
## Project 1

SUPPORTED_LANGUAGES = ["Urdu", "English"]

Users  = []
user_id = 1

def create_user():
    global user_id
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    language = input("Enter your language : ")

    if language.title() not in SUPPORTED_LANGUAGES:
        print(f'Sorry!, {language} is not supported!')
        return
    user = {
        "id" : user_id,
        "name" : name,
        "age" : age,
        "language" : language
    }
    Users.append(user)
    user_id += 1
    print("User Created!")

def show_user(id):
    for user in Users:
        if user["id"] == id:
           print(f'Name : {user["name"]}')
           print(f'Age : {user["age"]}')
           print(f'Language : {user["language"]}') 
           return 
    print("No Users!")

def language_supported(language):
    if language.title() in SUPPORTED_LANGUAGES:
         return print("Language Supported!")
    else:
         return print("Language not supported!")

def get_user_plan(messages_send):
    if messages_send == 0:
        print("New User")
    elif messages_send <= 50:
        print("Active User")
    elif messages_send <= 500:
        print("Power User")
    else:
        print("Premium User")

create_user()
show_user(1)
 







