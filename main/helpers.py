from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os
from main.prompt_templates import basic_template, veterinarian_template

# SETTINGS
KEY = os.environ["OPENAI_API_KEY"]

# basic chat response
def respond_to_message(
        user_input: str = "hello",
        template_name: str = "basic"
):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=KEY)
    if template_name == "basic":
        base_template = basic_template
        prompt = PromptTemplate.from_template(template=base_template)
    else:
        base_template = veterinarian_template
        prompt = ChatPromptTemplate.from_messages(base_template)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    # Process the incoming message
    response = chain.invoke({"user_input": user_input})
    return response