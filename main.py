from langchain.llms import OpenAI   

api_key = "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"

llm = OpenAI(
    openai_api_key=api_key,                   
    )
result = llm("What is the meaning of life?")