import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

from dotenv import load_dotenv

load_dotenv()
set_debug(True)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=3,
)

class Destino(BaseModel):
    cidade: str  = Field(description="cidade a visitar")
    motivo: str  = Field(description="motivo pelo qual e interessante visitar")

parseador = JsonOutputParser(pydantic_object=Destino)

tamplate1 = "Sugira uma cidade dado meu interesse por {interesse}. A sua saida deve ser SOMENTE o nome da cidade. {formatacao_de_saida}"

prompt1 = PromptTemplate(
    template = tamplate1,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()}
)

tamplate2 = "Sugira restaurantes populares entre locais em {cidade}"

prompt2 = PromptTemplate(
    template = tamplate2,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()}
)

tamplate3 = "Sugira atividades e locais culturais em {cidade}"

prompt3 = PromptTemplate(
    template = tamplate3,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()}
)

parte1 = prompt1 | llm | parseador 

parte2 = prompt2 | llm  | StrOutputParser()

parte3 = prompt3 | llm  | StrOutputParser()

cadeia = (parte1 | parte2 | parte3)

response = cadeia.invoke({"interesse": "praias"})

print(response)