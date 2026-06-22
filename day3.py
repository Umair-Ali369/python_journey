## ADDD  SAVE / LOAD TO EXISTING UESR SYSTEM
## Project 2 updated

import json
SUPPORTED_LANGUAGES = ["English", "Urdu", "Japanees", "Chinees", "French"]

class User:
    id = 0
    def __init__(self, name, language, age):
        User.id += 1
        self.id = User.id
        self.name = name
        self.language = language
        self.age = int(age)
        self.is_premium = False
        self.messages_send = 0
        return

    def __str__(self):
        return f"[{self.id} {self.name} | {self.language} | Premium: {self.is_premium}]"

    def send_message(self, message):
        self.messages_send += 1
        print(f"Message sended : {message}")
        return
    def show_profile(self):
        if self.language not in SUPPORTED_LANGUAGES:
            print(f'The {self.language} is not available!')
            return
        print(f'Name : {self.name} \n Language : {self.language} \n Age : {self.age}')

    def get_plan(self):
        if self.messages_send == 0:
            print("New User")
        elif self.messages_send <= 50:
            print("Active User")
        elif self.messages_send <= 500:
            print("Premium")
        else:
            print("Super Premium Candidate")

    def upgrade_to_premium(self):
        self.is_premium = True
        print("Upgraded")
        return
      
    def to_dict(self): 
        return { 
            "id" : self.id, 
            "Name": self.name, 
            "Age": self.age, 
            "Language": self.language, 
            "is_premium": self.is_premium, 
            "Messages": self.messages_send 
            }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            name = data.get("Name"),
            age = data.get("Age"),
            language = data.get("Language")
        )
        user.id = data.get("id")
        user.is_premium = data.get("is_premium")
        user.messages_send = data.get("Messages")
        return user
        
class PremiumUser(User):

    def __init__(self, name, language, age):
        super().__init__(name, language, age)
        self.translate_limit = 1000
        self.voice_calls_remaining = 100
        self.is_premium = True
        return

    def show_profile(self):
        super().show_profile()
        print("Plane : Premium")
        print(f'Translation limit : {self.translate_limit}')
        return


class UserManager():
   
    def __init__(self):
        self.all_Users = []

    def add_user(self, user):
        self.all_Users.append(user)
        print("User Added")
        return
     
    def find_user(self, name):
        self.name = name
        for user in self.all_Users:
            if self.name in user.name:
                print(f'Founded , {user}')
            
    def total_users(self):
        total = len(self.all_Users)
        print(f'Total Users : {total}')

    def save_to_file(self):
        dict_list = [user.to_dict() for user in self.all_Users]
        with open("global_system.json", "w") as file:
            json.dump(dict_list, file, indent=4)
        print("Saved")

    def load_from_file(self):
        try:
            with open("global_system.json", "r") as file:
                loaded_Users = json.load(file)
                for user in loaded_Users:
                    U = User.from_dict(user)
                    self.all_Users.append(U)
                print(loaded_Users)
            print("Loaded")
        except FileNotFoundError:
            print(f'File not found!')
        except json.JSONDecodeError:
            print("File currupted!")

    def show_all_users(self):
        if len(self.all_Users) == 0:
            print("No user here!")
        for user in self.all_Users:
            print(f'Users : {user}')



manager = UserManager()
manager.load_from_file()
u1 = User("Ahmad", "Urdu", 22)
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


