from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm= HuggingFaceEndpoint(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    task="text-generation"

)
model = ChatHuggingFace(llm=llm)
template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables=['topic']
)
template2 = PromptTemplate(
    template = "write a 5 line summary on following text. {text}",
    input_variables=['text']
)
parser = StrOutputParser()
chain = template1 | model | parser | template2 | model |parser

result = chain.invoke({'topic':'blackhole'})
print(result)
# prompt1 = template1.invoke({'topic':"black hole"})
# result1 = model.invoke(prompt1)
# print(result1.content)
# prompt2 = template2.invoke({'text': result1.content})
# result2 = model.invoke(prompt2)
# print(result2.content)