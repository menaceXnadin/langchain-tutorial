from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm = HuggingFaceEndpoint(model="meta-llama/Llama-3.1-8B-Instruct")
model2 = ChatHuggingFace(llm=llm)
prompt1 = PromptTemplate(
    template = "Generate short and simple notes from the following text {text}",
    input_variables = ['text']
)
prompt2 = PromptTemplate(
    template = "Generate quizes from the following text {text}",
    input_variables = ['text']
)
prompt3 = PromptTemplate(
    template = "merge the provided notes and quiz into a single document \n notes-> {notes}and quiz-> {quiz}",
    input_variables = ['notes','quiz']
)
parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'notes':prompt1 | model1 |parser,
    'quiz': prompt2 |model2|parser
})
merge_chain = prompt3 | model1|parser
chain = parallel_chain|merge_chain
text =  """
Title: Linear Regression

Linear regression is a supervised learning method used to predict a continuous value based on input variables. It fits a straight line that best represents the relationship between the independent variables and the dependent variable.

There are two types.

Simple Linear Regression uses one input variable.

Multiple Linear Regression uses two or more input variables.

The model assumes that the relationship is linear, errors are independent, variance of errors is constant, and predictors are not highly correlated.

It is trained using the least squares method, which finds coefficients that minimize the difference between predicted and actual values.

Common evaluation metrics include MSE, RMSE, MAE, and R squared.

Advantages include simplicity, interpretability, and fast training. Limitations include sensitivity to outliers and poor performance when relationships are non-linear.

Linear regression is widely used for forecasting, price prediction, scientific analysis, and trend estimation.
"""
# result = chain.invoke({'text': text})
# print(result)
chain.get_graph().print_ascii()