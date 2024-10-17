import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.globals import set_debug


from dotenv import load_dotenv

load_dotenv()
set_debug(True)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

modelo_cidade = ChatPromptTemplate.from_template("Sugira uma cidade dado meu interesse por {interesse}. A sua saida deve ser SOMENTE o nome da cidade. ")
modelo_restaurantes = ChatPromptTemplate.from_template("Sugira restaurantes populares entre locais em {cidade}")
modelo_cultural = ChatPromptTemplate.from_template("Sugira atividades e locais culturais em {cidade}")

prompt = ChatPromptTemplate.from_messages(
    [
       modelo_cidade,
       modelo_restaurantes,
       modelo_cultural
    ]
)

chain = prompt | llm

response = chain.invoke({
    "interesse": "praia",
    "cidade":""
})

print(response.content)
