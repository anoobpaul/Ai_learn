from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI 
import os

os.environ["OPENAI_API_KEY"] = "sk-**************************************pd"
model_name = "gpt-3.5-turbo-0125"

llm = ChatOpenAI(model_name=model_name)
response = llm.invoke("explain bitcoin in 5 bullet points?")
print(response)
