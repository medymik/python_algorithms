def howMany(paragraph, word):
    count = 0
    pos = 0
    for ch in paragraph:
        if ch == word[pos]:
            pos += 1
        else:
            pos = 0
        if pos == len(word):
            pos = 0
            count += 1
    return (count)

if __name__ == '__main__':
    assert(howMany("hello world", "hello") == 1)
    assert(howMany("hella world", "hello") == 0)
    assert(howMany("world hella world", "world") == 2)
    assert(howMany("corcorpycore", "cor") == 3)
