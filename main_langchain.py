import os
from langchain_groq import ChatGroq
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
print(prompt)

llm = ChatGroq