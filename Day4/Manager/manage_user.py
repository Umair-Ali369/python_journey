from Models.user import User
import json

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
        with open("Data/global_system.json", "w") as file:
            json.dump(dict_list, file, indent=4)
        print("Saved")

    def load_from_file(self):
        try:
            with open("Data/global_system.json", "r") as file:
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