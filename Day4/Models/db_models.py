from numbers import Integral
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from sqlalchemy.sql.expression import ColumnClause
from database import Base

class UserDB(Base):
    __tablename__ = "users"

    id  =  Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = False)
    language = Column(String, nullable = False)
    age = Column(Integer)
    is_premium = Column(Boolean, default = False)
    messages_send = Column(Integer, default = 0)
    created_at = Column(DateTime, default = datetime.now)

    messages = relationship("MessageDB", back_populates="sender")

class ConversationDB(Base):
    __tablename__ = "conversations" 

    id  =  Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, ForeignKey("users.id"))
    user2_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default = datetime.now)

    messages = relationship("MessageDB", back_populates="conversations")

class MessagesDB(Base):
    __tablename__ = "messages" 

    id  =  Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    original_text = Column(String)
    translated_text = ColumnClause(String)
    timeStamp = Column(DateTime, default = datetime.now)

    sender = relationship("UserDB", back_populates = "messages")
    conversation = relationship("ConversationDB", back_populates = "messages")
