import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv(override=True)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
st.title("Research Summarizer")
research_papers = [
    "Learning Dynamics of LLM Finetuning",
    "Unveiling Over‑Memorization in Finetuning LLMs for Reasoning Tasks",
    "SAM 2: Segment Anything in Images and Videos",
    "SAM2Long: Enhancing SAM 2 for Long Video Segmentation with a Training‑Free Memory Tree",
    "Data Shapley in One Training Run",
    "Explainable AI (XAI): A Systematic Meta‑Survey of Current Challenges and Future Opportunities",
    "Machine Learning Testing: Survey, Landscapes and Horizons",
    "Attention Is All You Need",
    "Computing Machinery and Intelligence",
    "Explainable Artificial Intelligence: a Systematic Review"
]
paper_input = st.selectbox("Select a research paper:",research_papers)
style_input = st.selectbox("Select a summarization style:",["Beginner Friendly","Technical","Code-Oriented","Mathemtical"])
length_input = st.selectbox("Select summary length:",["Short (1 paragraph)","Medium (3-5 paragraph)","Long (1 page)"])
prompt_template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template="""
You are an expert in AI and Machine Learning. 
Your task is to provide a comprehensive summary of the research paper titled "{paper}". 

The summary should follow these instructions:
1. Style: "{style}" — make sure the tone and detail match this style.
2. Length: "{length}" — adhere to the length guidelines.
3. Include key insights, main contributions, important methods, and any notable results.
4. Make it clear, coherent, and easy to understand for the chosen style.
5. Only summarize information that is explicitly available in the paper. 
   If certain details are missing or unclear, do not make guesses or add information.

Avoid adding personal opinions; focus only on the content of the paper.
"""
)

if st.button("Summarize"):
    final_prompt =prompt_template.format(paper=paper_input,style=style_input,length=length_input)
    with st.spinner("Generating summary..."):
        summary = llm.invoke(final_prompt)
    st.subheader("Summary:")
    st.write(summary.content)