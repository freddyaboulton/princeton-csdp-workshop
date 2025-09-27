# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "datasets",
# ]
#
# ///

from datasets import load_dataset

ds = load_dataset("freddyaboulton/affordable-housing", split="train")

def format_conversation(sample: dict) -> dict:
    conversation = [
        {"role": "system",
         "content": """
You are a helpful assistant that will classify whether a survey respondent's
attitude towards affordable housing is positive, negative, neutral, or ambiguous based on the
values of two questions called main.byo_best_words and main.byo_worst_words.
The user will provide you with the values of these two questions, and you will respond with either
"positive", "negative", "neutral", or "ambiguous".
If the values of both questions are "BLANK", you should respond with "neutral".
         """},
        {"role": "user", "content": f"""
main.byo_best_words: "{sample['main.byo_best_words'] or "BLANK"}"
main.byo_worst_words: "{sample['main.byo_worst_words'] or "BLANK"}"
        """}
    ]
    sample["messages"] = conversation
    return sample


ds = ds.map(format_conversation)
ds.push_to_hub("freddyaboulton/affordable-housing-conversations")