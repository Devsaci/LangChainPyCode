from langchain.llms import OpenAI    # type: ignore
from langchain.prompts import PromptTemplate  # type: ignore
from langchain.chains import LLMChain  # type: ignore
from langchain_openai import OpenAI  # type: ignore


llm = OpenAI(
    openai_api_key="",                   
    )
poem_prompt = PromptTemplate(
    input_variables=["subject"],
    template="Write a very short poem about {subject}"
)
poem_chain = LLMChain(
    llm=llm,
    prompt=poem_prompt
)
 
result = poem_chain({ "subject": "snow" })
 
print(result)