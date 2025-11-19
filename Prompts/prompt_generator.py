from langchain_core.prompts import PromptTemplate
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
prompt_template.save("research_template.json")
