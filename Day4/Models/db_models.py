from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from sqlalchemy.sql import func
from database import Base

class UserDB(Base):
    __tablename__ = "users"

    id            = Column(Integer, primary_key=True, index=True)
    name          = Column(String, nullable=False)
    email         = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    language      = Column(String, nullable=False)
    age           = Column(Integer)
    is_premium    = Column(Boolean, default=False)
    messages_sent = Column(Integer, default=0)  # ← fixed typo: send → sent
    created_at    = Column(DateTime, default=datetime.now)

    messages = relationship(
        "MessagesDB",
        back_populates="sender",
        primaryjoin="UserDB.id == MessagesDB.sender_id"
    )

class ConversationDB(Base):
    __tablename__ = "conversations"

    id         = Column(Integer, primary_key=True, index=True)
    user1_id   = Column(Integer, ForeignKey("users.id"))
    user2_id   = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)

    messages = relationship("MessagesDB", back_populates="conversation")
    user1    = relationship("UserDB", foreign_keys=[user1_id])
    user2    = relationship("UserDB", foreign_keys=[user2_id])

class MessagesDB(Base):
    __tablename__ = "messages"

    id              = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    sender_id       = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    original_text   = Column(String)
    translated_text: Mapped[str] = mapped_column(nullable=True)
    timestamp       = Column(DateTime, default=datetime.now())  

    sender       = relationship(
        "UserDB",
        back_populates="messages",
        primaryjoin="MessagesDB.sender_id == UserDB.id"
    )
    conversation = relationship("ConversationDB", back_populates="messages")