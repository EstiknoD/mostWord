text = input('File name (only .txt and in the same path): ')
content = []
with open(text, "r") as f:
    content = f.readlines()

if(content == []):
    print('The file does not have content')
    exit(0)

def sawWords():
    word = ''
    mosreWOrds = []
    mosreWOrds1 = {}
    for sentence in content:
        mostword = ''
        candidatestothemostword = []
        candidatestothemostword1 = {}
        for word in sentence.split():
            if(word in candidatestothemostword):
                candidatestothemostword1[word]["times"] += 1
            else:
                candidatestothemostword1[word] = {
                    "word": word,
                    "times": 1
                }
                candidatestothemostword.append(word)
        for canditate in candidatestothemostword:
            if(mostword == ''):
                mostword = canditate
            else:
                if(candidatestothemostword1[canditate]["times"] > candidatestothemostword1[mostword]["times"]):
                    mostword = canditate
        mosreWOrds.append(mostword)
        try:
            mosreWOrds1[mostword] = {
                "word": mostword,
                "times": candidatestothemostword1[mostword]["times"]
            }
        except:
            pass

    for cantidates in mosreWOrds:
        if (word == ''):
            word = cantidates
        else:
            try:
                if (mosreWOrds1[cantidates]["times"] > mosreWOrds1[cantidates]["times"]):
                    word = cantidates
            except:
                pass
    return word

print(sawWords())