# NovxX AI Platform — Backend

> **"A universal AI-powered platform that breaks language barriers for communication, learning, business, healthcare and productivity — for everyone on earth."**

---

## 🚀 Project Overview

NovxX is a multilingual, AI-powered super-app targeting:
- 🌍 Communication across languages
- 📚 Learning & education assistance
- 💼 Business productivity
- 👨‍💻 Developer tools
- 🏥 Healthcare information
- 🎙️ Voice AI (coming)

**Built by:** Umair Khan — Solo Developer & Founder
**Location:** Tank, KPK, Pakistan
**Started:** June 2026

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Backend Framework | FastAPI |
| Database | PostgreSQL 18 |
| ORM | SQLAlchemy |
| Authentication | JWT (python-jose + passlib/bcrypt) |
| AI Model | Llama 3.1 via Groq API |
| Translation | deep-translator (GoogleTranslator) |
| Server | Uvicorn |
| Environment | python-dotenv |

---

## 📁 Project Structure

```
novxx/
├── Models/
│   ├── user.py              # User, PremiumUser classes
│   └── db_models.py         # SQLAlchemy DB models (UserDB, ConversationDB, MessagesDB)
├── Managers/
│   └── manage_user.py       # UserManager class
├── Services/
│   ├── translator.py        # Translation service (deep-translator)
│   └── ai_service.py        # AI service (Groq/Llama)
├── Data/
│   └── chat_manager.py      # ChatManager class
├── database.py              # PostgreSQL connection + session
├── auth.py                  # JWT auth system
├── main.py                  # FastAPI app + all routes
├── create_db.py             # One-time DB table creation
├── .env                     # Secrets (not in GitHub)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/novxx-ai-platform.git
cd novxx-ai-platform

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Add your keys:
# GROQ_API_KEY=your_groq_key
# DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/global_systemDB2
# SECRET_KEY=your_secret_key

# Create database tables
python create_db.py

# Run the server
uvicorn main:app --reload
```

---

## 🔌 API Endpoints

### Auth
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/register` | Register new user | No |
| POST | `/login` | Login, get JWT token | No |
| GET | `/me` | Get current user profile | Yes |

### Users
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/users` | Get all users | No |
| POST | `/users` | Create user | No |
| GET | `/users/{id}` | Get user by ID | No |

### Conversations
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/conversations` | Start conversation | No |
| GET | `/conversations` | Get all conversations | No |
| GET | `/conversations/{id}` | Get conversation by ID | No |

### Messages
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/messages` | Send message (basic) | No |
| POST | `/messages/send` | Send message (protected + auto-translate) | Yes |
| GET | `/conversations/{id}/messages` | Get messages in conversation | No |

### AI (Phase 1, 2, 3)
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/ai/chat` | AI communication assistant | Yes |
| POST | `/ai/learn` | Learning assistant (explain any topic) | Yes |
| POST | `/ai/business` | Business assistant (emails, tasks) | Yes |
| POST | `/ai/test` | Quick AI test | No |

---

## 🌍 Supported Languages

| Language | Code |
|---|---|
| Urdu | `ur` |
| English | `en` |
| Japanese | `ja` |
| Arabic | `ar` |
| French | `fr` |
| Chinese | `zh-CN` |

---

## 🔐 Authentication

NovxX uses JWT (JSON Web Token) authentication:

```
1. POST /register → create account
2. POST /login    → get access_token
3. Add token to requests:
   Header: Authorization: Bearer <your_token>
4. Token expires in 30 minutes
```

---

## 🤖 AI Features

NovxX AI is powered by **Llama 3.1** via Groq API:

- **Auto-language detection** — AI responds in the user's registered language automatically
- **Phase 1:** Multilingual AI chat assistant
- **Phase 2:** Learning assistant — explain any topic simply
- **Phase 3:** Business assistant — emails, tasks, professional writing
- **Expandable** — swap Groq for Claude or GPT in one line

---

## 📦 Dependencies

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-jose[cryptography]
passlib[bcrypt]
python-multipart
python-dotenv
deep-translator
groq
requests
```

---

## 📅 Development Log — 15-Day Sprint

### Day 1 — Python Foundations
- Variables, data types, lists, dictionaries, functions
- Built: NovxX User Registration System (CLI)
- Key bug fixed: `return` placement inside `for` loops (recurring pattern)

### Day 2 — OOP & Classes
- Classes, `__init__`, `__str__`, `self`, inheritance, `super()`
- Built: `User`, `PremiumUser` classes with `user_count` class variable
- Added: `UserManager` class with `add_user`, `find_user`, `show_all_users`
- Key lesson: class variable vs instance variable distinction

### Day 3 — File Handling + Error Handling
- `json.dump`, `json.load`, `json.dumps`, `json.loads`
- `try/except` — FileNotFoundError, JSONDecodeError
- Built: `to_dict()` and `from_dict()` methods on User class
- Built: `save_to_file()` and `load_from_file()` in UserManager
- Key bug fixed: `User.id` (class counter) vs `self.id` (instance id)

### Day 4 — Project Structure + Modules
- Multi-file project organization
- Cross-folder imports (`from Models.user import User`)
- `__init__.py` — marking folders as Python packages
- Virtual environment workflow: activate → install → freeze
- Built: Full `novxx/` folder structure with `Models/`, `Managers/`, `Data/`

### Day 5 — External APIs with `requests`
- `requests.get()`, `response.json()`, `status_code`
- Error handling: Timeout, ConnectionError, HTTPError
- Built: `get_random_quote()`, `get_fact()` in `Services/translator.py`
- Tested: Live API calls to quotable.io and catfact.ninja

### Day 6 — Translation Service
- Installed `deep-translator` library
- `GoogleTranslator(source='auto', target='ur').translate(text)`
- Built: `translate_text(text, target_lang, source_lang="auto")`
- Tested: English → Urdu, Japanese, Arabic, French, Chinese
- Connected: `User.receive_message()` — auto-translates incoming messages

### Day 7 — Virtual Environments + Git
- Full venv workflow: create → activate → install → freeze → deactivate
- `.gitignore` setup: venv/, __pycache__/, .env, data files
- `requirements.txt` = Python's `package.json`
- Pushed: NovxX project structure to GitHub

### Day 8 — JSON + Data Handling Deep Dive
- Nested JSON structures for conversations and messages
- `.get()` safe access pattern
- List comprehensions, `next()` with generators, `sorted()`, `Counter()`
- Built: `ChatManager` class with full conversation + message system
- Built: `_serialize_conversations()` — smart serialization with `hasattr` check
- Built: `load_from_file()` — rebuilds User objects from JSON

### Day 9 — Full System Integration
- Connected User + ChatManager + Translation into one running system
- `main.py` orchestrates all components
- Real multilingual conversation: Ahmad (Urdu) ↔ Yuki (Japanese) ↔ Omar (Arabic)
- First working NovxX Phase 1 Communication demo

### Day 10 — FastAPI Introduction
- FastAPI app setup, `uvicorn main:app --reload`
- GET/POST routes, URL parameters, query parameters
- Pydantic `BaseModel` for request validation
- `HTTPException` for error responses
- Auto-generated `/docs` (Swagger UI)
- Built: Full REST API — 7 endpoints for users, conversations, messages
- Key insight: `UserCreate` (Pydantic) = validator; `User` (class) = real logic

### Day 11 — PostgreSQL Setup
- Installed PostgreSQL 18, created `global_systemDB2` database
- Installed `sqlalchemy`, `psycopg2-binary`
- Created `database.py` — engine, SessionLocal, Base, `get_db()`
- Created `Models/db_models.py` — UserDB, ConversationDB, MessagesDB
- SQLAlchemy relationships: `relationship()`, `ForeignKey()`, `back_populates`
- Ran `create_db.py` — 3 tables created in pgAdmin

### Day 12 — PostgreSQL + FastAPI Wired
- `Depends(get_db)` — session injection per request
- CRUD with SQLAlchemy: `db.add()`, `db.commit()`, `db.refresh()`, `.first()`, `.all()`
- Rewrote all routes to use real DB instead of memory
- Key bug fixed: missing `.first()` on queries returns Query object not data
- Milestone: **Data survived server restart** — first real persistence achieved

### Day 13 — JWT Authentication
- Installed `python-jose`, `passlib[bcrypt]`, `python-multipart`
- Password hashing: `pwd_context.hash()` / `pwd_context.verify()`
- JWT: `create_token()` encodes user_id with 30-min expiry
- `get_current_user()` — decodes token, fetches user from DB
- `Depends(get_current_user)` — protects any route
- Built: `POST /register`, `POST /login`, `GET /me`, `POST /messages/send`
- Tested: 401 Unauthorized on protected routes without token

### Day 14 — AI Integration (Phase 1 + 2 + 3)
- Installed `groq` library
- Connected Llama 3.1 (via Groq free API) to NovxX
- Created `Services/ai_service.py` with NovxX AI personality system prompt
- `chat_with_ai()` — core function, auto-translates response to user's language
- `get_study_help()` — Phase 2 Learning Assistant
- `get_business_help()` — Phase 3 Business Assistant
- Built: `/ai/chat`, `/ai/learn`, `/ai/business`, `/ai/test` endpoints
- Security: Moved all secrets to `.env` file, added to `.gitignore`
- Tested: AI responding in Urdu, Japanese, Arabic automatically per user language

### Day 15 — MVP Complete (coming)
- React frontend connection
- Full NovxX V1 demo

---

## 🗺️ Roadmap

### Phase 1 — Communication ✅
- [x] Multilingual AI chat
- [x] Real-time translation
- [x] User registration + auth
- [x] Conversation + message system

### Phase 2 — Learning Assistant ✅
- [x] AI topic explanation
- [x] Multi-language responses
- [ ] Study plan generation (coming)
- [ ] Book summaries (coming)

### Phase 3 — Business Assistant ✅
- [x] Email generation
- [x] Professional writing help
- [ ] Document translation (coming)
- [ ] Task management (coming)

### Phase 4 — Developer Assistant 🔜
- [ ] Coding help
- [ ] Documentation generation
- [ ] Technical content translation

### Phase 5 — Healthcare Support 🔜
- [ ] Health information access
- [ ] Medical translation
- [ ] Wellness tracking

### Phase 6 — Voice AI 🔜
- [ ] Speech to text (Whisper)
- [ ] Text to speech
- [ ] Real-time voice translation

---

## 👨‍💻 Developer Notes

- **Recurring bug pattern (Days 1-8):** Placing "not found" returns inside `else` blocks within `for` loops instead of after loop completion. Fixed by always placing fallback `return`/`print` outside the loop body.
- **Key architectural decision:** `UserCreate` (Pydantic) handles validation only. `UserDB` (SQLAlchemy) handles persistence. Kept separate intentionally.
- **Translation approach:** `deep-translator` (GoogleTranslator) used for prototyping. Will migrate to official Google Cloud Translate or DeepL for production.
- **AI approach:** Groq + Llama 3.1 for free tier. Architecture supports swapping to Claude or GPT-4 in one line (`ai_service.py`).

---

## 📄 License

MIT License — Built with purpose by Umair Khan, Tank KPK Pakistan 🇵🇰

---

*NovxX — Breaking language barriers. One message at a time.*
