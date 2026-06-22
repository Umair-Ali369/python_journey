from Manager.manage_user import UserManager
from Models.user import User
from Services.translator import get_random_quote, get_fact

manager = UserManager()
manager.load_from_file()
u1 = User("Ahmad", "ur", 22)
u2 = User("Yuki", "Japanese", 25)

manager.add_user(u1)
manager.add_user(u2)

manager.save_to_file()

manager.show_all_users()

manager2 = UserManager()
print("\nLoaded from file:")
manager2.load_from_file()
print("\n All Users : ")
manager2.show_all_users()

if __name__ == "__main__":
    getQuote = get_random_quote()
    for item in getQuote:
        print(f'TEXT : {item["text"]}')
        print(f'AUTHOR : {item["author"]}')
        getFact = get_fact()
        print(f'Fact : {getFact["fact"]}')
      
    sms = u1.receive_message("Hello, how are you today?")


    


