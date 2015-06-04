def translate(old_text):
    dictionary= {
        "hi":"salutations",
        "it":"the object of which you speak" ,
        "you":"my fine aquaintance",
        "mom":"maternal relation"
        #"i": "the person who currently presents themself"
    }
    old_text=old_text.lower()
    for key in dictionary.keys():
        old_text = old_text.replace(key,dictionary[key])
    return old_text