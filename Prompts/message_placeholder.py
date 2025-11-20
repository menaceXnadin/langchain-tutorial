from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
import os

prompt = ChatPromptTemplate([
    ('system','you are a helpful customer agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')])
chat_history = []
try:
    with open(os.path.join(os.path.dirname(__file__), 'chat_history.txt')) as f:
        chat_history.extend(f.readlines())
except FileNotFoundError:
    pass

print(chat_history)

prompt.invoke({'chat_history':chat_history,'query':'where is my refund?'})