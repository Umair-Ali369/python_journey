import os
from groq import Groq
from dotenv import load_dotenv
from Services.translator import translate_text

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

GLOBAL_SYSTEM_PROMPT = """
You are Global System AI - an intelligent , multilingual assistant build
into the global system platform.
Your purpose is to help user communicate, learn, and grow access lannguage
barries.
You are:
- Helpful, friendly, and concise
- Knowledgeable across all topics
- Culturally aware and respectful
- Always responding in English (translation is handled separately)
Keep responses clear and under 200 words unless the user asks for detail.
"""

def chatWithAI(
    message : str,
    user_language : str = "en",
    conversation_history : list =  []
) -> dict:
   """
   Send a message to global system and get a response.
   Automatically transalte response into user's language.
   """
   try:
       messages = [{"role" : "system", "content" : GLOBAL_SYSTEM_PROMPT}]
       for msg in conversation_history:
         messages.append(msg)

       messages.append({"role" : "user", "content" : message})

       response = client.chat.completions.create(
           model  = "llama-3.1-8b-instant",
           messages = messages,
           max_tokens = 500,
           temperature = 0.7
       )
        
       ai_response = response.choices[0].message.content
       if user_language != "en":
            translatedResponse = translate_text(ai_response, user_language)
       else:
           translatedResponse = ai_response

       return {
           "success" : True,
           "original_response" : ai_response,
           "translated_response" : translatedResponse,
           "model" : "llama-3.1-8b-instant",
           "user_language" : user_language
       }
    
   except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "original_response": None,
            "translated_response": None
        }

def get_study_help(
    topic : str, user_language : str = "en"
) -> dict:
    """
    Global System Learning Assistant 
    Explain any topic in simple words 
    """
    promt = f"""
    Explain '{topic}' in simple words, essy to understand terms.
    Use an analogy if helpfull.
    Keep It under 150 words
    """

    return chatWithAI(promt, user_language)

def get_business_help(
    task : str, user_language : str = "en"
) -> dict:
    """
    Global System Business Assistant 
    """
    promt = f"""
    You are professional business assistant.
    Help with this business task : {task}
    Be professional and concise.
    """

    return chatWithAI(promt, user_language)