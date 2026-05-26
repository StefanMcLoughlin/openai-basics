from openai import OpenAI
import json
from utils import clean_json_output

def main():

    client = OpenAI()

    running = True

    while running:
        article_text = input("Bitte Artikel eingeben: ")

        try:
            data = summarize_news(article_text, client)

            print("Kategorie:", data["category"])
            print("Sentiment:", data["sentiment"])
            print("Zusammenfassung:", data["summary"])
            print("Key Points:")
            for point in data["key_points"]:
                print("-", point)
            print("TLDR:", data["tldr"])

        except json.JSONDecodeError:
            print("Fehler: Die AI Antwort war kein gültiges JSON.")

        continue_program = input("Weitere News analysieren? (ja/nein): ")
        if continue_program.lower() == "nein":
            running = False


def summarize_news(article_text, client):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Analysiere folgenden News Artikel.

        Gib die Antwort ausschließlich als JSON zurück.

        Die JSON soll enthalten:
        - category (Kategorie des Artikels)
        - sentiment (Bewertung der allgemeinen Tonalität des Artikels)
        - summary (Eine kurze Zusammenfassung in 2-3 Sätzen)
        - key_points (Liste der 3 wichtigsten Punkte des Artikels)
        - tldr (Sehr kurze Zusammenfassung in maximal einem Satz)

        Für sentiment sind nur folgende Werte erlaubt:
        - positiv
        - neutral
        - negativ

        Artikel:
        "{article_text}"
        """

    )

    clean_output = clean_json_output(response.output_text)
    data = json.loads(clean_output)
    return data


if __name__ == "__main__":
    main()