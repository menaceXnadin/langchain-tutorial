from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm= HuggingFaceEndpoint(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    task="text-generation"

)
model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
template = PromptTemplate(
    template="Give me the name,age and address of the fictional person\n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt = template.format()
chain = template | model | parser
result = chain.invoke({})
print(result)
# result = model.invoke(prompt)
# print(result.content)
# final_result = parser.parse(result.content)
# print(final_result)
# print(type(final_result))