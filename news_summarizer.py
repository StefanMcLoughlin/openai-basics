from openai import OpenAI
import json

def main():

    client = OpenAI()

    article_text = input("Bitte Artikel eingeben: ")

    result = summarize_news(article_text, client)

    print(result)


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

    return response.output_text

if __name__ == "__main__":
    main()