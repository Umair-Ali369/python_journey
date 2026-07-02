from database import engine  # ⬅️ Removed 'create_tables' from here
from Models.db_models import UserDB, ConversationDB, MessagesDB
from database import Base

# This clears old tables to give you a clean slate
print("🧹 Dropping old tables...")
Base.metadata.drop_all(bind=engine)

# This builds your new UserDB, ConversationDB, and MessagesDB tables
print("🏗️ Creating new database tables...")
Base.metadata.create_all(bind=engine)

print("✅ NovxX tables created in global_systemdb2!")