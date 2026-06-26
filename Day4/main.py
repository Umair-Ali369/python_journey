# from Models.user import User
# from Manager.manage_user import UserManager
# from Data.chatManager import ChatManager

# def display_Header():
#     print("\n " + "="*40)
#     print("NovxX Communication System")
#     print("\n " + "="*40)

# def display_Seperator():
#     print("-"*40)

# def run_system():
#     display_Header()

#     manager = UserManager()

#     u1 = User("Ahmad", "ur", 22)
#     u2 = User("Yuki", "ja", 25)
#     u3 = User("Omar", "ar", 30)

#     manager.add_user(u1)
#     manager.add_user(u2)
#     manager.add_user(u3)

#     print(f'{manager.total_users()} users regisered on system.')
#     display_Seperator()

#     chat = ChatManager()
#     conv1 = chat.create_conversation(u1, u2)
#     conv2 = chat.create_conversation(u2, u3)

#     print(f"\n {len(chat.conversations)} conversations started!")
#     display_Seperator()

#     print("\n Sending Messages.....")
    
#     chat.add_message(conv1["id"], 1, "How are baby? I love girl who love me a lot.")
#     chat.add_message(conv1["id"], 2 , "Are you alight? Where do you live nowadays.")
#     chat.add_message(conv1["id"], 1, "I am okay, alright, fine. I live in London nowadsys.")

#     chat.add_message(conv2["id"], 2, "Hi, how are you buddy, where are you hidden in this beautiful earth.")
#     chat.add_message(conv2["id"], 3, "Yeah, thanks, bro I have a lot works and I'm busy in it all day.")

#     display_Seperator()
#     print("\n Conversaton 1 Ahmad - Yuki : \n")

#     messages = chat.get_messages(conv1["id"])
#     for msg in messages:
#        if msg:
#             sender = next(
#                 (p for p in conv1["participants"] if p.id == msg["sender_id"]),
#             None
#             )
#             sender_name = sender.name if sender else "Unknown"
#             print(f"[{sender_name}] : {msg["text"]} -> {msg["translated_text"]}")

#     display_Seperator()
#     print("\n Conversaton 2 Yuki - Omar: \n")
#     messages = chat.get_messages(conv2["id"])
#     for msg in messages:
#        if msg:
#             sender = next(
#                 (p for p in conv2["participants"] if p.id == msg["sender_id"]),
#                 None
#             )
#             sender_name = sender.name if sender else "Unknown"
#             print(f"[{sender_name}] : {msg["text"]} -> {msg["translated_text"]}")

#     display_Seperator()
#     print("\n Summaries :")

#     summ1 = chat.get_summary(conv1["id"])
#     summ2 = chat.get_summary(conv2["id"])
#     print(summ1)
#     display_Seperator()
#     print(summ2)

#     display_Seperator()
#     print("\n Saving all data to system.....")

#     manager.save_to_file()
#     chat.save_to_file()

# run_system()


from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from Models.user import User, PremiumUser
from Manager.manage_user import UserManager
from Data.chatManager import ChatManager

app = FastAPI(title = "WELLCOME TO GLOBAL SYSTEM")

user_manager = UserManager()
chat_manager = ChatManager()

## PYNDATIC MODELS
class UserCreate(BaseModel):
    name : str
    language : str
    age : int
    is_premium : bool = False

class ConversationCreate(BaseModel):
    user1_id : int
    user2_id : int

class MessageCreate(BaseModel):
    conversation_id : int
    sender_id : int
    text : str


## ROUTES

### home (get)
@app.get("/")
def home():
    return {
        "message" : "WELLCOME TO GLOBAL SYSTEM APIs",
        "status" : "running",
        "total_users" : len(user_manager.all_Users)
    }

### get all users (get)
@app.get("/users")
def getUsers():
    return {
        "Users" : [U.to_dict() for U in user_manager.all_Users]
    }

### create user (post)
@app.post("/users")
def create_user(data : UserCreate):
    if data.is_premium:
        new_user = PremiumUser(data.name, data.language, data.age)
    else:
        new_user = User(data.name, data.language, data.age)

    user_manager.add_user(new_user)
    return {
        "message" : f"Wellcome to Global System : {new_user.name}",
        "User" : new_user.to_dict()
    }


### get single user (get)
@app.get("/users/{user_id}")
def get_user(user_id : int):
    for user in user_manager.all_Users:
        if user.id == user_id:
            return user.to_dict()

    raise HTTPException(status = 404, details = "User Not found!")


### create conversation (post)
@app.post("/conversations")
def create_conversation(data : ConversationCreate):
    user1 = None
    for user in user_manager.all_Users:
        if user.id == data.user1_id:
            user1 = user
            break

    user2 = None
    for user in user_manager.all_Users:
        if user.id == data.user2_id:
            user2 = user
            break

    if not user1 or not user2:
        raise HTTPException(status = 404, detail = "One or both Users not found!")

    conv = chat_manager.create_conversation(user1, user2)
    return {
        "message " : "Converation Started",
        "Conversation_id" : conv["id"],
        "Between" : [user1.name, user2.name]
    }
    
### send message
@app.post("/messages")
def send_message(data : MessageCreate):
    success = chat_manager.add_message(
        conversation_id = data.conversation_id,
        sender_id= data.sender_id,
        text = data.text
    )
    if not success:
        raise HTTPException(status = 404, detail= "Conversation not Found!")

    return {
        "message" : "Message send and translated."
    }

### get conversation messages
@app.get("/conversations/{conv_id}/messages")
def get_messages(conv_id : int):
    messages = chat_manager.get_messages(conv_id)
    if not messages:
        raise HTTPException(status = 404, detail = "Conversation Not found")
    return {
        "Messages" : messages
    }