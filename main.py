from langchain.llms import OpenAI    # type: ignore
from langchain.prompts import PromptTemplate  # type: ignore
from langchain.chains import LLMChain  # type: ignore

api_key = "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"

llm = OpenAI(
    openai_api_key=api_key,                   
    )

code_prompt = PromptTemplate(
    
)
result = llm("What is the meaning of life?")
print(result)