import json
from datetime import datetime
from Models.user import User


class ChatManager:
    def __init__(self):
        self.conversations = []

    def create_conversation(self, user1, user2):
        new_conv = {
            "id" : len(self.conversations) + 1,
            "participants" : [user1, user2],
            "messages" : [],
            "created_at" : datetime.now().strftime("%d/%m/%Y")
        }

        self.conversations.append(new_conv)
        return new_conv

    def add_message(self, conversation_id, sender_id, text):
        for conv in self.conversations:
            if conv["id"] == conversation_id:
                recipient = next(
                    (p for p in conv["participants"] if p.id != sender_id),
                    None,
                )
                translated_text = (
                    recipient.receive_message(message=text) if recipient else text
                )

                new_message = {
                    "sender_id": sender_id,
                    "text": text,
                    "translated_text": translated_text,
                    "timeStamp": datetime.now().strftime("%d/%m/%Y"),
                }

                conv["messages"].append(new_message)
                return True
        return False

    def get_messages(self, conv_id):
        for conv in self.conversations:
            if conv["id"] == conv_id:
                return conv["messages"]
        return []

    def find_conversation(self, conv_id):
        for conv in self.conversations:
            if conv["id"] == conv_id:
                print(f'Founded : {conv}')
                return conv
            print("Conversation not founded.")
        
    def _serialize_conversations(self):
        return [
            {
                "id": conv["id"],
                "participants": [
                    p.to_dict() if hasattr(p, "to_dict") else p
                    for p in conv["participants"]
                ],
                "messages": conv["messages"],
                "created_at": conv["created_at"],
            }
            for conv in self.conversations
        ]

    def save_to_file(self):
        with open("Data/conversations.json", "w", encoding="utf-8") as file:
            json.dump(self._serialize_conversations(), file, indent=4, ensure_ascii=False)
        print("Saved")

    def load_from_file(self):
        try:
            with open("Data/conversations.json", "r") as file:
                loaded_convs = json.load(file)
                self.conversations = [
                    {
                        "id": conv["id"],
                        "participants": [
                            User.from_dict(p) if isinstance(p, dict) else p
                            for p in conv["participants"]
                        ],
                        "messages": conv["messages"],
                        "created_at": conv["created_at"],
                    }
                    for conv in loaded_convs
                ]
                print(loaded_convs)
        except FileNotFoundError:
            print("File Not found")
        except json.JSONDecodeError:
            print("File currupted!")
    
    def get_summary(self, conversation_id):
        for conv in self.conversations:
            if conv["id"] == conversation_id:
                messages = conv["messages"]
                print(f'Total messages : {len(messages)}')
                if messages:
                    print(f'Last message : {messages[-1]["text"]}')
                return
        print("Conversation not founded!")
