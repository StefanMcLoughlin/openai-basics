def clean_json_output(output):

    clean_output = output.strip()

    clean_output = clean_output.removeprefix("```json")
    clean_output = clean_output.removeprefix("```")
    clean_output = clean_output.removesuffix("```")

    clean_output = clean_output.strip()

    return clean_output