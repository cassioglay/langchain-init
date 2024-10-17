import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

modelo_do_prompt = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma família com {criancas} crianças, que gostam de {atividade}."
)

prompt = modelo_do_prompt.format(
    dias=numero_de_dias,
    criancas=numero_de_criancas,
    atividade=atividade
)

print(prompt)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

reposnse = llm.invoke(prompt)
print(reposnse.content)