# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "datasets",
#     "huggingface_hub<1.0",
# ]
#
# ///

from datasets import load_dataset

ds = load_dataset("princeton-hf-workshop/affordable-housing")

def format_conversation(sample: dict) -> dict:
    conversation = [
        {"role": "system", "content": "/no_think"},
        {
            "role": "user",
            "content": f"""
In this housing survey, respondents were asked to create what their least-favorite and most-favorite new buildings
would look like in their neighborhoods. Respondents were then asked what they would say about each building
at a city council meeting on housing.  The column main.byo_worst_words contains what respondents would say at a meeting about their
least-ideal building. Classify what the main concern is for each response from each respondent. The values of these questions may be "BLANK" if the
respondent did not provide an answer. The user will provide you with the values of these two questions, and you will respond with either
"safety", "density", "traffic/parking", "home values", "classism", "affordability", "racial resentment", "not needed" or "unclear/other".

Respond "affordability" if the respondent would say that they are concerned with costs. For example,"I would be concerned about being priced
out of my neighborhood if expensive units like this are built".

Vague statements should be coded as "unclear/other", such as, one value of main.byo_worst_words is "I would oppose the development". 
This value does not contain any information about why the
respondent would opppose the development, thus you should respond with "unclear/other". 
Another value states "Keep my neighborhood as is please."
Again, this does not specify why the respondent wants to maintain the status quo and should be labeled "unclear/other". Excessively short responses
such as simply "yes" should be coded as "unclear/other". 

Another value of main.byo_worst_words is "I am totally apposed to adding apartments to our single family area". This sentence suggests the
respondent doesn't want apartments in the area and wants to maintain their area as "single family". You should respond with "density".

An example that should be responded with "classism" is "Do not let low income people live in my neighborhood." Do not label concerns about affordability
such as "Rich people shouldn't take up apartments from people that can't afford homes" as classism.

Respond "home values" only if the respondent is concerned about the value of their home depreciating, not if their concern is affordability. 

If the value of main.byo_worst_words is "BLANK" or null you should respond with "unknown".

Answer of the respondent:
main.byo_worst_words: {sample["main.byo_worst_words"] or "BLANK"}
""",
        },
    ]
    sample["messages"] = conversation
    return sample

ds = ds.map(format_conversation)
ds.push_to_hub("princeton-hf-workshop/affordable-housing-conversations")
