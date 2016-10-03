import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

print get_matching_words('v')
print get_matching_words('ss')
print get_matching_words('e\Z')
print get_matching_words('e$') #same as above
print get_matching_words('b.b')
print get_matching_words('b.+b')
print get_matching_words('b.*b')
print get_matching_words('a.*e.*i.*o.*u.*')
# regularxpsion
print get_matching_words('^[regularxpsion]*$')
print get_matching_words('(.)\\1')
