
def count_chars(string):
    d = {}
    string = string.lower()
    for c in string:
        if c != ' ' and c != ',' and c != '!' and c != '?':
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    return d
                
example = "Hello, world!"
d = count_chars(example)
for char, count in d.items():
    print('{:3}{:10}'.format(char, count))

print('\n')

# Sorter i alfabetisk rekkefølge
for key in sorted(d.keys()):
    print('{:3}{:10}'.format(key, d[key] ))

print('\n')

# Sorter etter frekvens
for key, value in sorted(d.items(), key =lambda x: x[1]):
    print('{:3}{:10}'.format(key, value))
