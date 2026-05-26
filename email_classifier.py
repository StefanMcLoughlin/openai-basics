from openai import OpenAI
import json
from utils import clean_json_output

def main():

    client = OpenAI()

    running = True

    while running:
        customer_email = input("Bitte Kundenmail eingeben: ")

        try:
            data = analyze_email(customer_email, client)

            print("Kategorie:", data["category"])
            print("Priorität:", data["priority"])
            print("Zusammenfassung:", data["summary"])
            print("Antwortvorschlag:", data["suggested_reply"])

        except json.JSONDecodeError:
            print("Fehler: Die AI Antwort war kein gültiges JSON.")

        continue_program = input("Weitere Email analysieren? (ja/nein): ")
        if continue_program.lower() == "nein":
            running = False


def analyze_email(customer_email, client):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Analysiere folgende Kundenemail.

        Gib die Antwort ausschließlich als JSON zurück.

        Die JSON soll enthalten:
        - category
        - priority
        - summary
        - suggested_reply

        Für category sind nur folgende Werte erlaubt:
        - abrechnung
        - technik
        - allgemeine_anfrage

        Für priority sind nur folgende Werte erlaubt:
        - niedrig
        - mittel
        - hoch

        Kundenmail:
        "{customer_email}"
        """
    )

    clean_output = clean_json_output(response.output_text)
    data = json.loads(clean_output)
    return data

if __name__ == "__main__":
    main()