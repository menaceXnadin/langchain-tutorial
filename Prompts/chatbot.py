from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv(override=True)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chat_history = []
while True:
    user_input= input("You: ")
    chat_history.append({'user':user_input})
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    prompt = f"You are a helpful AI chatbot. Answer the following question:\n{user_input} and this is the chat history so far: {chat_history} and dont hallucinate"
    response = llm.invoke(prompt)
    print("Bot : ",response.content)
    chat_history.append({'ai':response.content})