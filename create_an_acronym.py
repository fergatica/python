def create_an_acronym(name):
    name = name.upper()
    acronym = ""
    for words in name.split():
        acronym = acronym + words[0]
    return acronym

