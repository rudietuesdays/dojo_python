import re
def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    matches = []

    for word in words:
    	if re.search(regex,word):
            matches.append(word)
    print matches

v_regex = 'v'
ss_re = (r's+s')
endE = ('e+$')
bbs = (r"b.b")
bb1 = (r"b.+b")
bb0 = (r'b.*b')
vowels = (r'[^aeiou]*?')

get_matching_words(vowels)
