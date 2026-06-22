## User Class System
## Project 2

SUPPORTED_LANGUAGES = ["English", "Urdu", "Japanees", "Chinees", "French"]

class User:
    user_count = 0
  ## bug one   ( pass )
    def __init__(self, name, language, age):
        User.user_count += 1
        self.id = User.user_count
        self.name = name
        self.language = language
        self.age = int(age)
        self.is_premium = False
        self.messages_send = 0
        return
    def __str__(self):
        return f"[{self.id}] {self.name} | {self.language} | Premium: {self.is_premium}"

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
            
    def show_all_users(self):
        for user in self.all_Users:
            print(f'All Users : {user}')

    def total_users(self):
        total = len(self.all_Users)
        print(f'Total Users : {total}')


manager = UserManager()

u1 = User("Ahmad", "Urdu", 22)
u2 = User("Yuki", "Japanese", 25)
u3 = PremiumUser("Omar", "French", 30)

manager.add_user(u1)
manager.add_user(u2)
manager.add_user(u3)

u1.send_message("Hello NovxX!")
u1.send_message("This is amazing!")
u3.show_profile()

manager.show_all_users()
manager.find_user("Ahmad")

