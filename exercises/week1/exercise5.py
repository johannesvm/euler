
with open('names.txt', 'r') as f:
    string = f.read()
    names = string.split(',')
    for i in range( len(names)):
        names[i] = names[i][1:-1]
    names = sorted(names)
    
    scores = []
    for name in names:
        score = 0
        for letter in name:
            score += ( ord(letter) - 64)
        scores.append(score)
        
    for i in range( len(names)):
        scores[i] *= (i+1)
