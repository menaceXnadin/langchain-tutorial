from gradio.server_messages import BaseMessage
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chat_history  = [
    SystemMessage(content="You are a helpful AI chatbot. Answer the user's questions based on the chat history without hallucinating."),

]
while True:
    user_input = input("You : ")
    if user_input.lower() in ["exit","quit"]:
        break
    chat_history.append(HumanMessage(content=user_input))
    response = llm.invoke(chat_history)
    print(response.content)
