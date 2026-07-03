from auth_user import hashPassword, verifyPassword, create_token, getCurrentUser
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db, engine
from Models.db_models import UserDB, ConversationDB, MessagesDB
from Services.translator import translate_text
from datetime import datetime
import Models.db_models as models
from database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Global System APIs", version= "2.0.0")

## PYNDATIC MODELS
class UserCreate(BaseModel):
    name : str
    email : str
    password : str
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

@app.get("/")
def home(db : Session = Depends(get_db)):
    total = db.query(UserDB).count()
    convTotal = db.query(ConversationDB).count()
    return {
        "Message" : "Wellcome to Global System",
        "Version" : "2.0.0",
        "Total Users" : total,
        "Total Conversations" : convTotal
    }

##  AUTH ROUTES 

# REGISTER
@app.post("/register")
def registerUser(data : UserCreate, db : Session = Depends(get_db)):
    existing = db.query(UserDB).filter(UserDB.email == data.email).first()
    if existing:
        raise HTTPException(status = 400, detail = "Email already registered!")
    
    newUser = UserDB(
        name = data.name,
        email = data.email,
        password_hash = hashPassword(data.password),
        language = data.language,
        age = data.age,
        is_premium = data.is_premium
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return {
        "Message" : f"Wellcome to Global System , {newUser.name}",
        "user_id" : newUser.id,
        "Email" : newUser.email
    }
    
# LOGIN
@app.post("/login")
def LoginUser(
    formData : OAuth2PasswordRequestForm = Depends(),
    db : Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.email == formData.username).first()

    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "Wrong email or password"
        )

    if not verifyPassword(formData.password, user.password_hash):
        raise HTTPException(
            status_code = 401,
            detail = "Wrong email or password"
        )

    token = create_token({"user_id" : str(user.id)})

    return {
        "access_token" : token,
        "token_type" : "bearer",
        "user" : {
         "id"  : user.id,
         "name" : user.name,
         "language" : user.language
        }
    }

# PROTECTED ROUTES E.G
@app.get("/me")
def getMe(currentUser : UserDB = Depends(getCurrentUser)):
    return {
        "id" : currentUser.id,
        "name" : currentUser.name,
        "email" : currentUser.email,
        "language" : currentUser.language,
        "is_premium" : currentUser.is_premium
    }


## USER ROUTES
@app.get("/users")
def get_users(db : Session = Depends(get_db)):
    users = db.query(UserDB).all()
    return {
        "Users" : [{"id" : u.id, "name" : u.name, "age" : u.age, "language" : u.language} for u in users]
    }

@app.post("/users")
def create_user(data : UserCreate, db : Session = Depends(get_db)):
    new_user = UserDB(
        name = data.name,
        language = data.language,
        age = data.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "Message" : f'Wellcome to Global System, {new_user.name}!',
        "User" : {
          "id" : int(new_user.id),
            "name" : str(new_user.name),
            "language" : str(new_user.language),
            "age" : int(new_user.age),
            "is_premium" : bool(new_user.is_premium)
        }
    }

@app.get("/users/{user_id}")
def get_user(user_id : int, db : Session = Depends(get_db)):
    Users  = db.query(UserDB).all()
    for u in Users:
        if user_id == u.id:
            return u.to_dict()
    raise HTTPException(status = "404", Detail = "User NOt Found!")

## CONVERSATION ROUTES

@app.post("/conversations")
def create_conversation(data : ConversationCreate, db : Session = Depends(get_db)):
    user1 = db.query(UserDB).filter(UserDB.id == data.user1_id).first()
    user2 = db.query(UserDB).filter(UserDB.id == data.user2_id).first()
    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="One or both users not found!")

    new_conversation = ConversationDB(
        user1_id = data.user1_id,
        user2_id = data.user2_id
             )

    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    return {
        "Message" : "Conversation created",
    }

@app.get("/conversations/{conv_id}")
def get_conversation(conv_id : int, db : Session = Depends(get_db)):
    conversation = db.query(ConversationDB).filter(ConversationDB.id == conv_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {
    "id": conversation.id,
    "user1_id": conversation.user1_id,
    "user2_id": conversation.user2_id,
    "created_at": conversation.created_at
}


## MESSAGE RUOTES
@app.post("/messages/send")
def send_message(data : MessageCreate, db : Session = Depends(get_db), currentUser : UserDB = Depends(getCurrentUser)):

    conv = db.query(ConversationDB).filter(ConversationDB.id == data.conversation_id).first()
    if not conv:
        raise HTTPException(status_code = 404, detail = "Conversation Not found!")

    recipient_id = conv.user2_id if conv.user1_id == data.sender_id else conv.user1_id
    recipient = db.query(UserDB).filter(UserDB.id == recipient_id).first()

   
    translated_Text = translate_text(data.text, recipient.language)

    new_message = MessagesDB(
        conversation_id = data.conversation_id,
        sender_id = currentUser.id,
        original_text = data.text,
        translated_text = translated_Text
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return {
        "Message" : "Send!",
        "form" : currentUser.name,
        "to" : recipient.name,
        "original" : data.text,
        "translated" : translated_Text,
        "Recipient_Language" : recipient.language
    } 