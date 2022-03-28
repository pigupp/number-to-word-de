def numtotext(num):
    # Create Dictionary
    text = {
        0: "null",
        1: "ein",
        "1": "eins",
        2: "zwei",
        3: "drei",
        4: "vier",
        5: "fünf",
        6: "sechs",
        7: "sieben",
        8: "acht",
        9: "neun",
        10: "zehn",
        11: "elf",
        12: "zwölf",
        13: "dreizehn",
        14: "vierzehn",
        15: "fünfzehn",
        16: "sechzehn", 
        17: "siebzehn",
        18: "achtzehn",
        19: "neunzehn",
        20: "zwanzig",
        30: "dreißig",
        40: "vierzig",
        50: "fünfzig",
        60: "sechzig",
        70: "siebzig",
        80: "achtzig",
        90: "neunzig",
        100: "hundert",
        1000: "tausend",
        "and": "und"
        }

    # Error
    if num > 1000 or num < 0:
        return "Error"
    # Translate
    # 0-19
    if num < 20:
        if num == 1:
            return text["1"]
        else:
            return text[num]
    # 20-99
    if num < 100:
        if num % 10 == 0:
            return text[num]
        else:
            return text[num % 10] + text["and"] + text[(num // 10) * 10]
    # 100-999
    if num < 1000:
        if num % 100 == 0:
            return text[num // 100] + text[100]
        else:
            return text[num // 100] + text[100] + numtotext(num % 100)
    # 1000
    if num == 1000:
        return text[num // 1000] + text[num]

# Input
zahl = int(input("Zahl von 0 bis 1000: "))
print("-> " + str(zahl) + ": " + numtotext(zahl).capitalize() + "\n")

input()
