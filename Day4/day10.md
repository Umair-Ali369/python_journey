## 🚀 Quick Start Guide

Follow these step-by-step instructions to get the application up and running on your local machine.

### 1. Install Dependencies
Open your terminal inside the project directory and install the required core packages:
```bash
pip install fastapi uvicorn pydantic
```

### 2. Launch the Application Server
Run the Uvicorn ASGI server with hot-reloading enabled:
```bash
uvicorn app:app --reload
```
*Your terminal will display:* `INFO: Uvicorn running on http://127.0.0.1:8000`

### 3. Open the Interactive Browser UI
FastAPI automatically generates an interactive visual documentation panel. Open your browser and navigate to:
👉 **http://localhost:8000/docs#/**

---

## 🛠️ Complete API Workflow (Step-by-Step)

To populate data and test the application system correctly within your browser, execute requests in this exact workflow sequence:

### Step 1: Create Users (`POST /users`)
Register your system participants. The database automatically auto-increments IDs starting from `1`.
* **Payload Examples:**
  ```json
  { "name": "Ahmad", "language": "ur", "age": 22, "is_premium": false }   // Generates ID 1
  { "name": "Yuki", "language": "ja", "age": 25, "is_premium": false }    // Generates ID 2
  { "name": "Omar", "language": "ar", "age": 30, "is_premium": false }    // Generates ID 3
  ```

### Step 2: Establish a Conversation (`POST /conversations`)
Link two existing user profiles together inside a private conversation room.
* **Payload Example (Ahmad <-> Yuki):**
  ```json
  {
    "user1_id": 1,
    "user2_id": 2
  }
  ```
* **Expected Response:** Returns a `Conversation_id` (e.g., `1`).

### Step 3: Send Translated Chat Messages (`POST /messages`)
Transmit text string values inside an established conversation room. The backend processes language localization seamlessly.
* **Payload Example (Ahmad sending to Room 1):**
  ```json
  {
    "conversation_id": 1,
    "sender_id": 1,
    "text": "How are baby? I love girl who love me a lot."
  }
  ```

### Step 4: Fetch Chat History Logs (`GET /conversations/{conv_id}/messages`)
Retrieve arrays of stored original text, metadata, and calculated translations.
* **Path Parameters:** Change `{conv_id}` inside the input field to `1`.
* **Action:** Click **Execute** to read data strings safely.

---

## 📡 API Core Routes Reference

| HTTP Method | API Endroute Path | Description |
| :--- | :--- | :--- |
| **GET** | `/` | System diagnostics home page. |
| **GET** | `/users` | Lists details for all registered accounts. |
| **POST** | `/users` | Provisions a new default or Premium profile. |
| **GET** | `/users/{user_id}` | Searches profile dictionary by user ID. |
| **POST** | `/conversations` | Initializes communication rooms between users. |
| **POST** | `/messages` | Stores text values and prompts automated translation. |
| **GET** | `/conversations/{conv_id}/messages` | Fetches complete message blocks for a specific conversation room. |

---

## ⚠️ Known Error Statuses

* **`404 One or both Users not found!`**: Prompted during room creation if user IDs do not exist in system memory arrays.
* **`404 Conversation not Found!`**: Prompted when attempting to post a message into an uninitialized or broken room ID.
* **`422 Unprocessable Entity`**: Data validation structure fault. Double check that field data types perfectly match schema specs (e.g. sending strings instead of an integer for `age`).