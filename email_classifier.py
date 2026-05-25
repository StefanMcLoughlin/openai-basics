from openai import OpenAI
import json

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

clean_output = response.output_text.strip()

clean_output = clean_output.removeprefix("```json")
clean_output = clean_output.removeprefix("```")
clean_output = clean_output.removesuffix("```")

clean_output = clean_output.strip()

data = json.loads(clean_output)

print("Kategorie:", data["category"])
print("Priorität:", data["priority"])
print("Zusammenfassung", data["summary"])
print("Antwortvorschlag:", data["suggested_reply"])