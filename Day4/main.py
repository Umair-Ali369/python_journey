from Models.user import User
from Manager.manage_user import UserManager
from Data.chatManager import ChatManager

def display_Header():
    print("\n " + "="*40)
    print("NovxX Communication System")
    print("\n " + "="*40)

def display_Seperator():
    print("-"*40)

def run_system():
    display_Header()

    manager = UserManager()

    u1 = User("Ahmad", "ur", 22)
    u2 = User("Yuki", "ja", 25)
    u3 = User("Omar", "ar", 30)

    manager.add_user(u1)
    manager.add_user(u2)
    manager.add_user(u3)

    print(f'{manager.total_users()} users regisered on system.')
    display_Seperator()

    chat = ChatManager()
    conv1 = chat.create_conversation(u1, u2)
    conv2 = chat.create_conversation(u2, u3)

    print(f"\n {len(chat.conversations)} conversations started!")
    display_Seperator()

    print("\n Sending Messages.....")
    
    chat.add_message(conv1["id"], 1, "How are baby? I love girl who love me a lot.")
    chat.add_message(conv1["id"], 2 , "Are you alight? Where do you live nowadays.")
    chat.add_message(conv1["id"], 1, "I am okay, alright, fine. I live in London nowadsys.")

    chat.add_message(conv2["id"], 2, "Hi, how are you buddy, where are you hidden in this beautiful earth.")
    chat.add_message(conv2["id"], 3, "Yeah, thanks, bro I have a lot works and I'm busy in it all day.")

    display_Seperator()
    print("\n Conversaton 1 Ahmad - Yuki : \n")

    messages = chat.get_messages(conv1["id"])
    for msg in messages:
       if msg:
            sender = next(
                (p for p in conv1["participants"] if p.id == msg["sender_id"]),
            None
            )
            sender_name = sender.name if sender else "Unknown"
            print(f"[{sender_name}] : {msg["text"]} -> {msg["translated_text"]}")

    display_Seperator()
    print("\n Conversaton 2 Yuki - Omar: \n")
    messages = chat.get_messages(conv2["id"])
    for msg in messages:
       if msg:
            sender = next(
                (p for p in conv2["participants"] if p.id == msg["sender_id"]),
                None
            )
            sender_name = sender.name if sender else "Unknown"
            print(f"[{sender_name}] : {msg["text"]} -> {msg["translated_text"]}")

    display_Seperator()
    print("\n Summaries :")

    summ1 = chat.get_summary(conv1["id"])
    summ2 = chat.get_summary(conv2["id"])
    print(summ1)
    display_Seperator()
    print(summ2)

    display_Seperator()
    print("\n Saving all data to system.....")

    manager.save_to_file()
    chat.save_to_file()

run_system()





