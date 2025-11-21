from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="give the sentiment of the review")


parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template='classify the feedback text into positive or negative \n{feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={
        'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2
feedback = "I absolutely love this product! It works perfectly and exceeded my expectations."
# result =classifier_chain.invoke({"feedback":feedback})
# print(result.sentiment)
# print(type(result))
prompt2 = PromptTemplate(
    template='The following feedback is positive. Write a short, appreciative reply:\n{feedback}',
    input_variables=['feedback'],
)

prompt3 = PromptTemplate(
    template='The following feedback is negative. Write a short, empathetic, and constructive reply:\n{feedback}',
    input_variables=['feedback'],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model1 | parser),
    RunnableLambda(lambda x: "couldnt find sentiment")
)
chain = classifier_chain | branch_chain
print(chain.invoke({'feedback': feedback}))
chain.get_graph().print_ascii()