



def extract_feature(opinion, selector, attribute=None):
    try:
        if not attribute:
            return opinion.select(selector).pop().get_text().strip()
        else:
            return opinion.select(selector).pop()[attribute]
    except IndexError:
        return None



def remove_whitespace(text):
    
    try:
        for char in ["\n","\r"]:
            return text.replace(char, ", ")
    except AttributeError:
        pass     