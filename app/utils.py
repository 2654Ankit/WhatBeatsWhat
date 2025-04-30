# from profanity_filter import ProfanityFilter

# pf = ProfanityFilter()

# def clean_text(text):
#     return pf.censor(text)

def format_response(seed, guess, count):
    return f"✅ Nice! '{guess}' beats '{seed}'. It has been guessed {count} times before."
