from database import engine, create_tables
from Models.db_models import UserDB, ConversationDB, MessagesDB

from database import Base

Base.metadata.create_all(bind=engine)
print("✅ NovxX tables created in global_system_db!")

