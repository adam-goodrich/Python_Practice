def comfortable_word(word):
    left = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
    right = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]
    index = 0
    for i in word:
        while i in left:
            if i in right:
                continue

            else:
                return False
        while i in right:
            if i in left:
                continue
            else:
                return False
        else:
            return True
        

print(comfortable_word('yam'))