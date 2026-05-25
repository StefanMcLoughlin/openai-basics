from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Schreibe eine kurze, professionelle Antwort auf eine Kundenemail."
)

print(response.output_text)