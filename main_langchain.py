import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
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