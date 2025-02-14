import openai
import os

# Recupera a chave da OpenAI dos Secrets do GitHub
openai.api_key = os.getenv("OPENAI_API_KEY")

# Envia uma mensagem para o ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Você está integrando o ChatGPT com GitHub."},
        {"role": "user", "content": "Explique como conectar o ChatGPT ao GitHub Actions."}
    ]
)

# Exibe a resposta do ChatGPT
print(response["choices"][0]["message"]["content"])
