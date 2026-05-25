from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="""
    Analysiere folgende Kundenemail.

    Gib die Antwort ausschließlich als JSON zurück.

    Die JSON soll enthalten:
    - category
    - priority
    - summary
    - suggested_reply

    Kundenmail:
    "Hallo, ich habe gestern eine Rechnung erhalten, obwohl ich bereits bezahlt habe. Bitte prüfen Sie das."
    """
)

print(response.output_text)