import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser

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

class Destino(BaseModel):
    cidade: str  = Field(description="cidade a visitar")
    motivo: str  = Field(description="motivo pelo qual e interessante visitar")

modelo_cidade = "Sugira uma cidade dado meu interesse por {interesse}. A sua saida deve ser SOMENTE o nome da cidade. {formatacao_de_saida}"

parseador = JsonOutputParser(pydantic_object=Destino)

prompt = PromptTemplate(
    template = modelo_cidade,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)

chain = prompt | llm | parseador

response = chain.invoke({"interesse": "praia"})

print(response)
