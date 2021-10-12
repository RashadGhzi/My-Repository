
def machingWord(sentence1,sentence2):
    word1 = sentence1.lower().strip().split(" ")
    word2 = sentence2.lower().strip().split(" ")

    score = 0
    for word1 in word1:
        for word2 in word2:
            if word1 == word2:
                score += 1
    return score

if __name__ == '__main__':

    print('Enter your word that you want to mach:')
    word = input()
    stringItem = ["Python is a good", "This is snake",
                 "Harry is is is a good boy", "Subscribe to code with harry","We like to meet with Harry vai", "Harry vai is a good person"]

    scores = [machingWord(word,sentence) for sentence in stringItem]
    sorted_item = sorted(zip(scores,stringItem),reverse=True)

    found_score = [item for item in scores if item != 0]
    print(f"{len(found_score)} result found.")

    for serial, item in sorted_item:
        if serial > 0:
            print(f"\"{item}\"")



