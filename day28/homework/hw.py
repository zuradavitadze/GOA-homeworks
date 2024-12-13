def search(text, word):
    count = 0
    start = 0
    while True:
        pos = text.find(word, start)
        if pos == -1:
            break
        count += 1
        start = pos + len(word)
    return count