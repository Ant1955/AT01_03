def vowels(message):
    vowels = "aeiouAEIOUуеёыаоэяиюУЕЁЫАОЭЯИЮ"
    n = 0
    for char in message:
        if char in vowels:
            n += 1
    return n
