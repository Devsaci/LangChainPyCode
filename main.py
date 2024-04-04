from langchain.llms import OpenAI    # type: ignore
from langchain.prompts import PromptTemplate  # type: ignore
from langchain.chains import LLMChain  # type: ignore
from langchain_openai import OpenAI  # type: ignore



llm = OpenAI(
    openai_api_key="",                   
    )

code_prompt = PromptTemplate(
    template = "write  a very simple {language} function that will return {task} ",
    input_variables = ["language", "task"]
)

code_chain = LLMChain(
    llm = llm,
    prompt = code_prompt
)

result = code_chain({
    "language": "python", 
    "task": "return a list of numbers from 1 to 10"
    })

print(result["text"])