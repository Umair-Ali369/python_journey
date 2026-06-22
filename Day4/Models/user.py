
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

    def receive_message(self, message, from_language="auto"):
        from Services.translator import translate_text
        translated = translate_text(message, self.language, from_language)
        print(f"{self.name} : recieved:{translated}")
      
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

